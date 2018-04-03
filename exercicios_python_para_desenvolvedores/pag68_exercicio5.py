import os
pasta1 = os.listdir("C:/Users/Gabriel/Desktop/exercicios_python_para_desenvolvedores/")
pasta2 = os.listdir("C:/Users/Gabriel/Desktop/exercicios_python_para_desenvolvedores/pasta_teste/")

novaLista1 = []
novaLista2 = []
nomeArquivos1 = []
nomeArquivos2 = []
arquivosIguais = []
contador1 = 0
contador2 = 0
contador3 = 0

for nomes1 in pasta1:
    if nomes1.endswith(".txt"):
        nomeNovo1 = "C:/Users/Gabriel/Desktop/exercicios_python_para_desenvolvedores/%s" % (nomes1)
        f1 = open(nomeNovo1, 'r')
        novaLista1.append(f1.read())
        nomeArquivos1.append(nomes1)
        f1.close()
        contador1 += 1

for nomes2 in pasta2:
    if nomes2.endswith(".txt"):
        nomeNovo2 = "C:/Users/Gabriel/Desktop/exercicios_python_para_desenvolvedores/pasta_teste/%s" % (nomes2)
        f2 = open(nomeNovo2, 'r')
        novaLista2.append(f2.read())
        nomeArquivos2.append(nomes2)
        f2.close()
        contador2 += 1

while contador3 < contador1:
    contador4 = 0
    while contador4 < contador2:
        if novaLista1[contador3] == novaLista2[contador4]:
            arquivosIguais.append(nomeArquivos1[contador3])
            arquivosIguais.append(nomeArquivos2[contador4])
        contador4 += 1
    contador3 += 1
print('Esses são os arquivos que são iguais na pasta 1 e na pasta 2: ')
print(arquivosIguais)
            
