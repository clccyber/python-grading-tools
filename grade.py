#!/usr/bin/env python3
"""
Simple grader wrapper that auto-detects exercise and runs grading.

Usage from student directory:
    python ../../../tools/grade.py

Or from anywhere:
    python /path/to/tools/grade.py --student-path /path/to/student/dir
"""

import sys
import os
from pathlib import Path
import argparse

def find_tools_dir():
    """Find the tools directory relative to this script."""
    script_dir = Path(__file__).parent.resolve()
    return script_dir

def detect_exercise_from_path(student_path):
    """
    Detect exercise ID from student directory path.
    
    Expected structure:
        .../chapterN/exNN/student/
    
    Returns:
        "chapterN/exNN" or None
    """
    student_path = Path(student_path).resolve()
    
    # Should be in a 'student' directory
    if student_path.name != 'student':
        # Maybe they're in the exercise directory?
        if (student_path / 'student').exists():
            student_path = student_path / 'student'
        else:
            return None
    
    # Get parent directories
    exercise_dir = student_path.parent  # ex01, ex02, etc.
    chapter_dir = exercise_dir.parent   # chapter2, chapter3, etc.
    
    exercise_name = exercise_dir.name
    chapter_name = chapter_dir.name
    
    # Validate format
    if not chapter_name.startswith('chapter'):
        return None
    if not (exercise_name.startswith('ex') or exercise_name.startswith('dex')):
        return None
    
    return f"{chapter_name}/{exercise_name}"

def find_config(tools_dir, exercise_id):
    """Find the YAML config file for this exercise."""
    config_path = tools_dir / 'grader' / 'rules' / 'exercise' / f'{exercise_id.replace("/", "-")}.yml'
    
    if config_path.exists():
        return config_path
    
    return None

def main():
    parser = argparse.ArgumentParser(
        description='Grade a Python exercise automatically',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # From student directory (auto-detects everything):
  cd chapter2/ex01/student
  python ../../../tools/grade.py
  
  # Explicit paths:
  python tools/grade.py --student-path chapter2/ex01/student
        """
    )
    
    parser.add_argument(
        '--student-path',
        default='.',
        help='Path to student directory (default: current directory)'
    )
    
    parser.add_argument(
        '--config',
        help='Path to config file (default: auto-detect from exercise)'
    )
    
    parser.add_argument(
        '--out',
        help='Output directory for feedback files (default: student directory)'
    )
    
    args = parser.parse_args()
    
    # Resolve paths
    tools_dir = find_tools_dir()
    student_path = Path(args.student_path).resolve()
    
    # Validate student path
    if not student_path.exists():
        print(f"Error: Student path does not exist: {student_path}", file=sys.stderr)
        sys.exit(1)
    
    # Detect exercise ID
    exercise_id = detect_exercise_from_path(student_path)
    if not exercise_id:
        print(f"Error: Could not detect exercise from path: {student_path}", file=sys.stderr)
        print(f"Expected structure: .../chapterN/exNN/student/", file=sys.stderr)
        sys.exit(1)
    
    print(f"Detected exercise: {exercise_id}")
    
    # Find config
    if args.config:
        config_path = Path(args.config)
    else:
        config_path = find_config(tools_dir, exercise_id)
    
    if not config_path or not config_path.exists():
        print(f"Error: No grading config found for {exercise_id}", file=sys.stderr)
        print(f"Expected: {config_path}", file=sys.stderr)
        print(f"", file=sys.stderr)
        print(f"This exercise may not have automated grading available yet.", file=sys.stderr)
        sys.exit(1)
    
    print(f"Using config: {config_path.name}")
    
    # Determine output directory
    out_dir = Path(args.out) if args.out else student_path
    
    # Import and run the actual grader
    sys.path.insert(0, str(tools_dir / 'grader'))
    
    try:
        from run_grader import main as run_grader_main
        
        # Override sys.argv to pass arguments to run_grader
        original_argv = sys.argv
        sys.argv = [
            'run_grader.py',
            '--config', str(config_path),
            '--student-path', str(student_path),
            '--out', str(out_dir)
        ]
        
        # Run the grader
        run_grader_main()
        
        # Restore argv
        sys.argv = original_argv
        
    except ImportError as e:
        print(f"Error: Could not import grader: {e}", file=sys.stderr)
        print(f"Make sure grader/ directory is in {tools_dir}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error running grader: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
