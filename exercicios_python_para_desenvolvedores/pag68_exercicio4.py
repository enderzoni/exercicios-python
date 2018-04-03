import argparse
import sys

def fragmentaArquivo(entraArquivo, tamanhoPedaco):

    f = open(entraArquivo, 'rb')
    data = f.read()
    f.close()

    bytes = len(data)

    nomePedacos = []
    j = 0
    for i in range(0, bytes + 1, tamanhoPedaco):
        j += 1
        fn1 = "%s_00%s" % (entraArquivo, j)
        nomePedacos.append(fn1)
        f = open(fn1, 'wb')
        f.write(data[i:i + tamanhoPedaco])
        f.close()
        
def juntaArquivos(nomeArquivos,numDePedacos):

    dataList = []
    for i in range(1, numDePedacos):
        chunkName = nomeArquivos+'_00%s'%i
        f = open(chunkName, 'r')
        dataList.append(f.read())
        f.close()
        print(dataList)
    for y in range(0, numDePedacos - 1):
        data = dataList[y]
        f2 = open(nomeArquivos, 'a')
        f2.write(data)
        f2.close() 
