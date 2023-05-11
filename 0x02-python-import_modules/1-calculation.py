#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    addR = add(a, b)
    subR = sub(a, b)
    mulR = mul(a, b)
    divR = div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, addR))
    print("{:d} - {:d} = {:d}".format(a, b, subR))
    print("{:d} * {:d} = {:d}".format(a, b, mulR))
    print("{:d} / {:d} = {:d}".format(a, b, divR))
