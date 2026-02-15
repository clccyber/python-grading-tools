import sys, re, os, tempfile, shutil
from .utils import run_subprocess

def half_up(n):
    return int(n + 0.5)

def create_seeded_wrapper(student_path, entrypoint, seed):
    """
    Create a wrapper script that imports the student's code but seeds random first.
    
    This ensures dice rolls are deterministic for testing.
    Returns path to temporary wrapper script.
    """
    # Read the student's original code
    student_file = os.path.join(student_path, entrypoint)
    try:
        with open(student_file, 'r', encoding='utf-8') as f:
            student_code = f.read()
    except Exception as e:
        return None, f"Could not read {entrypoint}: {e}"
    
    # Create wrapper that seeds random before running student code
    wrapper_code = f"""# Auto-generated wrapper to seed random for testing
import random
random.seed({seed})

# Student code begins here:
{student_code}
"""
    
    # Write to temporary file in student directory
    wrapper_file = os.path.join(student_path, f'.grader_wrapper_{entrypoint}')
    try:
        with open(wrapper_file, 'w', encoding='utf-8') as f:
            f.write(wrapper_code)
        return wrapper_file, None
    except Exception as e:
        return None, f"Could not create wrapper: {e}"

def parse_lucky_sevens_output(output):
    """
    Parse the output of Lucky Sevens game.
    
    Expected format:
        "You are broke after X rolls."
        "You should have quit after Y rolls when you had $Z."
    
    Returns: {'rolls_to_broke': int, 'max_roll': int, 'max_money': float}
    """
    result = {
        'rolls_to_broke': None,
        'max_roll': None,
        'max_money': None
    }
    
    # Look for "broke after X rolls"
    broke_match = re.search(r'broke after (\d+) rolls?', output, re.I)
    if broke_match:
        result['rolls_to_broke'] = int(broke_match.group(1))
    
    # Look for "quit after X rolls when you had $Y"
    quit_match = re.search(r'quit after (\d+) rolls? when you had \$?(\d+(?:\.\d+)?)', output, re.I)
    if quit_match:
        result['max_roll'] = int(quit_match.group(1))
        result['max_money'] = float(quit_match.group(2))
    
    return result

def simulate_lucky_sevens(initial_money, seed):
    """
    Simulate the Lucky Sevens game with a seeded RNG to get expected results.
    
    Game rules:
    - Roll two dice
    - If sum == 7: win $4
    - Otherwise: lose $1
    
    Returns: {'rolls_to_broke': int, 'max_roll': int, 'max_money': int}
    """
    import random
    random.seed(seed)
    
    money = initial_money
    max_money = money
    max_roll = 0
    rolls = 0
    
    while money > 0:
        rolls += 1
        
        # Roll two dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        
        # Apply game rules
        if total == 7:
            money += 4
        else:
            money -= 1
        
        # Track maximum
        if money > max_money:
            max_money = money
            max_roll = rolls
    
    return {
        'rolls_to_broke': rolls,
        'max_roll': max_roll,
        'max_money': max_money
    }

def grade_lucky_sevens(cfg, student_path):
    """
    Grade ex11 - Lucky Sevens dice game.
    
    Uses seeded random number generator to make dice rolls deterministic.
    This allows us to verify the student's game logic produces expected results.
    """
    
    ex_id = cfg.get('exercise_id')
    entrypoint = cfg.get('entrypoint')
    
    # Test cases with different initial money and seeds
    test_cases = [
        {
            'name': 'small_pot',
            'initial_money': 10,
            'seed': 42
        },
        {
            'name': 'medium_pot',
            'initial_money': 50,
            'seed': 12345
        },
        {
            'name': 'large_pot',
            'initial_money': 100,
            'seed': 99999
        }
    ]
    
    total_simulation = 60  # Correct game simulation
    total_output = 40      # Correct output format
    
    tasks = [
        {'name': 'game_simulation', 'max': total_simulation, 'earned': 0, 'status': 'fail'},
        {'name': 'output_format', 'max': total_output, 'earned': 0, 'status': 'fail'},
    ]
    
    notes = []
    points_per_case_sim = total_simulation / len(test_cases)
    points_per_case_out = total_output / len(test_cases)
    
    for case in test_cases:
        case_name = case['name']
        initial = case['initial_money']
        seed = case['seed']
        
        # Create wrapper that seeds random
        wrapper_file, error = create_seeded_wrapper(student_path, entrypoint, seed)
        if error:
            notes.append(f"Case '{case_name}': {error}")
            continue
        
        try:
            # Run the wrapped student code
            res = run_subprocess(
                [sys.executable, '-I', os.path.basename(wrapper_file)],
                input_text=f"{initial}\n",
                cwd=student_path,
                timeout=10  # Dice games can take a while
            )
            
            if res['timeout']:
                notes.append(
                    f"Case '{case_name}': Timeout after {res['elapsed']:.1f}s - "
                    f"infinite loop or game never ends"
                )
                continue
            
            # Parse student output
            actual = parse_lucky_sevens_output(res['stdout'])
            
            # Simulate with same seed to get expected values
            expected = simulate_lucky_sevens(initial, seed)
            
            # Check simulation correctness
            sim_correct = True
            
            if actual['rolls_to_broke'] != expected['rolls_to_broke']:
                notes.append(
                    f"Case '{case_name}': Broke after {actual['rolls_to_broke']} rolls, "
                    f"expected {expected['rolls_to_broke']} rolls (with seed {seed})"
                )
                sim_correct = False
            
            if actual['max_money'] != expected['max_money']:
                notes.append(
                    f"Case '{case_name}': Max money ${actual['max_money']}, "
                    f"expected ${expected['max_money']}"
                )
                sim_correct = False
            
            if actual['max_roll'] != expected['max_roll']:
                notes.append(
                    f"Case '{case_name}': Max at roll {actual['max_roll']}, "
                    f"expected roll {expected['max_roll']}"
                )
                sim_correct = False
            
            if sim_correct:
                tasks[0]['earned'] += points_per_case_sim
            
            # Check output format
            output_correct = True
            
            if actual['rolls_to_broke'] is None:
                notes.append(f"Case '{case_name}': Missing 'broke after X rolls' message")
                output_correct = False
            
            if actual['max_money'] is None or actual['max_roll'] is None:
                notes.append(f"Case '{case_name}': Missing 'quit after X rolls when you had $Y' message")
                output_correct = False
            
            if output_correct:
                tasks[1]['earned'] += points_per_case_out
        
        finally:
            # Clean up wrapper file
            try:
                if wrapper_file and os.path.exists(wrapper_file):
                    os.remove(wrapper_file)
            except:
                pass
    
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
