#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[3])
    usr_op = sys.argv[2]
    ops = {"*": mul, "+": add, "-": sub, "/": div}
    if usr_op not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(n1, usr_op, n2, ops[usr_op](n1, n2)))
