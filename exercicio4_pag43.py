def stat(dic):
    s = sum(dic.values())
    med = s / len(dic.values())
    var = max(dic.values()) - min(dic.values())
    return s, med, var
d = { chr(v): v for v in range(55, 70)}
print(d)
print(stat(d))
