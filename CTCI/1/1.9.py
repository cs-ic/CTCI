def issubstring(string_1, string_2):
    """
    string cancatenation is a high time complexity algorithm use string append instead in list DS
    """

    for i in string_2:
        if string_1 == string_2:
            return True
        else:
            temp = string_2[0]
            string_2 = string_2[1 : len(string_2)]
            string_2 = string_2 + temp
            print(string_1, string_2)

    return False


def func(string_1, stirng_2):
    """
    if you consider waterbottle = xy and erbottlewat = yx
    then if you add yx+yx it becomes yxyx and xy i.e. water bottle repeats itself in string
    so all you have to do now is check for the presence of xy in yxyx string
    """
    stirng_2 = stirng_2 + stirng_2
    if string_1 in stirng_2:
        return True
    else:
        return False


print(issubstring("waterbottle", "erbottlewat"))
print(func("waterbottle", "erbottlewat"))

""" Second method is far better as string cancatination is O(n^2) and even if we use list with pop and 
append function which are constant time complexities the comparision is in itself O(mn) time complexity
whereas in second function string cancatination takes place only once and rest is O(mn) time complexity
where O(m) is the length of smaller string as once it reaches middle of the string and exceeds the midpoint
remianing string will be shorter than the comparison string so the given string will not be a rotation
hence we can avoid uneccasary checks with specific conditional constraints"""
