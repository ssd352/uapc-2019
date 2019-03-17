T = int(input())
for _ in range(T):
    str_ = input()
    if str_[0] != "0":
        print('equivalent')
    else:
        if any(char != "0" for char in str_[:-1]):
            print('not equivalent')
        elif int(str_[-1]) > 7:
            print('not equivalent')
        else:
            print('equivalent')
