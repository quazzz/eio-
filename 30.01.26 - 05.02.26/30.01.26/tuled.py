x = int(input()) # 4h only
y = int(input()) # 5h only
n = int(input()) # budget

x/= 100
y/= 100
if x * 4 + y * 5 < n:
    print(9)
elif x < y:
    if(4 * x > n):
        print(n / x)
    else:
        jaak = n - 4 * x
        print(4 + jaak / y)
else:
    if(5 * y > n):
        print(n / y)
    else:
        jaak = n - 5 * y
        print(5 + jaak / x)