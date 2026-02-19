
import math
from .utils import run_subprocess
from .compare import isclose, normalize_text, find_numbers_in_line

def half_up(n):
    return int(n + 0.5)

def compute_expected(ex_id, lines):
    def f(i, cast=float, default=0.0):
        try:
            return cast(lines[i])
        except Exception:
            return default
    
    # Chapter 1 exercises
    if ex_id == 'chapter1/ex02':
        width = f(0, float)
        height = f(1, float)
        return {'area': width * height}
    if ex_id == 'chapter1/ex03':
        base = f(0, float)
        height = f(1, float)
        return {'area': 0.5 * base * height}
    if ex_id == 'chapter1/ex04':
        radius = f(0, float)
        return {'area': 3.14 * radius * radius}
    if ex_id == 'chapter1/ex05':
        height = f(0, float)
        width = f(1, float)
        depth = f(2, float)
        return {'volume': height * width * depth}
    
    # Chapter 2 exercises
    if ex_id == 'chapter2/ex01':
        gross = f(0, float); deps = f(1, int)
        TAX_RATE = 0.20; STD = 10000.0; DEP = 3000.0
        taxable = gross - STD - DEP*deps
        return {'income tax': taxable * TAX_RATE}
    if ex_id == 'chapter2/ex02':
        a = f(0, float)
        return {'surface area': 6 * a * a}
    if ex_id == 'chapter2/ex03':
        new = f(0, int); old = f(1, int)
        return {'total cost': new * 3.00 + old * 2.00}
    if ex_id == 'chapter2/ex04':
        r = f(0, float)
        return {
            'diameter': 2*r,
            'circumference': 2*math.pi*r,
            'surface area': 4*math.pi*r*r,
            'volume': (4.0/3.0)*math.pi*r*r*r,
        }
    if ex_id == 'chapter2/ex05':
        m = f(0, float); v = f(1, float)
        return {'momentum': m*v}
    if ex_id == 'chapter2/ex06':
        m = f(0, float); v = f(1, float)
        return {'momentum': m*v, 'kinetic energy': 0.5*m*v*v}
    if ex_id == 'chapter2/ex07':
        y = f(0, int)
        return {'minutes': y * 365 * 24 * 60}
    if ex_id == 'chapter2/ex08':
        y = f(0, int)
        seconds = y * 365 * 24 * 60 * 60
        return {'meters': seconds * 3.0e8}
    if ex_id == 'chapter2/ex09':
        km = f(0, float)
        return {'nautical miles': km * (90*60)/10000}
    if ex_id == 'chapter2/ex10':
        wage = f(0, float); reg = f(1, float); ot = f(2, float)
        return {'total weekly pay': wage * reg + wage * 1.5 * ot}
    
    if ex_id == 'chapter3/ex04':
        # Bouncing ball total distance
        height = f(0, float)
        index = f(1, float)
        bounces = f(2, int)
        
        # Each loop iteration: fall down + bounce back up
        distance = 0
        for _ in range(bounces):
            distance += height      # Fall down from current height
            height = height * index # New height after bounce
            distance += height      # Bounce back up to new height
        
        return {'total distance': distance}   

    if ex_id == 'chapter3/ex05':
        # Population growth
        initial = f(0, int)
        rate = f(1, float)
        hours_for_rate = f(2, int)
        total_hours = f(3, int)
        # How many growth periods?
        periods = total_hours // hours_for_rate
        # Population after growth
        population = initial * (rate ** periods)
        return {'total population': population}
    
    if ex_id == 'chapter3/ex06':
        # Leibniz π approximation: π/4 = 1 - 1/3 + 1/5 - 1/7 + ...
        iterations = f(0, int)
        result = 0.0
        for i in range(iterations):
            term = 1.0 / (2 * i + 1)
            if i % 2 == 0:
                result += term
            else:
                result -= term
        pi_approx = result * 4
        return {'approximation of pi': pi_approx}
    
    if ex_id == 'chapter3/ex08':
        # GCD using Euclidean algorithm
        a = f(0, int)
        b = f(1, int)
        gcd = math.gcd(a, b)
        return {'greatest common divisor': gcd}
    
    if ex_id == 'chapter3/ex09':
        # Sum and average of numbers until blank line
        # lines contains all non-empty inputs
        numbers = [f(i, float) for i in range(len(lines))]
        if not numbers:
            return {'sum': 0.0, 'average': 0.0}
        total = sum(numbers)
        avg = total / len(numbers)
        return {'sum': total, 'average': avg}
    
    return {}

