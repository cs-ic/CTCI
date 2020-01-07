# Permutaions of string

str1 = "abcd"
str2 = "dbca"
str3 = "abcdf"

# brute force approach :
# sort the strings and compare two strings and print the output

"""
print(sorted(str1) == sorted(str2))
print(sorted(str1) == sorted(str3))
"""

# hash table :
# update key of dic with corresponding character in string and if dic of str1 == str2 the strings are equal

"""
dic = {}
for i in str1:
    if not i in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for i in str2:
    if not i in dic:
        dic[i] = 1
        print(False)
    else:
        dic[i] -= 1

print(0 == sum(dic.values()))

"""

# Resources
"""
------------------
You just have to use dict.values().
This will return a list containing all the values of your dictionary, without having to specify any key.

You may also be interested in:

.keys(): return a list containing the keys
.items(): return a list of tuples (key, value)
Note that in Python 3, returned value is not actually proper list but view object.

-------------------

That is a very strange way to organize things. If you stored in a dictionary, this is easy:

# This example should work in any version of Python.
# urls_d will contain URL keys, with counts as values, like: {'http://www.google.fr/' : 1 }
urls_d = {}
for url in list_of_urls:
    if not url in urls_d:
        urls_d[url] = 1
    else:
        urls_d[url] += 1
This code for updating a dictionary of counts is a common "pattern" in Python. It is so common that there is a special data structure, defaultdict, created just to make this even easier:

from collections import defaultdict  # available in Python 2.5 and newer

urls_d = defaultdict(int)
for url in list_of_urls:
    urls_d[url] += 1
If you access the defaultdict using a key, and the key is not already in the defaultdict, the key is automatically added with a default value. The defaultdict takes the callable you passed in, and calls it to get the default value. In this case, we passed in class int; when Python calls int() it returns a zero value. So, the first time you reference a URL, its count is initialized to zero, and then you add one to the count.

But a dictionary full of counts is also a common pattern, so Python provides a ready-to-use class: containers.Counter You just create a Counter instance by calling the class, passing in any iterable; it builds a dictionary where the keys are values from the iterable, and the values are counts of how many times the key appeared in the iterable. The above example then becomes:

from collections import Counter  # available in Python 2.7 and newer

urls_d = Counter(list_of_urls)
If you really need to do it the way you showed, the easiest and fastest way would be to use any one of these three examples, and then build the one you need.

from collections import defaultdict  # available in Python 2.5 and newer

urls_d = defaultdict(int)
for url in list_of_urls:
    urls_d[url] += 1

urls = [{"url": key, "nbr": value} for key, value in urls_d.items()]
If you are using Python 2.7 or newer you can do it in a one-liner:

from collections import Counter

urls = [{"url": key, "nbr": value} for key, value in Counter(list_of_urls).items()]

---------------------------------

Using the default works, but so does:

urls[url] = urls.get(url, 0) + 1
using .get, you can get a default return if it doesn't exist. By default it's None, but in the case I sent you, it would be 0.

-----------------------------------

"""

