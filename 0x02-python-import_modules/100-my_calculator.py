#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
operator = ['+', '-', '*', '/']
func = [add(a, b), sub(a, b), mul(a, b), div(a, b)]
if len(sys.argv) != 4:
    print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
    sys.exit(1)
for i in range(0, 4):
    if sys.argv[2] == operator[i]:
        print("{} {} {} = {}".format(int(sys.arg[1]), sys.argv[2], int(sys.argv[3]), func[i]))
        return
    else:
        continue
print("Unknown operator. Available operators: +, -, * and /")
sys.exit(1)