def grade_io(cfg, student_path):
    tp = cfg.get('tolerances', {})
    num_tol = tp.get('numeric', {'rel_tol':1e-3, 'abs_tol':1e-2})
    text_tol = tp.get('text', {})
    ex_id = cfg.get('exercise_id')

    total_numeric = 60
    total_labels = 20
    total_format = 20

    money_ex = ex_id in ('chapter2/ex03','chapter2/ex10')
    if not money_ex:
        total_numeric += total_format
        total_format = 0

    tasks = [
        {'name':'numeric_correctness','max': total_numeric,'earned':0,'status':'fail'},
        {'name':'label_and_presence','max': total_labels,'earned':0,'status':'fail'},
    ]
    if money_ex:
        tasks.append({'name':'formatting_money','max': total_format,'earned':0,'status':'fail'})

    fmt_cfg = cfg.get('formatting', {}).get('money', {})
    penalty_per_extra = fmt_cfg.get('penalty_per_extra_decimal', 2)
    fmt_min_points = fmt_cfg.get('min_points', 0)
    fmt_tips = fmt_cfg.get('tips', [ 'Use f-strings with {:.2f} or round(value, 2) before printing'
    ])

    notes = []
    formatting_issues = {}
    earned_num = earned_lab = earned_fmt = 0

    for case in cfg.get('io_tests', []):
        case_name = case.get('name','case')
        formatting_issues[case_name] = []
        res = run_subprocess([ sys_exe(), '-I', cfg.get('entrypoint')
        ], input_text=case.get('stdin',''), cwd=student_path, timeout=cfg.get('timeout_seconds',2))

        if res['timeout']:
            notes.append(
                f"Timeout in case '{case_name}' after {res['elapsed']:.1f}s - "
                f"program likely has an infinite loop or is waiting for input"
            )
            continue

        out = res['stdout']
        out_norm = normalize_text(out, text_rules=text_tol)

        lines_in = [ln.strip() for ln in case.get('stdin','').splitlines() if ln.strip()]
        expected_map = compute_expected(ex_id, lines_in)

        per_label = case.get('weights',{}).get('per_label', total_labels // max(1,len(expected_map)))
        per_numeric = case.get('weights',{}).get('per_numeric', total_numeric // max(1,len(expected_map)))
        fmt_max = case.get('weights',{}).get('formatting_money', total_format)

        for key, exp in expected_map.items():
            label_found = any(key in ln for ln in out_norm.split('\n'))
            if label_found:
                earned_lab += per_label
            else:
                notes.append(f"Case '{case_name}': missing label '{key}'.")

            actual = None; line_no = None; line_text = None
            for idx, ln in enumerate(out.split('\n'), start=1):
                if key in normalize_text(ln, text_rules=text_tol):
                    # Try to find number after '=' or 'is' for better robustness
                    found_value = None
                    
                    # Strategy 1: Look for number after '=' sign (nerdy format)
                    if '=' in ln:
                        after_equals = ln.split('=', 1)[1]
                        nums_after = find_numbers_in_line(after_equals)
                        if nums_after:
                            found_value = nums_after[0][1]  # First number after '='
                    
                    # Strategy 2: Look for number after ' is ' (human format)
                    if found_value is None and ' is ' in ln.lower():
                        # Split on ' is ' case-insensitively
                        parts = ln.lower().split(' is ', 1)
                        if len(parts) > 1:
                            # Make sure the key is in the part BEFORE 'is'
                            if key.lower() in parts[0]:
                                # Get numbers from part AFTER 'is'
                                after_is = ln.split(' is ', 1)[1] if ' is ' in ln else ln.split(' IS ', 1)[1]
                                nums_after = find_numbers_in_line(after_is)
                                if nums_after:
                                    found_value = nums_after[0][1]
                    
                    # Strategy 3: Fallback - take last number in line (avoids input echo)
                    if found_value is None:
                        nums = find_numbers_in_line(ln)
                        if nums:
                            found_value = nums[-1][1]  # Last number (likely the answer)
                    
                    if found_value is not None:
                        actual = found_value
                        line_no = idx
                        line_text = ln
                        break
            
            # Final fallback: find ANY number in output (original behavior)
            if actual is None:
                for idx, ln in enumerate(out.split('\n'), start=1):
                    nums = find_numbers_in_line(ln)
                    if nums:
                        actual = nums[-1][1]  # Changed from [0] to [-1] for last number
                        line_no = idx
                        line_text = ln
                        break

            if actual is None:
                notes.append(f"Case '{case_name}': could not detect a numeric value for '{key}'.")
            else:
                if isclose(actual, exp, rel_tol=num_tol.get('rel_tol',1e-3), abs_tol=num_tol.get('abs_tol',1e-2)):
                    earned_num += per_numeric
                else:
                    notes.append( f"Case '{case_name}': numeric mismatch for '{key}' — expected ≈ {exp:.6g}, found {actual} " f"(tolerance rel={num_tol.get('rel_tol')}, abs={num_tol.get('abs_tol')})."
                    )

            if money_ex and line_text is not None:
                dec_count = 0
                try:
                    s = str(actual)
                    if '.' in s:
                        dec_count = len(s.split('.')[1])
                except Exception:
                    pass
                per_money = fmt_max // max(1,len(expected_map))
                if dec_count <= 2:
                    earned_fmt += per_money
                else:
                    extra = dec_count - 2
                    awarded = max(per_money - penalty_per_extra * extra, fmt_min_points)
                    earned_fmt += awarded
                    formatting_issues[case_name].append({ 'rule_id': 'money_max_2dp', 'description': 'Monetary values should print with no more than 2 decimal places.', 'pattern': '$X.YY (use format spec: {:.2f} or round(value, 2))',
                        'line': line_no or 0,
                        'actual': line_text or '',
                        'tip': ' '.join(fmt_tips)
                    })

    def finalize(task, earned):
        task['earned'] = min(task['max'], earned)
        task['status'] = 'pass' if task['earned'] == task['max'] else ('partial' if task['earned']>0 else 'fail')

    finalize(tasks[0], earned_num)
    finalize(tasks[1], earned_lab)
    if money_ex:
        finalize(tasks[2], earned_fmt)

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
    import sys
    return sys.executable
