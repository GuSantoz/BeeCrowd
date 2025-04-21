N = int(input())

for _ in range(N):
    divisivel = 0
    X = int(input())
    for i in range(1, X):
        if X % i == 0:
            divisivel += i
    if divisivel == X:
        print(f'{X} eh perfeito')
    else:
        print(f'{X} nao eh perfeito')
        
