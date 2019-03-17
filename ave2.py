n = int(input())
point_set = set()
mx = 0.0
my = 0.0
for _ in range(n):
    x, y = [int(_) for _ in input().split()]
    point_set.add((x, y))
    mx += x
    my += y
mx /= n
my /= n
mirror = {(int(2 * mx - x), int(2 * my - y)) for x, y in point_set}
if mirror == point_set:
    print('symmetric')
else:
    print('not symmetric')
