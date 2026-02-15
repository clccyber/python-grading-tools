import sys, os
import ast
from pathlib import Path
from .utils import run_subprocess

def half_up(n):
    return int(n + 0.5)

def grade_gui_structure(cfg, student_path):
    """
    Grade GUI exercises by checking code structure with AST.
    
    Config structure:
    exercise_id: chapter7/calculator
    mode: gui_structure
    module_file: calculator.py
    timeout_seconds: 5
    
    gui_structure_checks:
      - widget_type: Tk
        points: 10
        description: "Main window creation"
      
      - widget_type: Entry
        points: 15
        min_count: 1
        description: "Entry widget for input"
      
      - widget_type: Button
        points: 20
        min_count: 4
        must_have_command: true
        description: "Buttons with event handlers"
      
      - widget_type: Label
        points: 15
        description: "Label for output"
      
      - method_call: mainloop
        points: 10
        description: "Event loop started"
      
      - method_call: pack
        points: 10
        or_method: grid
        description: "Widgets laid out"
    """
    
    ex_id = cfg.get('exercise_id')
    module_file = cfg.get('module_file')
    checks = cfg.get('gui_structure_checks', [])
    
    if not checks:
        raise ValueError(f'No gui_structure_checks defined for {ex_id}')
    
    notes = []
    tasks = []
    
    # Find student file
    module_path = Path(student_path) / module_file
    if not module_path.exists():
        notes.append(f"File '{module_file}' not found in student directory")
        return {
            'summary': {'exercise_id': ex_id, 'score': 0, 'raw_earned': 0, 'raw_total': 100},
            'tasks': [],
            'notes': notes,
            'formatting_issues': {}
        }
    
    # Parse the code
    try:
        with open(module_path, 'r') as f:
            code = f.read()
        tree = ast.parse(code)
    except SyntaxError as e:
        notes.append(f"Syntax error in {module_file}: {e}")
        notes.append(f"  Line {e.lineno}: {e.text}")
        return {
            'summary': {'exercise_id': ex_id, 'score': 0, 'raw_earned': 0, 'raw_total': 100},
            'tasks': [],
            'notes': notes,
            'formatting_issues': {}
        }
    except Exception as e:
        notes.append(f"Error reading {module_file}: {type(e).__name__}: {e}")
        return {
            'summary': {'exercise_id': ex_id, 'score': 0, 'raw_earned': 0, 'raw_total': 100},
            'tasks': [],
            'notes': notes,
            'formatting_issues': {}
        }
    
    # Analyze the AST
    findings = analyze_gui_ast(tree)
    
    # Grade each check
    total_points = sum(check.get('points', 0) for check in checks)
    
    for check in checks:
        check_type = 'widget' if 'widget_type' in check else 'method'
        points = check.get('points', 0)
        description = check.get('description', '')
        
        task = {
            'name': description,
            'max': points,
            'earned': 0,
            'status': 'fail'
        }
        
        if check_type == 'widget':
            widget_type = check['widget_type']
            min_count = check.get('min_count', 1)
            must_have_command = check.get('must_have_command', False)
            
            count = findings['widgets'].get(widget_type, 0)
            commands_count = findings['widgets_with_command'].get(widget_type, 0)
            
            if count >= min_count:
                if must_have_command:
                    if commands_count >= min_count:
                        task['earned'] = points
                        task['status'] = 'pass'
                    else:
                        # Partial credit - found widget but missing command
                        task['earned'] = points // 2
                        task['status'] = 'partial'
                        notes.append(
                            f"{widget_type}: Found {count} widget(s) but only "
                            f"{commands_count} have command= parameter"
                        )
                else:
                    task['earned'] = points
                    task['status'] = 'pass'
            else:
                notes.append(
                    f"{widget_type}: Expected at least {min_count}, found {count}"
                )
        
        elif check_type == 'method':
            method = check['method_call']
            or_method = check.get('or_method')
            
            if method in findings['method_calls']:
                task['earned'] = points
                task['status'] = 'pass'
            elif or_method and or_method in findings['method_calls']:
                task['earned'] = points
                task['status'] = 'pass'
            else:
                if or_method:
                    notes.append(f"Missing: .{method}() or .{or_method}() call")
                else:
                    notes.append(f"Missing: .{method}() call")
        
        tasks.append(task)
    
    # Calculate final score
    raw_earned = sum(t['earned'] for t in tasks)
    raw_total = sum(t['max'] for t in tasks)
    pct = (raw_earned / raw_total) * 100 if raw_total > 0 else 0.0
    score = half_up(pct)
    score = max(0, min(100, score))
    
    return {
        'summary': {
            'exercise_id': ex_id,
            'score': score,
            'raw_earned': raw_earned,
            'raw_total': raw_total,
            'elapsed_sec': None
        },
        'tasks': tasks,
        'notes': notes,
        'formatting_issues': {}
    }

def analyze_gui_ast(tree):
    """
    Walk AST and find tkinter widget creation and method calls.
    
    Returns:
        findings = {
            'widgets': {'Tk': 1, 'Entry': 2, 'Button': 4, 'Label': 1},
            'widgets_with_command': {'Button': 3},
            'method_calls': ['mainloop', 'pack', 'grid'],
            'imports': ['tkinter', 'tkinter.ttk']
        }
    """
    
    findings = {
        'widgets': {},
        'widgets_with_command': {},
        'method_calls': set(),
        'imports': []
    }
    
    # Common tkinter widget types to look for
    widget_types = {
        'Tk', 'Toplevel', 'Frame', 'Label', 'Button', 'Entry', 'Text',
        'Listbox', 'Scrollbar', 'Canvas', 'Checkbutton', 'Radiobutton',
        'Scale', 'Spinbox', 'Menu', 'Menubutton', 'OptionMenu',
        'LabelFrame', 'PanedWindow', 'Message', 'Combobox'
    }
    
    for node in ast.walk(tree):
        # Check for imports
        if isinstance(node, ast.Import):
            for alias in node.names:
                findings['imports'].append(alias.name)
        
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                findings['imports'].append(node.module)
        
        # Check for widget creation: tk.Button(...) or Button(...)
        elif isinstance(node, ast.Call):
            widget_name = None
            has_command = False
            
            # Check function being called
            if isinstance(node.func, ast.Attribute):
                # tk.Button style
                widget_name = node.func.attr
            elif isinstance(node.func, ast.Name):
                # Button style (imported directly)
                widget_name = node.func.id
            
            # If it's a known widget type
            if widget_name in widget_types:
                # Count the widget
                findings['widgets'][widget_name] = findings['widgets'].get(widget_name, 0) + 1
                
                # Check if it has command= parameter
                for keyword in node.keywords:
                    if keyword.arg == 'command':
                        has_command = True
                        break
                
                if has_command:
                    findings['widgets_with_command'][widget_name] = \
                        findings['widgets_with_command'].get(widget_name, 0) + 1
        
        # Check for method calls: .pack(), .grid(), .mainloop(), etc.
        elif isinstance(node, ast.Attribute):
            method_name = node.attr
            # Common layout and lifecycle methods
            if method_name in {'pack', 'grid', 'place', 'mainloop', 'destroy', 'quit'}:
                findings['method_calls'].add(method_name)
    
    return findings
