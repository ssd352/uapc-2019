hh_curr, mm_curr = [int(_) for _ in input().split(':')]
hh_target, mm_target = [int(_) for _ in input().split(':')]
# if hh_curr == hh_target and mm_curr == mm_target:
#     print('')
buttons = ['S']
# diffs = min((hh_curr - hh_target) % 12, (hh_target - hh_curr) % 12)
if hh_curr < hh_target:
    ups = hh_target - hh_curr
    downs = 12 - ups
else:
    downs = hh_curr - hh_target
    ups = 12 - downs
if ups <= downs:
    buttons += ["U"] * ups
else:
    buttons += ["D"] * downs
buttons.append('S')

if mm_curr < mm_target:
    ups = mm_target - mm_curr
    downs = 60 - ups
else:
    downs = mm_curr - mm_target
    ups = 60 - downs
if ups <= downs:
    buttons += ["U"] * ups
else:
    buttons += ["D"] * downs
buttons.append("S")
print(''.join(buttons))
