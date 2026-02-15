import sys
from .utils import run_subprocess
from .compare import normalize_text

def half_up(n):
    return int(n + 0.5)

def compute_expected_text(ex_id, lines):
    """
    Returns expected text patterns that should appear in output.
    For boolean/conditional exercises that output decisions, not numbers.
    """
    def f(i, cast=float, default=0.0):
        try:
            return cast(lines[i])
        except Exception:
            return default
    
    if ex_id == 'chapter3/ex01':
        # Equilateral triangle
        s1 = f(0, float); s2 = f(1, float); s3 = f(2, float)
        if s1 == s2 == s3:
            return {'required_phrase': 'is equilateral', 'forbidden_phrase': 'not'}
        else:
            return {'required_phrase': 'not', 'forbidden_phrase': None}
    
    if ex_id == 'chapter3/ex02':
        # Right triangle - Pythagorean theorem
        s1 = f(0, float); s2 = f(1, float); s3 = f(2, float)
        sides = sorted([s1, s2, s3])
        # a² + b² = c²
        is_right = abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 0.01
        if is_right:
            return {'required_phrase': 'is a right triangle', 'forbidden_phrase': 'not a right'}
        else:
            return {'required_phrase': 'not a right triangle', 'forbidden_phrase': None}
    
    return {}

def grade_text(cfg, student_path):
    """
    Grade exercises that output text decisions/patterns rather than numeric values.
    Used for conditional logic, boolean outputs, text-based responses.
    """
    tp = cfg.get('tolerances', {})
    text_tol = tp.get('text', {})
    ex_id = cfg.get('exercise_id')
    
    total_correctness = 80
    total_labels = 20
    
    tasks = [
        {'name':'decision_correctness','max': total_correctness,'earned':0,'status':'fail'},
        {'name':'output_presence','max': total_labels,'earned':0,'status':'fail'},
    ]
    
    notes = []
    earned_correct = earned_labels = 0
    
    for case in cfg.get('io_tests', []):
        case_name = case.get('name','case')
        res = run_subprocess([
            sys_exe(), '-I', cfg.get('entrypoint')
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
        expected = compute_expected_text(ex_id, lines_in)
        
        if not expected:
            notes.append(f"Case '{case_name}': no expected pattern defined")
            continue
        
        per_case_correct = case.get('weights',{}).get('per_decision', total_correctness // len(cfg.get('io_tests', [])))
        per_case_label = case.get('weights',{}).get('per_output', total_labels // len(cfg.get('io_tests', [])))
        
        # Check for required phrase
        required = expected.get('required_phrase', '')
        forbidden = expected.get('forbidden_phrase')
        
        # Basic check: did they produce any output?
        if out_norm.strip():
            earned_labels += per_case_label
        else:
            notes.append(f"Case '{case_name}': no output produced")
            continue
        
        # Check for correct decision
        has_required = required.lower() in out_norm
        has_forbidden = forbidden and forbidden.lower() in out_norm
        
        if has_required and not has_forbidden:
            earned_correct += per_case_correct
        else:
            if not has_required:
                notes.append(f"Case '{case_name}': expected phrase '{required}' not found in output")
            if has_forbidden:
                notes.append(f"Case '{case_name}': incorrect - output contains '{forbidden}' when it shouldn't")
    
    def finalize(task, earned):
        task['earned'] = min(task['max'], earned)
        task['status'] = 'pass' if task['earned'] == task['max'] else ('partial' if task['earned']>0 else 'fail')
    
    finalize(tasks[0], earned_correct)
    finalize(tasks[1], earned_labels)
    
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
