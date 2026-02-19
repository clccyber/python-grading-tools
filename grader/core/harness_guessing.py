import sys, re, subprocess, math
import time

def half_up(n):
    return int(n + 0.5)

def simulate_guessing_game(student_path, entrypoint, case, timeout=10):
    """
    Simpler approach: Use expect-style interaction.
    """
    lower = case['lower']
    upper = case['upper']
    secret = case['secret']
    should_cheat = case.get('cheat', False)
    cheat_after = case.get('cheat_after', 999)
    
    try:
        # Use pexpect if available, otherwise fall back
        try:
            import pexpect
            
            proc = pexpect.spawn(
                sys.executable,
                ['-u', entrypoint],
                cwd=student_path,
                timeout=timeout,
                encoding='utf-8'
            )
            
            # Wait for prompts and respond
            proc.expect('smaller', timeout=2)
            proc.sendline(str(lower))
            
            proc.expect('larger', timeout=2)
            proc.sendline(str(upper))
            
            guesses = []
            found = False
            detected_cheating = False
            
            while len(guesses) < 100:
                try:
                    # Read until we see a guess or game ends
                    index = proc.expect([
                        r'Your number is (\d+)',
                        r'your number is (\d+)',
                        r'Hooray',
                        r'hooray',
                        r'cheat',
                        pexpect.EOF,
                        pexpect.TIMEOUT
                    ], timeout=2)
                    
                    if index in [0, 1]:  # Found guess
                        guess = int(proc.match.group(1))
                        if guess not in guesses:
                            guesses.append(guess)
                            
                            if guess == secret:
                                found = True
                                break
                            elif guess < secret:
                                response = '>'
                            else:
                                response = '<'
                            
                            if should_cheat and len(guesses) >= cheat_after:
                                response = '<' if response == '>' else '>'
                            
                            proc.sendline(response)
                    
                    elif index in [2, 3]:  # Victory
                        found = True
                        break
                    
                    elif index == 4:  # Cheating detection
                        detected_cheating = True
                        break
                    
                    elif index in [5, 6]:  # EOF or timeout
                        break
                        
                except pexpect.TIMEOUT:
                    break
                except pexpect.EOF:
                    break
            
            proc.close()
            used_binary_search = check_binary_search(guesses, lower, upper, secret)
            
            return {
                'found_number': found,
                'num_guesses': len(guesses),
                'used_binary_search': used_binary_search,
                'detected_cheating': detected_cheating,
                'guesses': guesses,
                'timeout': False,
                'error': None
            }
            
        except ImportError:
            # pexpect not available, use manual approach
            return simulate_with_subprocess(student_path, entrypoint, case, timeout)
            
    except Exception as e:
        return {
            'found_number': False,
            'num_guesses': 0,
            'used_binary_search': False,
            'detected_cheating': False,
            'guesses': [],
            'timeout': False,
            'error': str(e)
        }

def simulate_with_subprocess(student_path, entrypoint, case, timeout):
    """Fallback without pexpect - simpler line-based approach."""
    lower = case['lower']
    upper = case['upper']
    secret = case['secret']
    should_cheat = case.get('cheat', False)
    cheat_after = case.get('cheat_after', 999)
    
    try:
        proc = subprocess.Popen(
            [sys.executable, '-u', entrypoint],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,  # Combine streams
            text=True,
            cwd=student_path
        )
        
        # Immediately send both bounds (they'll be buffered)
        proc.stdin.write(f"{lower}\n{upper}\n")
        proc.stdin.flush()
        
        guesses = []
        found = False
        detected_cheating = False
        start_time = time.time()
        
        while len(guesses) < 100:
            if time.time() - start_time > timeout:
                proc.kill()
                return {
                    'found_number': False,
                    'num_guesses': len(guesses),
                    'used_binary_search': False,
                    'detected_cheating': False,
                    'guesses': guesses,
                    'timeout': True,
                    'error': 'Timeout'
                }
            
            try:
                line = proc.stdout.readline()
                if not line:
                    break
                
                line_lower = line.lower()
                
                # Check for victory
                if 'hooray' in line_lower or 'got it' in line_lower:
                    found = True
                    break
                
                # Check for cheating
                if 'cheat' in line_lower:
                    detected_cheating = True
                    break
                
                # Extract guess
                match = re.search(r'your number is\s*(\d+)', line_lower)
                if match:
                    guess = int(match.group(1))
                    if guess not in guesses:
                        guesses.append(guess)
                        
                        if guess == secret:
                            found = True
                            break
                        elif guess < secret:
                            response = '>'
                        else:
                            response = '<'
                        
                        if should_cheat and len(guesses) >= cheat_after:
                            response = '<' if response == '>' else '>'
                        
                        proc.stdin.write(f"{response}\n")
                        proc.stdin.flush()
                        
            except:
                break
        
        proc.kill()
        used_binary_search = check_binary_search(guesses, lower, upper, secret)
        
        return {
            'found_number': found,
            'num_guesses': len(guesses),
            'used_binary_search': used_binary_search,
            'detected_cheating': detected_cheating,
            'guesses': guesses,
            'timeout': False,
            'error': None
        }
        
    except Exception as e:
        try:
            proc.kill()
        except:
            pass
        return {
            'found_number': False,
            'num_guesses': 0,
            'used_binary_search': False,
            'detected_cheating': False,
            'guesses': [],
            'timeout': False,
            'error': str(e)
        }

