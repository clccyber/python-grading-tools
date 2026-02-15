
import subprocess, time

def run_subprocess(cmd, input_text=None, cwd=None, timeout=5):
    """
    Run a subprocess with timeout protection.
    
    Default timeout is 5 seconds - enough for student exercises, 
    not so long that infinite loops hang the grader.
    
    Returns:
        dict with keys:
            'returncode': int or None (if timeout)
            'stdout': str
            'stderr': str
            'elapsed': float (seconds)
            'timeout': bool (True if killed due to timeout)
    """
    start = time.time()
    try:
        proc = subprocess.run(
            cmd,
            input=input_text.encode('utf-8') if input_text is not None else None,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=cwd,
            timeout=timeout,
            check=False
        )
        elapsed = time.time() - start
        return {
            'returncode': proc.returncode,
            'stdout': proc.stdout.decode('utf-8', errors='replace'),
            'stderr': proc.stderr.decode('utf-8', errors='replace'),
            'elapsed': elapsed,
            'timeout': False
        }
    except subprocess.TimeoutExpired as e:
        elapsed = time.time() - start
        stdout = e.stdout.decode('utf-8', errors='replace') if e.stdout else ''
        stderr = e.stderr.decode('utf-8', errors='replace') if e.stderr else ''
        return {
            'returncode': None,
            'stdout': stdout,
            'stderr': stderr,
            'elapsed': elapsed,
            'timeout': True
        }
