def func(a, b):
    if len(a) != len(b):
        (x, y) = (a, b) if len(a) > len(b) else (b, a)
        y = y + "0"
        for i in range(len(x)):
            if x[i] != y[i]:
                y = y[:i] + x[i] + y[i : len(x) - 1]
                return x == y

    if len(a) == len(b):
        count = 0
        for i, j in zip(a, b):
            if i != j:
                count += 1
        return count <= 1

    return 0


"""
There is another approach pending of combining all three insertion, deletion and replacement 
function in a single function
The other approach work on pointers/index if a particual index do not match move on and put check = False
and if again another check donot match return Fasle
/bin/bash: ws: command not found

"""

print(
    func("pale", "ple"),
    func("pales", "pale"),
    func("pale", "bale"),
    func("pale", "bake"),
)

