
from pathlib import Path
import json
try:
    import yaml  # type: ignore
    HAVE_YAML = True
except Exception:
    HAVE_YAML = False

DEFAULTS = {
    'scoring': {
        'normalize_to_100': True,
        'percent_decimals': 0,
        'round_mode': 'half_up',
        'clamp_0_100': True
    },
    'tolerances': {
        'numeric': {'rel_tol': 1e-3, 'abs_tol': 1e-2},
        'text': {
            'case_insensitive': True,
            'ignore_trailing_space': True,
            'collapse_internal_spaces': True
        }
    },
    'timeout_seconds': 5,  # Generous for student code, catches infinite loops
}

def deep_merge(a, b):
    if isinstance(a, dict) and isinstance(b, dict):
        out = dict(a)
        for k,v in b.items():
            out[k] = deep_merge(a.get(k), v)
        return out
    return b if b is not None else a


def load_config(path):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f'Config not found: {p}')
    text = p.read_text(encoding='utf-8')
    cfg = None
    if HAVE_YAML:
        cfg = yaml.safe_load(text)
    else:
        cfg = json.loads(text)
    cfg = deep_merge(DEFAULTS, cfg)
    if cfg.get('mode') not in ('io', 'text', 'table', 'guessing_game', 'lucky_sevens', 'file_io', 'function', 'gui_structure', 'api'):
        raise ValueError('mode must be io, text, table, guessing_game, lucky_sevens, file_io, function, gui_structure, or api')
    # force integer scoring
    if cfg['scoring'].get('percent_decimals',0) != 0:
        cfg['scoring']['percent_decimals'] = 0
    return cfg
