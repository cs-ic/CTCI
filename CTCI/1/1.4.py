def func(string):
    dic = dict()
    for char in string:
        if char in dic and char != " ":
            dic[char] += 1
        else:
            dic[char] = 1

    check = True

    for i in dic.values():
        if not i % 2 == 0:
            if not check:
                return check
            else:
                check = False

    return True


print(func("tact coa".replace(" ", "")))
