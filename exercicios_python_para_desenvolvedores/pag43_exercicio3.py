def flatten(it):
    if isinstance(it, list):
        ls = []
        for item in it:
            ls = ls +flatten(item)

        return ls
    else:
        return[it]
l = [[1, [2]], [3, 4], [[5, 6], 7]]
print(flatten(l))
