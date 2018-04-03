reverso = False
chave = 0
dados = (3, 1, 4, 90, 12, 9, 43, 56)
chave = int(input('Digite a chave: '))
reverso_i = input('Deseja ativar o modo reverso?(S/N) ')
if(reverso_i == 'S'):
    reverso = True
while((chave >= 0) & (chave < len(dados))):
    print(dados[chave])
    if(reverso == True):
        chave = chave - 1
    else:
        chave = chave + 1
