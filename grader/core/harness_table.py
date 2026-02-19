import sys, re
from .utils import run_subprocess
from .compare import isclose, normalize_text, find_numbers_in_line

def half_up(n):
    return int(n + 0.5)

def count_decimals(num_text):
    """Count decimal places in a number string."""
    if '.' not in num_text:
        return 0
    return len(num_text.split('.')[1])

def extract_row_values(line, num_columns):
    """
    Extract numeric values from a table row.
    Returns list of {'value': float, 'text': str} dicts, or None if incomplete.
    """
    # Skip lines that are clearly separators or headers (no digits)
    if not any(c.isdigit() for c in line):
        return None
    
    # Skip lines that are mostly dashes (separator lines)
    if line.count('-') > len(line) / 2:
        return None
    
    numbers = find_numbers_in_line(line)
    
    if len(numbers) < num_columns:
        return None  # Incomplete or header row
    
    result = []
    for i in range(num_columns):
        num_text, num_val = numbers[i]
        result.append({
            'value': num_val,
            'text': num_text
        })
    return result

def check_table_structure(lines, checks):
    """
    Check optional structural elements (headers, separators).
    Returns (points_earned, notes).
    Non-fragile: missing structure reduces points but doesn't fail.
    """
    if not checks:
        return (0, [])  # No checks defined
    
    notes = []
    earned = 0
    
    for check in checks:
        check_type = check['type']
        pattern = check.get('pattern', '')
        points = check.get('points', 5)
        
        if check_type == 'header_present':
            found = any(re.search(pattern, line, re.I) for line in lines[:5])
            if found:
                earned += points
            else:
                notes.append(f"Table header pattern '{pattern}' not found")
                
        elif check_type == 'separator_line':
            found = any(re.match(pattern, line) for line in lines[:10])
            if found:
                earned += points
            else:
                notes.append(f"Table separator line not found")
    
    return (earned, notes)

def compute_expected_table_row(ex_id, inputs, row_num, columns):
    """
    Calculate expected values for a single table row.
    Encodes the loop logic students should implement.
    
    Args:
        ex_id: Exercise identifier
        inputs: List of input values (from stdin)
        row_num: Row number (1-indexed)
        columns: Column specifications
    
    Returns:
        List of expected values for this row
    """
    def f(i, cast=float, default=0):
        try:
            return cast(inputs[i])
        except:
            return default
    
    if ex_id == 'chapter3/ex07':
        # Salary schedule
        starting = f(0, float)
        percent_increase = f(1, float) / 100.0
        num_years = f(2, int)
        
        year = row_num
        salary = starting * ((1 + percent_increase) ** (year - 1))
        
        return [year, salary]
    
    if ex_id == 'chapter3/ex10':
        # Payment schedule - stateful, needs to simulate from beginning
        purchase = f(0, float)
        down_payment = purchase * 0.10
        balance = purchase - down_payment
        monthly_payment = purchase * 0.05
        annual_rate = 0.12
        
        # Simulate up to the requested row
        for month in range(1, row_num + 1):
            starting_balance = balance
            interest = balance * (annual_rate / 12)
            principal = monthly_payment - interest
            ending_balance = balance - principal
            
            if month == row_num:
                return [month, starting_balance, interest, principal, monthly_payment, ending_balance]
            
            balance = ending_balance
        
        return []
    
    return []

