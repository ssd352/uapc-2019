n = int(input())
cnt = 3
found = False
if n % cnt == 0:
    found = True
else:
    cnt = 5
    while cnt * cnt * cnt <= n:
        if n % cnt == 0:
            found = True
            break
        cnt += 2
        if n % cnt == 0:
            found = True
            break
        cnt += 4
if not found:
    print("RSA OK")
else:
    a = n // cnt
    if a % cnt == 0:
        print("RSA MISTAKE")
    else:
        div = int(a ** 0.5)
        if div * div == a:
            print('RSA MISTAKE')
        else:
            print("RSA OK")
