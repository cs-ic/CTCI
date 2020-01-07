def func(string):
    j = 1
    answer = list()
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            j += 1
        else:
            answer.append(string[i])
            answer.append(str(j))
            j = 1
    answer.append(string[i])
    answer.append(str(j))

    if len(answer) < len(string):
        return "".join(answer)
    else:
        return string


print(func("aabcccccaaa"), func("aabbccddee"))  # a2b1c5a3

