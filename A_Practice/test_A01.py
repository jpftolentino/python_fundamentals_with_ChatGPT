
# Tests for A01 — Printing
from importlib import import_module
from test_utils import capture_print, check_equal, join_lines

M = import_module("A01_Printing")

def run_practice(t):
    check_equal("A01-P1", capture_print(M.a1_p1), "Hello, Python!", t)
    check_equal("A01-P2", capture_print(M.a1_p2, "Ada"), join_lines(["Ada"]*5), t)
    check_equal("A01-P3", capture_print(M.a1_p3), "1 2 3 4 5", t)
    check_equal("A01-P4", capture_print(M.a1_p4), "She said 'Hi!'", t)
    check_equal("A01-P5", capture_print(M.a1_p5), "Hello\nPython", t)
    check_equal("A01-P6", capture_print(M.a1_p6), "HelloWorld", t)
    check_equal("A01-P7", capture_print(M.a1_p7, "Alice", 25), "My name is Alice and I am 25 years old.", t)
    check_equal("A01-P8", capture_print(M.a1_p8, "Bob", 30), "My name is Bob and I am 30 years old.", t)
    check_equal("A01-P9", capture_print(M.a1_p9), "Hi " * 10, t)
    expected = "roses are red\nviolets are blue\npython is fun"
    check_equal("A01-P10", capture_print(M.a1_p10), expected, t)

def run_review(t):
    check_equal("A01-R1", capture_print(M.a1_r1), "Hello, Python!", t)
    check_equal("A01-R2", capture_print(M.a1_r2, "Ada"), join_lines(["Ada"]*5), t)
    check_equal("A01-R3", capture_print(M.a1_r3), "She said 'Hi!'", t)
    check_equal("A01-R4", capture_print(M.a1_r4, 95), "My score is 95", t)
    check_equal("A01-R5", capture_print(M.a1_r5), "Hi " * 10, t)

def main():
    totals = {'total':0,'passed':0}
    run_practice(totals)
    run_review(totals)
    print("-"*60)
    print(f"Summary A01: {totals['passed']}/{totals['total']} passed")

if __name__ == "__main__":
    main()
