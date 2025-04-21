A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

numeros = [A, B, C, D, E]
I = 0

for numero in numeros:
    if numero%2 == 0:
        I = I + 1
    
print(f'{I} valores pares')
