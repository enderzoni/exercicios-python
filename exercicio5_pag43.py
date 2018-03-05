def inverso(frase):
    r = frase.split()
    for i in range(len(r)):
        r[i] = r[i][:: -1]
    return ' '.join(r)
frase = input('digite uma frase ')
print(inverso(frase))
