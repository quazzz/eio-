import sys

n = int(sys.stdin.readline())
digits = sorted(sys.stdin.readline().strip())

if len(digits) != n:
    digits = digits[:n]

num1 = digits[::2]
num2 = digits[1::2]

number1 = int(''.join(num1)) if num1 else 0
number2 = int(''.join(num2)) if num2 else 0

print(number1 + number2)