def check_binary_search(guesses, lower, upper, secret):
    if len(guesses) == 0:
        return False
    
    current_lower = lower
    current_upper = upper
    
    for guess in guesses:
        expected = (current_lower + current_upper) // 2
        if abs(guess - expected) > 1:
            return False
        
        if guess < secret:
            current_lower = guess + 1
        elif guess > secret:
            current_upper = guess - 1
        else:
            break
    
    return True

def grade_guessing_game(cfg, student_path):
    ex_id = cfg.get('exercise_id')
    entrypoint = cfg.get('entrypoint')
    timeout = cfg.get('timeout_seconds', 10)
    
    test_cases = [
        {'name': 'simple_range', 'lower': 0, 'upper': 10, 'secret': 5, 'max_guesses': 4, 'cheat': False},
        {'name': 'larger_range', 'lower': 0, 'upper': 50, 'secret': 25, 'max_guesses': 6, 'cheat': False},
        {'name': 'edge_lower', 'lower': 0, 'upper': 50, 'secret': 1, 'max_guesses': 6, 'cheat': False},
        {'name': 'edge_upper', 'lower': 0, 'upper': 50, 'secret': 49, 'max_guesses': 6, 'cheat': False},
        {'name': 'cheating_detection', 'lower': 0, 'upper': 10, 'secret': 7, 'max_guesses': 4, 'cheat': True, 'cheat_after': 3}
    ]
    
    total_correctness = 70
    total_optimality = 10
    total_cheating = 20
    
    honest_cases = [c for c in test_cases if not c.get('cheat')]
    cheat_cases = [c for c in test_cases if c.get('cheat')]
    
    points_per_honest = total_correctness / len(honest_cases)
    points_per_optimal = total_optimality / len(honest_cases)
    points_per_cheat = total_cheating / len(cheat_cases) if cheat_cases else 0
    
    tasks = [
        {'name': 'finds_number', 'max': total_correctness, 'earned': 0, 'status': 'fail'},
        {'name': 'optimal_guesses', 'max': total_optimality, 'earned': 0, 'status': 'fail'},
        {'name': 'detects_cheating', 'max': total_cheating, 'earned': 0, 'status': 'fail'},
    ]
    
    notes = []
    
    for case in test_cases:
        result = simulate_guessing_game(student_path, entrypoint, case, timeout=timeout)
        
        if result['timeout']:
            notes.append(f"Case '{case['name']}': Timed out")
            continue
        
        if result['error']:
            notes.append(f"Case '{case['name']}': {result['error']}")
            continue
        
        if case.get('cheat'):
            if result['detected_cheating']:
                tasks[2]['earned'] += points_per_cheat
            else:
                notes.append(f"Case '{case['name']}': Failed to detect cheating")
        else:
            if not result['found_number']:
                notes.append(f"Case '{case['name']}': Never found {case['secret']} (guesses: {result['guesses']})")
            else:
                tasks[0]['earned'] += points_per_honest
                
                if result['num_guesses'] > case['max_guesses']:
                    notes.append(f"Case '{case['name']}': Took {result['num_guesses']} guesses (optimal: {case['max_guesses']})")
                elif not result['used_binary_search']:
                    notes.append(f"Case '{case['name']}': Didn't use binary search (guesses: {result['guesses']})")
                else:
                    tasks[1]['earned'] += points_per_optimal
    
    for task in tasks:
        task['earned'] = min(task['max'], task['earned'])
        task['status'] = 'pass' if task['earned'] == task['max'] else ('partial' if task['earned']>0 else 'fail')
    
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

def sys_exe():
    return sys.executable
