linhas = 0
palavras = 0
caracter = 0
arquivo = input('Digite o nome do arquivo e seu endereço caso não esteja no mesmo diretório do programa: ')
with open(arquivo, 'rt') as f:
    for line in f:
        linhas = linhas + 1
        for word in line.split():
            palavras = palavras + 1
        for char in range(0, len(line)):
            caracter = caracter + 1
    print('linhas: ', linhas)
    print('palavras: ', palavras)
    print('caracteres: ', caracter)
