num = int(input()) 
f1, f2 = 1,1
if num == 1:
    print(1)
elif num == 2:
    print(2)
else:
    for i in range(3, num):
        s = f1 + f2
        print(f"f1: {f1} f2: {f2} s: {s}")
        f2 = f1
        f1 = s
    print(s)