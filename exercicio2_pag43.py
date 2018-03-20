limite = int(input('Digite qual numero deseja descobrir se é primo: '))
primo = 1
i = limite // 2
while i > 1:
    if limite % i == 0: break
    i -= 1
else:
    if(i == 1):
        print("seu numero é primo")
        primo = 0
if(primo == 1):
    print("seu numero não é primo")
