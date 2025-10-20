
import io, sys
from contextlib import redirect_stdout

def capture_print(fn, *args, **kwargs):
    buf = io.StringIO()
    with redirect_stdout(buf):
        fn(*args, **kwargs)
    return buf.getvalue().strip()

def join_lines(lines):
    return "\n".join(str(x) for x in lines)

def check_equal(name, got, expected, totals):
    totals['total'] += 1
    ok = (got == expected)
    if ok:
        totals['passed'] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: expected={expected!r}, got={got!r}")
