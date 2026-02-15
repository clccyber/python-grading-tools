import sys, os, tempfile, shutil
from pathlib import Path
from .utils import run_subprocess

def half_up(n):
    return int(n + 0.5)

def grade_file_io(cfg, student_path):
    """
    Grade exercises that read from and write to files OR read from files and print to stdout.
    
    Supports three modes:
    1. Command-line arguments: python script.py input.txt output.txt [other args]
    2. Interactive prompts: prompts for filenames via stdin
    3. File input + stdout: reads file, prints to stdout
    
    Config structure:
    file_io_tests:
      - name: test_case_name
        mode: cmdline | interactive
        input_files:
          filename.txt: "file contents"
        cmdline_args: [arg1, arg2, ...]  # For cmdline mode
        stdin: "filename1\nfilename2\n"   # For interactive mode
        output_files:                     # For file output
          outfile.txt: "expected contents"
        expected_stdout: "expected stdout" # For stdout output
    """
    
    ex_id = cfg.get('exercise_id')
    entrypoint = cfg.get('entrypoint')
    test_cases = cfg.get('file_io_tests', [])
    
    if not test_cases:
        raise ValueError(f'No file_io_tests defined for {ex_id}')
    
    total_correctness = 80
    total_output_check = 20
    
    tasks = [
        {'name': 'file_correctness', 'max': total_correctness, 'earned': 0, 'status': 'fail'},
        {'name': 'output_format', 'max': total_output_check, 'earned': 0, 'status': 'fail'},
    ]
    
    notes = []
    points_per_case = total_correctness / len(test_cases)
    
    for case in test_cases:
        case_name = case.get('name', 'unnamed')
        mode = case.get('mode', 'interactive')  # cmdline or interactive
        input_files = case.get('input_files', {})
        output_files = case.get('output_files', {})
        cmdline_args = case.get('cmdline_args', [])
        stdin_text = case.get('stdin', '')
        
        # Create temporary directory for this test
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # Copy student script to temp directory
            student_script = Path(student_path) / entrypoint
            if not student_script.exists():
                notes.append(f"Case '{case_name}': {entrypoint} not found")
                continue
            
            temp_script = temp_path / entrypoint
            shutil.copy2(student_script, temp_script)
            
            # Create input files
            for filename, content in input_files.items():
                input_file = temp_path / filename
                input_file.write_text(content, encoding='utf-8')
            
            # Run student program
            if mode == 'cmdline':
                # Command-line arguments mode
                cmd = [sys.executable, str(temp_script)] + cmdline_args
                res = run_subprocess(cmd, cwd=str(temp_path), timeout=cfg.get('timeout_seconds', 5))
            else:
                # Interactive mode (prompts for filenames)
                cmd = [sys.executable, str(temp_script)]
                res = run_subprocess(cmd, input_text=stdin_text, cwd=str(temp_path), 
                                   timeout=cfg.get('timeout_seconds', 5))
            
            if res['timeout']:
                notes.append(
                    f"Case '{case_name}': Timeout after {res['elapsed']:.1f}s - "
                    f"program likely has an infinite loop or is waiting for input"
                )
                continue
            
            if res['returncode'] != 0:
                notes.append(
                    f"Case '{case_name}': Program exited with error code {res['returncode']}"
                )
                if res['stderr']:
                    notes.append(f"  Error: {res['stderr'][:200]}")
                continue
            
            # Check output files OR stdout
            expected_stdout = case.get('expected_stdout')
            
            if expected_stdout:
                # Check stdout output
                actual_stdout = res['stdout'].strip()
                expected_lines = expected_stdout.strip().splitlines()
                actual_lines = actual_stdout.splitlines()
                
                if len(actual_lines) != len(expected_lines):
                    notes.append(
                        f"Case '{case_name}': Output has {len(actual_lines)} lines, "
                        f"expected {len(expected_lines)} lines"
                    )
                    all_correct = False
                    continue
                
                # Compare line by line
                mismatches = []
                for i, (actual_line, expected_line) in enumerate(zip(actual_lines, expected_lines), 1):
                    actual_normalized = ' '.join(actual_line.split())
                    expected_normalized = ' '.join(expected_line.split())
                    
                    if actual_normalized != expected_normalized:
                        mismatches.append(
                            f"  Line {i}: expected '{expected_line}', got '{actual_line}'"
                        )
                
                if mismatches:
                    notes.append(f"Case '{case_name}': Output mismatch:")
                    notes.extend(mismatches[:3])
                    if len(mismatches) > 3:
                        notes.append(f"  ... and {len(mismatches) - 3} more differences")
                    all_correct = False
                    continue
            
            # Check output files
            all_correct = True
            for filename, expected_content in output_files.items():
                output_file = temp_path / filename
                
                if not output_file.exists():
                    notes.append(f"Case '{case_name}': Output file '{filename}' was not created")
                    all_correct = False
                    continue
                
                try:
                    actual_content = output_file.read_text(encoding='utf-8')
                except Exception as e:
                    notes.append(f"Case '{case_name}': Could not read '{filename}': {e}")
                    all_correct = False
                    continue
                
                # Normalize line endings for comparison
                actual_lines = actual_content.strip().splitlines()
                expected_lines = expected_content.strip().splitlines()
                
                if len(actual_lines) != len(expected_lines):
                    notes.append(
                        f"Case '{case_name}': File '{filename}' has {len(actual_lines)} lines, "
                        f"expected {len(expected_lines)} lines"
                    )
                    all_correct = False
                    continue
                
                # Compare line by line
                mismatches = []
                for i, (actual_line, expected_line) in enumerate(zip(actual_lines, expected_lines), 1):
                    # Normalize whitespace
                    actual_normalized = ' '.join(actual_line.split())
                    expected_normalized = ' '.join(expected_line.split())
                    
                    if actual_normalized != expected_normalized:
                        mismatches.append(
                            f"  Line {i}: expected '{expected_line}', got '{actual_line}'"
                        )
                
                if mismatches:
                    notes.append(f"Case '{case_name}': File '{filename}' content mismatch:")
                    notes.extend(mismatches[:3])  # Show first 3 mismatches
                    if len(mismatches) > 3:
                        notes.append(f"  ... and {len(mismatches) - 3} more differences")
                    all_correct = False
            
            # Award points if all files correct
            if all_correct:
                tasks[0]['earned'] += points_per_case
                tasks[1]['earned'] += total_output_check / len(test_cases)
    
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
        'formatting_issues': {}
    }
