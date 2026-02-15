import argparse, sys
from core.config_schema import load_config
from core.harness import grade_io
from core.harness_text import grade_text
from core.harness_table import grade_table
from core.harness_guessing import grade_guessing_game
from core.harness_lucky_sevens import grade_lucky_sevens
from core.harness_file_io import grade_file_io
from core.harness_function import grade_functions
from core.harness_gui_structure import grade_gui_structure
from core.reporting import write_reports

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', required=True)
    ap.add_argument('--student-path', required=True)
    ap.add_argument('--out', default='report_out')
    args = ap.parse_args()

    cfg = load_config(args.config)
    mode = cfg.get('mode')
    
    if mode == 'io':
        result = grade_io(cfg, args.student_path)
    elif mode == 'text':
        result = grade_text(cfg, args.student_path)
    elif mode == 'table':
        result = grade_table(cfg, args.student_path)
    elif mode == 'guessing_game':
        result = grade_guessing_game(cfg, args.student_path)
    elif mode == 'lucky_sevens':
        result = grade_lucky_sevens(cfg, args.student_path)
    elif mode == 'file_io':
        result = grade_file_io(cfg, args.student_path)
    elif mode == 'function':
        result = grade_functions(cfg, args.student_path)
    elif mode == 'gui_structure':
        result = grade_gui_structure(cfg, args.student_path)
    elif mode == 'api':
        print('API mode is not implemented in this toolkit.', file=sys.stderr)
        sys.exit(2)
    else:
        print(f'Unknown mode: {mode}. Use io, text, table, guessing_game, lucky_sevens, file_io, function, gui_structure, or api.', file=sys.stderr)
        sys.exit(2)
    
    write_reports(result, args.out)
    
    # Print report.txt to screen
    report_path = f"{args.out}/report.txt"
    try:
        with open(report_path, 'r') as f:
            print("\n" + "="*60)
            print(f.read())
            print("="*60)
    except FileNotFoundError:
        print(f"Warning: Could not find {report_path}", file=sys.stderr)
    
    sys.exit(0 if result['summary']['score']==100 else 1)

if __name__ == '__main__':
    main()
