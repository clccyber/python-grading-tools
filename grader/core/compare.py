
import math, re

def isclose(a, b, rel_tol=1e-3, abs_tol=1e-2):
    try:
        return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)
    except Exception:
        return False

_def_text = {'case_insensitive': True, 'ignore_trailing_space': True, 'collapse_internal_spaces': True}

def normalize_text(s, text_rules=None):
    tr = dict(_def_text)
    if text_rules:
        tr.update(text_rules)
    out = s
    out = out.replace('\r\n','\n').replace('\r','\n')
    if tr.get('ignore_trailing_space', True):
        out = '\n'.join([ln.rstrip() for ln in out.split('\n')])
    if tr.get('collapse_internal_spaces', True):
        out = '\n'.join([' '.join(ln.split()) for ln in out.split('\n')])
    if tr.get('case_insensitive', True):
        out = out.lower()
    return out

_money_any_dec = re.compile(r"\$?(-?\d+(?:\.(\d+))?)")
_money_max2 = re.compile(r"\$?-?\d+(?:\.\d{1,2})?")


def find_money_values(text):
    vals = []
    for i, line in enumerate(text.split('\n'), start=1):
        for m in _money_any_dec.finditer(line):
            num = m.group(1)
            dec = m.group(2) or ''
            try:
                vals.append((i, m.group(0), float(num), len(dec)))
            except Exception:
                pass
    return vals

_float_any = re.compile(r"-?\d+(?:\.\d+)?")

def find_numbers_in_line(line):
    res = []
    for m in _float_any.finditer(line):
        try:
            res.append((m.group(0), float(m.group(0))))
        except Exception:
            pass
    return res


def enforce_max2_decimals(line):
    return bool(_money_max2.search(line))
