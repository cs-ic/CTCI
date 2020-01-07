string = "abcdefghijka"


# Brute force approach

"""
check = set()
for char in string:
    if char in check:
        print(char, " is already present in string")
    else:
        check.add(char)
"""

# hash checker approach

check = {}

for char in string:
    if check[char]:
        print(char, " is present in the string")
    else:
        check.update({char: 1})
"""
attempted but cant work out the --if check[char] == 1:-- part
as if i use char in check then its better to use set in brute 
force approach but i think both check[char] and char in check are
linear time complexity

"""

# bit wise check
