palavras = []
palavrasRegistradas = []
listaPronta = []
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
ocorrencia = []

arquivo = input('Digite o nome do arquivo e seu endereço caso não esteja no mesmo diretório do programa: ')
with open(arquivo, 'rt') as f:
    for line in f:
        for word in line.split():
            palavras.append(word)
            contador1 += 1
while contador2 < contador1:
    ocorrencia.append(palavras.count(palavras[contador2]))
    contador2 += 1
contador2 = 0
while contador2 < contador1:
    if palavras[contador2] in palavrasRegistradas:
        ocorrencia[contador2] = ocorrencia[contador2]
    else:
        palavrasRegistradas.append(palavras[contador2])
        listaPronta.append((palavras[contador2], ocorrencia[contador2]))
        contador3 += 1
    contador2 += 1
listaPronta.sort(key=lambda x: x[1], reverse = True)
while contador4 < contador3:
    print(listaPronta[contador4])
    contador4 += 1
