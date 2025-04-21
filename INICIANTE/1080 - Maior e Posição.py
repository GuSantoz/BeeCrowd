valores = 1
maior = 0

while valores <= 100:
    n = int(input())
    
    if n > maior:
        maior = n
        posicao = valores
        
    valores += 1
    
print(maior)
print(posicao)
