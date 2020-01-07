string = "Mr John Smith   "

# bruteforce

"""

# highly inefficient using O(3n) time with 1st loop, len function and reversed solution

solution = str()

for n, i in enumerate(string):
    if i == " ":
        solution = solution + "%20"
    else:
        solution = solution + i

n = len(solution)

for i in reversed(solution):
    if i == "0" or i == "2" or i == "%":
        n -= 1
    else:
        break

print(string)
print(solution[0:n])

"""

# using inbuilt replace function
"""
# using inbuilt replace function
# better execution but still feels extremely unefficient
# and in order to remove the slicing function i could just cound the spaces left after the
# first occurence of a word and then use replace function for the first n spaces


for n, i in enumerate(reversed(string)):
    if not i == " ":
        break

string = string[0:-n].replace(" ", "%20")
print(string)
"""

# if i use the given information to me before hand that how many characters end up being after
# print(string[: 13].replace(" ", "%20"))

