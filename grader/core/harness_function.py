import sys, os
import tempfile, shutil
from pathlib import Path
import inspect
from .utils import run_subprocess

def half_up(n):
    return int(n + 0.5)

def has_main_block(file_path):
    """Check if file has 'if __name__ == "__main__"' block"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            return '__name__' in content and '__main__' in content
    except:
        return False

def find_student_python_file(student_dir, config):
    """
    Find the student's Python file to grade.
    
    Priority:
    1. Check config['target_file'] if specified (NEW)
    2. Check config['module_file'] if specified (LEGACY)
    3. Fall back to heuristics:
       - If only one .py file → use it
       - If multiple with __main__ → use newest
       - If multiple without __main__ → use newest
    
    Returns:
        Path to Python file, or None if not found
    """
    student_path = Path(student_dir)
    
    # NEW: Check if YAML specifies target_file
    target_file = config.get('target_file')
    if target_file:
        specified_path = student_path / target_file
        if specified_path.exists():
            return specified_path
        else:
            # Log warning but continue to fallback
            print(f"  Warning: Specified target_file '{target_file}' not found, using fallback detection")
    
    # LEGACY: Check module_file (old configs)
    module_file = config.get('module_file')
    if module_file:
        module_path = student_path / module_file
        if module_path.exists():
            return module_path
    
    # FALLBACK: Heuristic detection
    py_files = list(student_path.glob('*.py'))
    
    if not py_files:
        return None
    
    if len(py_files) == 1:
        return py_files[0]
    
    # Multiple files - check for __main__ blocks
    main_files = [f for f in py_files if has_main_block(f)]
    
    if main_files:
        # Pick newest among files with __main__
        return max(main_files, key=lambda f: f.stat().st_mtime)
    
    # No __main__ blocks - pick newest overall
    return max(py_files, key=lambda f: f.stat().st_mtime)

def grade_functions(cfg, student_path):
    """
    Grade exercises by importing student module and testing functions directly.
    
    Supports image processing functions with special validation.
    
    Config structure for image functions:
    function_tests:
      - name: grayscale
        weight: 100
        signature:
          params: ['image']
        image_validation:
          type: grayscale  # or: invert, posterize, sepia
          test_image: smokey.gif
          sample_pixels: 100
    """
    
    ex_id = cfg.get('exercise_id')
    function_tests = cfg.get('function_tests', [])
    
    if not function_tests:
        raise ValueError(f'No function_tests defined for {ex_id}')
    
    notes = []
    tasks = []
    
    # Find student Python file using new failsafe logic
    module_path = find_student_python_file(student_path, cfg)
    
    if not module_path:
        notes.append(f"No Python file found in student directory")
        return {
            'summary': {'exercise_id': ex_id, 'score': 0, 'raw_earned': 0, 'raw_total': 100},
            'tasks': [],
            'notes': notes,
            'formatting_issues': {}
        }
    
    module_file = module_path.name
    
    # Import the module
    try:
        # Add student path to sys.path temporarily
        original_path = sys.path.copy()
        sys.path.insert(0, str(student_path))
        
        module_name = module_file.replace('.py', '')
        
        # Clear any cached imports
        if module_name in sys.modules:
            del sys.modules[module_name]
        
        student_module = __import__(module_name)
        
    except SyntaxError as e:
        notes.append(f"Syntax error in {module_file}: {e}")
        notes.append(f"  Line {e.lineno}: {e.text}")
        sys.path = original_path
        return {
            'summary': {'exercise_id': ex_id, 'score': 0, 'raw_earned': 0, 'raw_total': 100},
            'tasks': [],
            'notes': notes,
            'formatting_issues': {}
        }
    except Exception as e:
        notes.append(f"Error importing {module_file}: {type(e).__name__}: {e}")
        sys.path = original_path
        return {
            'summary': {'exercise_id': ex_id, 'score': 0, 'raw_earned': 0, 'raw_total': 100},
            'tasks': [],
            'notes': notes,
            'formatting_issues': {}
        }
    
    # Test each function
    total_weight = sum(test.get('weight', 10) for test in function_tests)
    
    for func_test in function_tests:
        func_name = func_test.get('name')
        weight = func_test.get('weight', 10)
        signature_spec = func_test.get('signature', {})
        test_cases = func_test.get('cases', [])
        
        task = {
            'name': f'{func_name}()',
            'max': weight,
            'earned': 0,
            'status': 'fail'
        }
        
        # Check if function exists
        if not hasattr(student_module, func_name):
            notes.append(f"Function '{func_name}' not found in {module_file}")
            notes.append(f"  Expected function: def {func_name}(...)")
            tasks.append(task)
            continue
        
        func = getattr(student_module, func_name)
        
        # Check if it's actually a function
        if not callable(func):
            notes.append(f"'{func_name}' exists but is not a function (it's a {type(func).__name__})")
            tasks.append(task)
            continue
        
        # Validate signature if specified
        if signature_spec:
            try:
                sig = inspect.signature(func)
                expected_params = signature_spec.get('params', [])
                actual_params = [p.name for p in sig.parameters.values() 
                               if p.kind in (inspect.Parameter.POSITIONAL_OR_KEYWORD, 
                                           inspect.Parameter.POSITIONAL_ONLY)]
                
                if len(expected_params) != len(actual_params):
                    notes.append(
                        f"Function '{func_name}' has wrong number of parameters: "
                        f"expected {len(expected_params)} ({', '.join(expected_params)}), "
                        f"got {len(actual_params)} ({', '.join(actual_params)})"
                    )
                    tasks.append(task)
                    continue
                    
            except Exception as e:
                notes.append(f"Could not inspect signature of '{func_name}': {e}")
        
        # Run test cases
        passed = 0
        failed = 0
        
        # Check for image validation (special case for PIL exercises)
        image_validation = func_test.get('image_validation')
        if image_validation:
            # Handle image processing functions
            try:
                result = validate_image_function(
                    func, 
                    image_validation, 
                    student_path,
                    notes
                )
                if result['passed']:
                    passed = result['checks_passed']
                    failed = result['checks_failed']
                else:
                    failed = 1
                    notes.append(result.get('error', 'Image validation failed'))
            except Exception as e:
                failed = 1
                notes.append(f"Error validating image function: {e}")
        
        else:
            # Regular test cases
            for i, case in enumerate(test_cases, 1):
                args = case.get('args', [])
                kwargs = case.get('kwargs', {})
                expected = case.get('expected')
                tolerance = case.get('tolerance', 0.0001)  # For float comparison
                case_name = case.get('name', f'case_{i}')
                
                try:
                    result = func(*args, **kwargs)
                    
                    # Compare result to expected
                    if expected is not None:
                        # Check return type if specified
                        expected_type = signature_spec.get('returns')
                        if expected_type:
                            expected_type_obj = eval(expected_type) if isinstance(expected_type, str) else expected_type
                            if not isinstance(result, expected_type_obj) and not (
                                expected_type_obj == float and isinstance(result, int)
                            ):
                                notes.append(
                                    f"{func_name}({format_args(args)}): "
                                    f"returned {type(result).__name__}, expected {expected_type}"
                                )
                                failed += 1
                                continue
                        
                        # Compare values
                        if isinstance(expected, float) and isinstance(result, (int, float)):
                            if abs(result - expected) > tolerance:
                                notes.append(
                                    f"{func_name}({format_args(args)}): "
                                    f"returned {result}, expected {expected}"
                                )
                                failed += 1
                            else:
                                passed += 1
                        elif result != expected:
                            notes.append(
                                f"{func_name}({format_args(args)}): "
                                f"returned {repr(result)}, expected {repr(expected)}"
                            )
                            failed += 1
                        else:
                            passed += 1
                    else:
                        # No expected value, just check it runs
                        passed += 1
                        
                except Exception as e:
                    notes.append(
                        f"{func_name}({format_args(args)}): "
                        f"raised {type(e).__name__}: {e}"
                    )
                    failed += 1
        
        # Calculate score for this function
        total_tests = passed + failed
        if total_tests > 0:
            task['earned'] = int((passed / total_tests) * weight)
            task['status'] = 'pass' if failed == 0 else ('partial' if passed > 0 else 'fail')
        
        tasks.append(task)
    
    # Restore sys.path
    sys.path = original_path
    
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

def format_args(args):
    """Format argument list for display"""
    if len(args) == 0:
        return ""
    if len(args) == 1:
        arg = args[0]
        if isinstance(arg, list):
            if len(arg) > 5:
                return f"{arg[:5]}..."
            return str(arg)
        return repr(arg)
    return ", ".join(repr(arg) if not isinstance(arg, list) else str(arg) for arg in args)

def validate_image_function(func, validation_config, student_path, notes):
    """
    Validate image processing functions.
    
    Returns:
        {
            'passed': bool,
            'checks_passed': int,
            'checks_failed': int,
            'error': str (if failed)
        }
    """
    import random
    
    # Try to import PIL
    try:
        from PIL import Image
    except ImportError:
        return {
            'passed': False,
            'checks_passed': 0,
            'checks_failed': 1,
            'error': 'PIL/Pillow not available for image validation'
        }
    
    validation_type = validation_config.get('type')
    test_image_name = validation_config.get('test_image', 'test.gif')
    sample_pixels = validation_config.get('sample_pixels', 100)
    
    # Load test image (look in student directory or use default)
    test_image_path = Path(student_path) / test_image_name
    if not test_image_path.exists():
        return {
            'passed': False,
            'checks_passed': 0,
            'checks_failed': 1,
            'error': f'Test image {test_image_name} not found'
        }
    
    try:
        original_image = Image.open(test_image_path)
    except Exception as e:
        return {
            'passed': False,
            'checks_passed': 0,
            'checks_failed': 1,
            'error': f'Could not load test image: {e}'
        }
    
    # Run the function
    try:
        # Make a copy to pass to function
        test_copy = original_image.copy()
        result_image = func(test_copy)
        
        # Some functions modify in place, some return new image
        if result_image is None:
            result_image = test_copy
    except Exception as e:
        return {
            'passed': False,
            'checks_passed': 0,
            'checks_failed': 1,
            'error': f'Function crashed: {type(e).__name__}: {e}'
        }
    
    # Validate based on type
    checks_passed = 0
    checks_failed = 0
    
    if validation_type == 'grayscale':
        # Check that all sampled pixels have R=G=B
        width, height = result_image.size
        for _ in range(min(sample_pixels, width * height)):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            
            try:
                pixel = result_image.getpixel((x, y))
                if isinstance(pixel, int):
                    # Already grayscale mode
                    checks_passed += 1
                else:
                    r, g, b = pixel[0], pixel[1], pixel[2]
                    if r == g == b:
                        checks_passed += 1
                    else:
                        checks_failed += 1
                        if checks_failed <= 3:  # Only report first few
                            notes.append(f"Pixel ({x},{y}) not grayscale: RGB({r},{g},{b})")
            except Exception as e:
                checks_failed += 1
                if checks_failed == 1:
                    notes.append(f"Error checking pixel: {e}")
    
    elif validation_type == 'invert':
        # Check that pixels are inverted (255 - original)
        width, height = result_image.size
        for _ in range(min(sample_pixels, width * height)):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            
            try:
                orig_pixel = original_image.getpixel((x, y))
                result_pixel = result_image.getpixel((x, y))
                
                # Handle both RGB and grayscale
                if isinstance(orig_pixel, int):
                    expected = 255 - orig_pixel
                    if abs(result_pixel - expected) <= 1:
                        checks_passed += 1
                    else:
                        checks_failed += 1
                else:
                    r1, g1, b1 = orig_pixel[0], orig_pixel[1], orig_pixel[2]
                    r2, g2, b2 = result_pixel[0], result_pixel[1], result_pixel[2]
                    
                    if (abs((255 - r1) - r2) <= 1 and
                        abs((255 - g1) - g2) <= 1 and
                        abs((255 - b1) - b2) <= 1):
                        checks_passed += 1
                    else:
                        checks_failed += 1
                        if checks_failed <= 3:
                            notes.append(f"Pixel ({x},{y}) not inverted properly")
            except Exception as e:
                checks_failed += 1
                if checks_failed == 1:
                    notes.append(f"Error checking inversion: {e}")
    
    elif validation_type == 'posterize':
        # Check that pixels match target RGB within threshold
        target_rgb = validation_config.get('target_rgb', (128, 128, 128))
        threshold = validation_config.get('threshold', 127)
        
        width, height = result_image.size
        for _ in range(min(sample_pixels, width * height)):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            
            try:
                pixel = result_image.getpixel((x, y))
                # Check if pixel is either black or target color
                if isinstance(pixel, int):
                    if pixel == 0 or abs(pixel - target_rgb[0]) <= 10:
                        checks_passed += 1
                    else:
                        checks_failed += 1
                else:
                    r, g, b = pixel[0], pixel[1], pixel[2]
                    is_black = (r < 10 and g < 10 and b < 10)
                    is_target = (abs(r - target_rgb[0]) <= 10 and
                               abs(g - target_rgb[1]) <= 10 and
                               abs(b - target_rgb[2]) <= 10)
                    if is_black or is_target:
                        checks_passed += 1
                    else:
                        checks_failed += 1
            except Exception as e:
                checks_failed += 1
                if checks_failed == 1:
                    notes.append(f"Error checking posterize: {e}")
    
    else:
        # Unknown validation type - just check function ran
        checks_passed = 1
    
    # Calculate result
    total_checks = checks_passed + checks_failed
    if total_checks == 0:
        total_checks = 1  # Avoid division by zero
    
    success_rate = checks_passed / total_checks
    passed = success_rate >= 0.9  # 90% of checks must pass
    
    return {
        'passed': passed,
        'checks_passed': checks_passed,
        'checks_failed': checks_failed
    }
