a, b = [int(_) for _ in input().split()]
if a + b > 2 ** 31 - 1:
    print("overflow")
else:
    print(a + b)
