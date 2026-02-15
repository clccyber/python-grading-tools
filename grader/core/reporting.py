
import json
from pathlib import Path

def write_reports(result, out_dir='report_out'):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / 'report.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    lines = []
    s = result['summary']
    
    # Header
    lines.append("=" * 60)
    lines.append(f"  GRADE REPORT: {s['exercise_id']}")
    lines.append("=" * 60)
    lines.append("")
    
    # Score
    lines.append(f"Final Score: {s['score']} / 100")
    lines.append(f"Raw Points: {s['raw_earned']:.1f} / {s['raw_total']}")
    lines.append("")
    
    # Tasks breakdown
    lines.append("Task Breakdown:")
    lines.append("-" * 60)
    for t in result['tasks']:
        icon = '✓' if t['status']=='pass' else ('△' if t['status']=='partial' else '✗')
        status_label = t['status'].upper()
        lines.append(f"  {icon} {t['name']:<30} {t['earned']:>3}/{t['max']:<3}  [{status_label}]")
    lines.append("")
    
    # Notes section
    if result.get('notes'):
        lines.append("Notes:")
        lines.append("-" * 60)
        for n in result['notes']:
            lines.append(f"  • {n}")
        lines.append("")
    
    lines.append("=" * 60)
    (out / 'report.txt').write_text('\n'.join(lines), encoding='utf-8')
    if result.get('formatting_issues'):
        md = ['# Formatting Issues\n']
        for case_name, issues in result['formatting_issues'].items():
            if not issues: continue
            md.append(f"## Case: {case_name}\n")
            for idx, it in enumerate(issues, start=1):
                md.append(f"### {idx}. Rule `{it['rule_id']}` (Line {it['line']})\n")
                md.append(f"**Description:** {it['description']}\n")
                md.append(f"**Expected Pattern:** `{it['pattern']}`\n")
                md.append(f"**Your Output:**\n```\n{it['actual'].strip()}\n```\n")
                if it.get('tip'):
                    md.append(f"💡 **Tip:** {it['tip']}\n")
                md.append("---\n")
        (out / 'formatting_issues.md').write_text('\n'.join(md), encoding='utf-8')
