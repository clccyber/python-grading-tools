import sys, os, tempfile, shutil
from pathlib import Path
from .utils import run_subprocess

def half_up(n):
    return int(n + 0.5)

def grade_file_io(cfg, student_path):
    """
    Grade exercises that read from and write to files.
    
    Supports:
    1. Command-line arguments mode
    2. Interactive prompts mode
    3. File input + stdout mode
    4. Encrypt/decrypt pipeline mode (NEW)
    """
    
    ex_id = cfg.get('exercise_id')
    entrypoint = cfg.get('entrypoint')
    decrypt_script = cfg.get('decrypt_script')  # Optional: signals pipeline mode
    test_cases = cfg.get('file_io_tests', [])
    
    if not test_cases:
        raise ValueError(f'No file_io_tests defined for {ex_id}')
    
    # Determine if this is a pipeline test
    is_pipeline = decrypt_script is not None
    
    if is_pipeline:
        return grade_pipeline(cfg, student_path, test_cases)
    else:
        return grade_single_file_io(cfg, student_path, test_cases)

def grade_pipeline(cfg, student_path, test_cases):
    """Grade encrypt/decrypt pipeline exercises."""
    ex_id = cfg.get('exercise_id')
    entrypoint = cfg.get('entrypoint')
    decrypt_script = cfg.get('decrypt_script')
    
    total_correctness = 70
    total_encryption_check = 10
    total_roundtrip = 20
    
    tasks = [
        {'name': 'roundtrip_correctness', 'max': total_roundtrip, 'earned': 0, 'status': 'fail'},
        {'name': 'encryption_works', 'max': total_encryption_check, 'earned': 0, 'status': 'fail'},
        {'name': 'decryption_works', 'max': total_correctness, 'earned': 0, 'status': 'fail'},
    ]
    
    notes = []
    points_per_case_roundtrip = total_roundtrip / len(test_cases)
    points_per_case_encrypt = total_encryption_check / len(test_cases)
    points_per_case_decrypt = total_correctness / len(test_cases)
    
    for case in test_cases:
        case_name = case.get('name', 'unnamed')
        input_files = case.get('input_files', {})
        
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # Copy both scripts
            encrypt_path = Path(student_path) / entrypoint
            if not encrypt_path.exists():
                notes.append(f"Case '{case_name}': {entrypoint} not found")
                continue
            shutil.copy2(encrypt_path, temp_path / entrypoint)
            
            decrypt_path = Path(student_path) / decrypt_script
            if not decrypt_path.exists():
                notes.append(f"Case '{case_name}': {decrypt_script} not found")
                continue
            shutil.copy2(decrypt_path, temp_path / decrypt_script)
            
            # Create input files
            original_content = None
            for filename, content in input_files.items():
                input_file = temp_path / filename
                input_file.write_text(content, encoding='utf-8')
                original_content = content
            
            # Run encryption
            encrypt_stdin = case.get('encrypt_stdin', '')
            res1 = run_subprocess(
                [sys.executable, entrypoint],
                input_text=encrypt_stdin,
                cwd=str(temp_path),
                timeout=cfg.get('timeout_seconds', 10)
            )
            
            if res1['timeout']:
                notes.append(f"Case '{case_name}': Encrypt timed out")
                continue
            
            if res1['returncode'] != 0:
                notes.append(f"Case '{case_name}': Encrypt failed with exit code {res1['returncode']}")
                if res1['stderr']:
                    notes.append(f"  Error: {res1['stderr'][:200]}")
                continue
            
            # Check encrypted file
            encrypted_filename = encrypt_stdin.strip().split('\n')[1] if len(encrypt_stdin.strip().split('\n')) > 1 else 'encrypted.txt'
            encrypted_file = temp_path / encrypted_filename
            
            if not encrypted_file.exists():
                notes.append(f"Case '{case_name}': Encrypted file '{encrypted_filename}' not created")
                continue
            
            encrypted_content = encrypted_file.read_text(encoding='utf-8')
            
            # Check encryption differs from input
            if case.get('check_encrypted_differs') and encrypted_content.strip() == original_content.strip():
                notes.append(f"Case '{case_name}': Encrypted file same as input (encryption failed)")
            else:
                tasks[1]['earned'] += points_per_case_encrypt
            
            # Run decryption
            decrypt_stdin = case.get('decrypt_stdin', '')
            res2 = run_subprocess(
                [sys.executable, decrypt_script],
                input_text=decrypt_stdin,
                cwd=str(temp_path),
                timeout=cfg.get('timeout_seconds', 10)
            )
            
            if res2['timeout']:
                notes.append(f"Case '{case_name}': Decrypt timed out")
                continue
            
            if res2['returncode'] != 0:
                notes.append(f"Case '{case_name}': Decrypt failed with exit code {res2['returncode']}")
                if res2['stderr']:
                    notes.append(f"  Error: {res2['stderr'][:200]}")
                continue
            
            tasks[2]['earned'] += points_per_case_decrypt
            
            # Check roundtrip
            output_filename = decrypt_stdin.strip().split('\n')[1] if len(decrypt_stdin.strip().split('\n')) > 1 else 'output.txt'
            output_file = temp_path / output_filename
            
            if not output_file.exists():
                notes.append(f"Case '{case_name}': Decrypted file '{output_filename}' not created")
                continue
            
            final_content = output_file.read_text(encoding='utf-8')
            expected = case.get('expected_roundtrip', original_content)
            
            if final_content.strip() == expected.strip():
                tasks[0]['earned'] += points_per_case_roundtrip
            else:
                notes.append(f"Case '{case_name}': Roundtrip failed - output doesn't match input")
                final_lines = final_content.strip().splitlines()
                expected_lines = expected.strip().splitlines()
                for i, (f, e) in enumerate(zip(final_lines, expected_lines), 1):
                    if f != e:
                        notes.append(f"  Line {i}: expected '{e[:50]}', got '{f[:50]}'")
                        break
    
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

