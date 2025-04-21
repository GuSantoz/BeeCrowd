idade = int(input())
acum = 0
cont = 0

while idade >= 0:
    if idade > 0:
        acum += idade
    cont += 1
    idade = int(input())
    
total = acum/cont    
print(f'{total:.2f}')
