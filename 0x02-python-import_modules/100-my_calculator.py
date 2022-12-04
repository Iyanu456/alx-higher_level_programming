#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
operator = ['+', '-', '*', '/']
if len(sys.argv) != 4:
    print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
    sys.exit(1)
a = int(sys.argv[1])
b = int(sys.argv[3])
func = [add(a, b), sub(a, b), mul(a, b), div(a, b)]
for i in range(0, 4):
    if sys.argv[2] == operator[i]:
        print("{} {} {} = {}".format(a, sys.argv[2], b, func[i]))
        sys.exit()
    else:
        continue
print("Unknown operator. Available operators: +, -, * and /")
sys.exit(1)
