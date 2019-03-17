n, str_ = input().split()
n = int(n)
print((str_.count("L") - str_.count("R")) % n)
