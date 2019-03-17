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

# if n % 2 == 1 and (mx, my) not in point_set:
#     print('not symmetric')
# else:
        # set_copy = point_set
cond = all((int(2 * mx - x), int(2 * my - y)) in point_set for x, y in point_set)
if cond:
    print('symmetric')
else:
    print('not symmetric')
    # for x, y in point_set:
    #     r = (int(2 * mx - x), int(2 * my - y))
    #     p = (x, y)
    #     if len(set_copy) == 0:
    #         print('symmetric')
    #         break
    #     elif p in set_copy and r in set_copy:
    #         set_copy.remove(p)
    #         set_copy.remove(r)
    #     elif (p in set_copy and r not in set_copy) or (r in set_copy and p not in set_copy):
    #         print('not symmetric')
    #         break
    # else:
    #     print('symmetric')
