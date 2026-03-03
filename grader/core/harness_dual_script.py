import sys
from .utils import run_subprocess

def half_up(n):
    return int(n + 0.5)

def grade_dual_script(cfg, student_path):
    """
    Grade exercises with two related scripts (e.g., decimal<->octal conversion).
    
    Tests each script independently and optionally verifies roundtrip.
    """
    ex_id = cfg.get('exercise_id')
    script1 = cfg.get('entrypoint')
    script2 = cfg.get('second_entrypoint')
    
    script1_tests = cfg.get('script1_tests', [])
    script2_tests = cfg.get('script2_tests', [])
    roundtrip_tests = cfg.get('roundtrip_tests', [])
    
    total_script1 = 40
    total_script2 = 40
    total_roundtrip = 20
    
    tasks = [
        {'name': f'{script1}_correctness', 'max': total_script1, 'earned': 0, 'status': 'fail'},
        {'name': f'{script2}_correctness', 'max': total_script2, 'earned': 0, 'status': 'fail'},
        {'name': 'roundtrip', 'max': total_roundtrip, 'earned': 0, 'status': 'fail'},
    ]
    
    notes = []
    
    # Test script 1
    if script1_tests:
        points_per_test = total_script1 / len(script1_tests)
        for test in script1_tests:
            test_name = test.get('name', 'unnamed')
            stdin = test.get('stdin', '')
            expected = test.get('expected_output', '')
            
            res = run_subprocess(
                [sys.executable, script1],
                input_text=stdin + '\n',
                cwd=student_path,
                timeout=cfg.get('timeout_seconds', 5)
            )
            
            if res['timeout']:
                notes.append(f"{script1} test '{test_name}': timed out")
                continue
            
            if res['returncode'] != 0:
                notes.append(f"{script1} test '{test_name}': exited with error")
                continue
            
            output = res['stdout'].strip()
            if expected in output:
                tasks[0]['earned'] += points_per_test
            else:
                notes.append(f"{script1} test '{test_name}': expected '{expected}' in output, got '{output}'")
    
    # Test script 2
    if script2_tests:
        points_per_test = total_script2 / len(script2_tests)
        for test in script2_tests:
            test_name = test.get('name', 'unnamed')
            stdin = test.get('stdin', '')
            expected = test.get('expected_output', '')
            
            res = run_subprocess(
                [sys.executable, script2],
                input_text=stdin + '\n',
                cwd=student_path,
                timeout=cfg.get('timeout_seconds', 5)
            )
            
            if res['timeout']:
                notes.append(f"{script2} test '{test_name}': timed out")
                continue
            
            if res['returncode'] != 0:
                notes.append(f"{script2} test '{test_name}': exited with error")
                continue
            
            output = res['stdout'].strip()
            if expected in output:
                tasks[1]['earned'] += points_per_test
            else:
                notes.append(f"{script2} test '{test_name}': expected '{expected}' in output, got '{output}'")
    
    # Test roundtrip
    if roundtrip_tests:
        points_per_test = total_roundtrip / len(roundtrip_tests)
        for test in roundtrip_tests:
            decimal_input = test.get('decimal_input', '')
            expected_octal = test.get('expected_octal', '')
            expected_decimal = test.get('expected_decimal', '')
            
            # Run decimal -> octal
            res1 = run_subprocess(
                [sys.executable, script1],
                input_text=decimal_input + '\n',
                cwd=student_path,
                timeout=cfg.get('timeout_seconds', 5)
            )
            
            if res1['timeout'] or res1['returncode'] != 0:
                notes.append(f"Roundtrip '{decimal_input}': {script1} failed")
                continue
            
            # Extract octal from output
            octal_output = res1['stdout'].strip()
            if expected_octal not in octal_output:
                notes.append(f"Roundtrip '{decimal_input}': {script1} didn't produce '{expected_octal}'")
                continue
            
            # Run octal -> decimal  
            res2 = run_subprocess(
                [sys.executable, script2],
                input_text=expected_octal + '\n',
                cwd=student_path,
                timeout=cfg.get('timeout_seconds', 5)
            )
            
            if res2['timeout'] or res2['returncode'] != 0:
                notes.append(f"Roundtrip '{decimal_input}': {script2} failed")
                continue
            
            decimal_output = res2['stdout'].strip()
            if expected_decimal in decimal_output:
                tasks[2]['earned'] += points_per_test
            else:
                notes.append(f"Roundtrip '{decimal_input}': final output '{decimal_output}' != original '{expected_decimal}'")
    
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
