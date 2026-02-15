import sys, re, subprocess, math
from .utils import run_subprocess

def half_up(n):
    return int(n + 0.5)

def simulate_guessing_game(student_path, entrypoint, case, timeout=5):
    """
    Simulate playing the guessing game with the student's program.
    
    The grader plays as the user who thought of a secret number.
    Student's program guesses, grader responds with <, >, or =.
    
    Args:
        student_path: Directory containing student code
        entrypoint: Python file to run
        case: Test case dict with lower, upper, secret, cheat settings
        timeout: Max seconds to run
    
    Returns:
        {
            'found_number': bool,
            'num_guesses': int,
            'used_binary_search': bool,
            'detected_cheating': bool,
            'guesses': [list of guesses],
            'timeout': bool,
            'error': str or None
        }
    """
    lower = case['lower']
    upper = case['upper']
    secret = case['secret']
    should_cheat = case.get('cheat', False)
    cheat_after = case.get('cheat_after', 999)
    
    try:
        # Start student's program
        proc = subprocess.Popen(
            [sys.executable, '-I', entrypoint],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=student_path,
            bufsize=0  # Unbuffered
        )
        
        # Send initial bounds
        proc.stdin.write(f"{lower}\n")
        proc.stdin.flush()
        proc.stdin.write(f"{upper}\n")
        proc.stdin.flush()
        
        guesses = []
        found = False
        detected_cheating = False
        output_lines = []
        
        max_guesses = 100  # Safety limit
        
        while len(guesses) < max_guesses:
            try:
                # Read next line from program
                line = proc.stdout.readline()
                if not line:
                    break  # Program ended
                
                output_lines.append(line)
                line_lower = line.lower()
                
                # Check for cheating detection
                if 'cheat' in line_lower and 'out of guesses' in line_lower:
                    detected_cheating = True
                    break
                
                # Check for victory message
                if 'hooray' in line_lower or "i've got it" in line_lower or 'got it' in line_lower:
                    found = True
                    break
                
                # Look for guess pattern: "Your number is X" or "X Y" (showing range)
                # Match patterns like "0 10" or "Your number is 5"
                numbers = re.findall(r'\b(\d+)\b', line)
                
                if len(numbers) >= 2:
                    # Pattern: "lower upper" then "Your number is guess"
                    # The guess is likely the last number or a computed midpoint
                    # Look for explicit "your number is X" first
                    guess_match = re.search(r'(?:your number is|number is)\s*(\d+)', line_lower)
                    if guess_match:
                        guess = int(guess_match.group(1))
                    else:
                        # Might be showing range - wait for next line with actual guess
                        continue
                elif len(numbers) == 1:
                    guess = int(numbers[0])
                else:
                    continue  # No guess found yet
                
                # Valid guess found
                guesses.append(guess)
                
                # Determine correct response
                if guess == secret:
                    response = '='
                    # Don't send response - program should recognize it won
                    # But read any remaining output
                    try:
                        final_line = proc.stdout.readline()
                        if 'hooray' in final_line.lower() or 'got it' in final_line.lower():
                            found = True
                    except:
                        pass
                    break
                elif guess < secret:
                    response = '>'  # Number is greater than guess
                else:
                    response = '<'  # Number is less than guess
                
                # Optionally inject cheating
                if should_cheat and len(guesses) >= cheat_after:
                    # Give contradictory hint (flip the response)
                    if response == '<':
                        response = '>'
                    elif response == '>':
                        response = '<'
                
                # Send response
                proc.stdin.write(f"{response}\n")
                proc.stdin.flush()
                
            except subprocess.TimeoutExpired:
                proc.kill()
                return {
                    'found_number': False,
                    'num_guesses': len(guesses),
                    'used_binary_search': False,
                    'detected_cheating': False,
                    'guesses': guesses,
                    'timeout': True,
                    'error': 'Program timed out'
                }
        
        # Clean up
        try:
            proc.terminate()
            proc.wait(timeout=1)
        except:
            proc.kill()
        
        # Verify binary search strategy
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
    """
    Verify that guesses follow binary search strategy.
    Each guess should be at or near the midpoint of the current range.
    """
    if len(guesses) == 0:
        return False
    
    current_lower = lower
    current_upper = upper
    
    for guess in guesses:
        # Calculate expected midpoint
        expected = (current_lower + current_upper) // 2
        
        # Allow off-by-one due to rounding differences
        if abs(guess - expected) > 1:
            return False
        
        # Update range based on where guess was relative to secret
        if guess < secret:
            current_lower = guess + 1
        elif guess > secret:
            current_upper = guess - 1
        else:
            # Found it - this is fine
            break
    
    return True

def grade_guessing_game(cfg, student_path):
    """
    Grade ex03 - Computer guessing game with cheating detection.
    
    The student's program:
    - Takes lower and upper bounds as input
    - Guesses numbers using binary search
    - Reads user feedback (<, >, =)
    - Finds the number in optimal time
    - Detects if user gives contradictory hints (cheating)
    """
    
    ex_id = cfg.get('exercise_id')
    entrypoint = cfg.get('entrypoint')
    
    # Define test cases
    test_cases = [
        {
            'name': 'simple_range',
            'lower': 0,
            'upper': 10,
            'secret': 5,
            'max_guesses': 4,  # ceil(log2(11))
            'cheat': False
        },
        {
            'name': 'larger_range',
            'lower': 0,
            'upper': 50,
            'secret': 25,
            'max_guesses': 6,  # ceil(log2(51))
            'cheat': False
        },
        {
            'name': 'edge_lower',
            'lower': 0,
            'upper': 50,
            'secret': 1,
            'max_guesses': 6,
            'cheat': False
        },
        {
            'name': 'edge_upper',
            'lower': 0,
            'upper': 50,
            'secret': 49,
            'max_guesses': 6,
            'cheat': False
        },
        {
            'name': 'cheating_detection',
            'lower': 0,
            'upper': 10,
            'secret': 5,
            'max_guesses': 4,
            'cheat': True,
            'cheat_after': 3  # Give wrong hint on 3rd guess
        }
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
        result = simulate_guessing_game(student_path, entrypoint, case)
        
        if result['timeout']:
            notes.append(f"Case '{case['name']}': Program timed out")
            continue
        
        if result['error']:
            notes.append(f"Case '{case['name']}': Error - {result['error']}")
            continue
        
        if case.get('cheat'):
            # Test cheating detection
            if result['detected_cheating']:
                tasks[2]['earned'] += points_per_cheat
            else:
                notes.append(
                    f"Case '{case['name']}': Failed to detect cheating "
                    f"(contradictory hints after guess {case['cheat_after']})"
                )
        else:
            # Test correct guessing
            if not result['found_number']:
                notes.append(
                    f"Case '{case['name']}': Never found the number {case['secret']} "
                    f"(made {result['num_guesses']} guesses: {result['guesses']})"
                )
            else:
                # Award correctness points
                tasks[0]['earned'] += points_per_honest
                
                # Check optimality
                if result['num_guesses'] > case['max_guesses']:
                    notes.append(
                        f"Case '{case['name']}': Found it but took {result['num_guesses']} guesses, "
                        f"optimal is {case['max_guesses']} (binary search)"
                    )
                elif not result['used_binary_search']:
                    notes.append(
                        f"Case '{case['name']}': Found it but didn't use binary search "
                        f"(guesses weren't at midpoint: {result['guesses']})"
                    )
                else:
                    # Fully optimal
                    tasks[1]['earned'] += points_per_optimal
    
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

def sys_exe():
    return sys.executable
