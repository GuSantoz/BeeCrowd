N = int(input())

cont = 1

while cont <= N:
    if cont % 2 == 0:
        print(f'{cont}^2 = {cont**2}')
    cont += 1
