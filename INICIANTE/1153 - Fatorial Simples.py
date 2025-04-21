N = int(input())
cont = N - 1
acum = N * cont

while cont > 1:
    cont -= 1
    acum *= cont
        
print(acum)