def grade_table(cfg, student_path):
    """
    Grade exercises that output tables with multiple rows of data.
    
    Grading breakdown:
    - Row values: Numeric correctness of each cell
    - Formatting: Decimal places, money formatting
    - Structure: Optional headers/separators (non-fragile)
    """
    tp = cfg.get('tolerances', {})
    num_tol = tp.get('numeric', {'rel_tol':1e-3, 'abs_tol':1e-2})
    text_tol = tp.get('text', {})
    ex_id = cfg.get('exercise_id')
    
    table_cfg = cfg.get('table_config', {})
    expected_rows = table_cfg.get('expected_rows', 10)
    skip_lines = table_cfg.get('skip_header_lines', 0)
    columns = table_cfg.get('columns', [])
    formatting_checks = table_cfg.get('formatting_checks', [])
    
    # Calculate max points for structure checks
    total_structure = sum(check.get('points', 5) for check in formatting_checks)
    total_numeric = 60
    total_format = 20
    
    if total_structure == 0:
        # No structure checks - give those points to numeric
        total_numeric += 20
    
    tasks = [
        {'name': 'row_values', 'max': total_numeric, 'earned': 0, 'status': 'fail'},
        {'name': 'formatting', 'max': total_format, 'earned': 0, 'status': 'fail'},
    ]
    
    if total_structure > 0:
        tasks.append({'name': 'table_structure', 'max': total_structure, 'earned': 0, 'status': 'fail'})
    
    notes = []
    formatting_issues = {}
    
    for case in cfg.get('io_tests', []):
        case_name = case.get('name', 'case')
        formatting_issues[case_name] = []
        
        res = run_subprocess([
            sys_exe(), '-I', cfg.get('entrypoint')
        ], input_text=case.get('stdin',''), cwd=student_path, timeout=cfg.get('timeout_seconds',2))
        
        if res['timeout']:
            notes.append(
                f"Timeout in case '{case_name}' after {res['elapsed']:.1f}s - "
                f"program likely has an infinite loop or is waiting for input"
            )
            continue
        
        output = res['stdout']
        output_lines = output.strip().split('\n')
        
        # Check optional table structure
        if formatting_checks:
            struct_earned, struct_notes = check_table_structure(output_lines, formatting_checks)
            tasks[-1]['earned'] += struct_earned
            notes.extend([f"Case '{case_name}': {n}" for n in struct_notes])
        
        # Extract data rows
        data_lines = output_lines[skip_lines:] if skip_lines < len(output_lines) else output_lines
        
        # Parse rows
        rows_found = []
        for line_num, line in enumerate(data_lines, start=skip_lines+1):
            row_values = extract_row_values(line, len(columns))
            if row_values:
                rows_found.append({'line': line_num, 'values': row_values, 'text': line})
                rows_found.append({'line': line_num, 'values': row_values, 'text': line})
        
        # Check row count
        if len(rows_found) != expected_rows:
            notes.append(
                f"Case '{case_name}': expected {expected_rows} data rows, found {len(rows_found)}"
            )
        
        # Get inputs
        inputs = [ln.strip() for ln in case.get('stdin','').splitlines() if ln.strip()]
        
        # Points per cell
        total_cells = expected_rows * len(columns)
        points_per_cell_numeric = total_numeric / total_cells
        points_per_cell_format = total_format / total_cells
        
        # Check each row
        for row_idx, row_data in enumerate(rows_found):
            row_num = row_idx + 1  # 1-indexed for display
            actual_row = row_data['values']
            
            # Skip if we've exceeded expected rows
            if row_num > expected_rows:
                break
            
            # Get expected values for this row
            expected_values = compute_expected_table_row(ex_id, inputs, row_num, columns)
            
            if not expected_values:
                notes.append(f"Case '{case_name}': no expected values for row {row_num}")
                continue
            
            # Check each column
            for col_idx, col_spec in enumerate(columns):
                col_name = col_spec.get('name', f'column{col_idx}')
                
                if col_idx >= len(actual_row) or col_idx >= len(expected_values):
                    notes.append(f"Case '{case_name}', row {row_num}: missing {col_name}")
                    continue
                
                actual_val = actual_row[col_idx]['value']
                expected_val = expected_values[col_idx]
                actual_text = actual_row[col_idx]['text']
                
                # Numeric correctness
                if isclose(actual_val, expected_val, 
                          rel_tol=num_tol.get('rel_tol', 1e-3), 
                          abs_tol=num_tol.get('abs_tol', 1e-2)):
                    tasks[0]['earned'] += points_per_cell_numeric
                else:
                    notes.append(
                        f"Case '{case_name}', row {row_num}, {col_name}: "
                        f"expected ≈ {expected_val:.6g}, found {actual_val}"
                    )
                
                # Formatting check
                fmt_spec = col_spec.get('format', {})
                if 'decimals' in fmt_spec:
                    required_decimals = fmt_spec['decimals']
                    actual_decimals = count_decimals(actual_text)
                    
                    if actual_decimals == required_decimals:
                        tasks[1]['earned'] += points_per_cell_format
                    else:
                        formatting_issues[case_name].append({
                            'rule_id': 'decimal_places',
                            'description': f'Row {row_num}, {col_name} should have {required_decimals} decimal places',
                            'pattern': f'X.{"Y"*required_decimals}',
                            'line': row_data['line'],
                            'actual': actual_text,
                            'tip': f'Use format spec {{:.{required_decimals}f}} or round(..., {required_decimals})'
                        })
    
    def finalize(task, earned):
        task['earned'] = min(task['max'], earned)
        task['status'] = 'pass' if task['earned'] == task['max'] else ('partial' if task['earned']>0 else 'fail')
    
    for task in tasks:
        finalize(task, task['earned'])
    
    raw_earned = sum(t['earned'] for t in tasks)
    raw_total = sum(t['max'] for t in tasks)
    pct = (raw_earned / raw_total) * 100 if raw_total>0 else 0.0
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
        'formatting_issues': formatting_issues
    }

def sys_exe():
    return sys.executable
