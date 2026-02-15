#!/usr/bin/env python3
"""
Cross-platform rubric viewer for Python exercises.
Copies the appropriate rubric to the current directory.

Usage:
    python rubric.py
"""

import sys
from pathlib import Path
import re
import shutil

def find_repo_root():
    """Find repository root by walking up until we find tools/rubrics/"""
    current = Path.cwd().resolve()
    while current != current.parent:
        rubrics_path = current / 'tools' / 'rubrics'
        if rubrics_path.exists() and rubrics_path.is_dir():
            return current
        current = current.parent
    
    raise Exception(
        'Could not locate repository root.\n'
        'Expected to find tools/rubrics/ somewhere above current directory.'
    )

def detect_exercise():
    """
    Detect chapter and exercise from current directory path.
    Expects structure: .../chapterN/exMM/student
    
    Returns: (chapter_dir, exercise_dir) e.g., ('chapter2', 'ex01')
    """
    cwd = Path.cwd().resolve()
    parts = cwd.parts
    
    try:
        student_idx = len(parts) - 1
        if parts[student_idx] != 'student':
            raise ValueError('Not in student directory')
        
        ex_dir = parts[student_idx - 1]  # exMM
        ch_dir = parts[student_idx - 2]  # chapterN
        
        # Validate format
        if not re.match(r'chapter\d+', ch_dir):
            raise ValueError(f'Invalid chapter directory: {ch_dir}')
        if not re.match(r'ex\d+', ex_dir):
            raise ValueError(f'Invalid exercise directory: {ex_dir}')
        
        return ch_dir, ex_dir
    
    except (IndexError, ValueError) as e:
        raise Exception(
            f'Could not detect exercise from path: {cwd}\n'
            f'Expected structure: .../chapterN/exMM/student\n'
            f'Error: {e}'
        )

def main():
    try:
        # Find repo and detect exercise
        root = find_repo_root()
        ch_dir, ex_dir = detect_exercise()
        
        # Locate rubric file
        rubric_name = f'{ch_dir}-{ex_dir}.md'
        rubric_path = root / 'tools' / 'rubrics' / rubric_name
        
        if not rubric_path.exists():
            print(f'Error: Rubric not found: {rubric_name}', file=sys.stderr)
            print(f'Expected at: {rubric_path}', file=sys.stderr)
            sys.exit(1)
        
        # Copy to current directory
        dest = Path.cwd() / 'RUBRIC.md'
        shutil.copy2(rubric_path, dest)
        
        print(f'✓ Rubric copied to RUBRIC.md')
        print(f'  Source: {rubric_name}')
        print(f'\nView with:')
        print(f'  cat RUBRIC.md')
        print(f'  or open in VS Code')
        
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
