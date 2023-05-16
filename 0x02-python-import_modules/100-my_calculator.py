#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        calc = 0
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[3])
        match sys.argv[2]:
            case '+':
                calc = n1 + n2
            case '-':
                calc = n1 - n2
            case '*':
                calc = n1 * n2
            case '/':
                calc = n1 / n2
            case other:
                print("Unknown operator. Available operators: +, -, * and /")
                sys.exit(1)
        print("{:d} {} {:d} = {:d}".format(n1, sys.argv[2], n2, calc))