def grade_single_file_io(cfg, student_path, test_cases):
    """Grade single file I/O exercises (original functionality)."""
    ex_id = cfg.get('exercise_id')
    entrypoint = cfg.get('entrypoint')
    
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
        mode = case.get('mode', 'interactive')
        input_files = case.get('input_files', {})
        output_files = case.get('output_files', {})
        cmdline_args = case.get('cmdline_args', [])
        stdin_text = case.get('stdin', '')
        
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # Copy student script
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
                cmd = [sys.executable, str(temp_script)] + cmdline_args
                res = run_subprocess(cmd, cwd=str(temp_path), timeout=cfg.get('timeout_seconds', 5))
            else:
                cmd = [sys.executable, str(temp_script)]
                res = run_subprocess(cmd, input_text=stdin_text, cwd=str(temp_path), 
                                   timeout=cfg.get('timeout_seconds', 5))
            
            if res['timeout']:
                notes.append(
                    f"Case '{case_name}': Timeout after {res['elapsed']:.1f}s"
                )
                continue
            
            if res['returncode'] != 0:
                notes.append(
                    f"Case '{case_name}': Program exited with error code {res['returncode']}"
                )
                if res['stderr']:
                    notes.append(f"  Error: {res['stderr'][:200]}")
                continue
            
            # Check stdout if expected
            expected_stdout = case.get('expected_stdout')
            
            if expected_stdout:
                actual_stdout = res['stdout'].strip()
                expected_lines = expected_stdout.strip().splitlines()
                actual_lines = actual_stdout.splitlines()
                
                if len(actual_lines) != len(expected_lines):
                    notes.append(
                        f"Case '{case_name}': Output has {len(actual_lines)} lines, "
                        f"expected {len(expected_lines)} lines"
                    )
                    continue
                
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
                    continue
            
            # Check output files
            all_correct = True
            for filename, expected_content in output_files.items():
                output_file = temp_path / filename
                
                if not output_file.exists():
                    notes.append(f"Case '{case_name}': Output file '{filename}' not created")
                    all_correct = False
                    continue
                
                try:
                    actual_content = output_file.read_text(encoding='utf-8')
                except Exception as e:
                    notes.append(f"Case '{case_name}': Could not read '{filename}': {e}")
                    all_correct = False
                    continue
                
                actual_lines = actual_content.strip().splitlines()
                expected_lines = expected_content.strip().splitlines()
                
                if len(actual_lines) != len(expected_lines):
                    notes.append(
                        f"Case '{case_name}': File '{filename}' has {len(actual_lines)} lines, "
                        f"expected {len(expected_lines)} lines"
                    )
                    all_correct = False
                    continue
                
                mismatches = []
                for i, (actual_line, expected_line) in enumerate(zip(actual_lines, expected_lines), 1):
                    actual_normalized = ' '.join(actual_line.split())
                    expected_normalized = ' '.join(expected_line.split())
                    
                    if actual_normalized != expected_normalized:
                        mismatches.append(
                            f"  Line {i}: expected '{expected_line}', got '{actual_line}'"
                        )
                
                if mismatches:
                    notes.append(f"Case '{case_name}': File '{filename}' content mismatch:")
                    notes.extend(mismatches[:3])
                    if len(mismatches) > 3:
                        notes.append(f"  ... and {len(mismatches) - 3} more differences")
                    all_correct = False
            
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
