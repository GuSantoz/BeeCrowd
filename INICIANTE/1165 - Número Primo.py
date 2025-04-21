N = int(input()) 

for _ in range(N):
    divisivel = 0
    X = int(input())
    for i in range(1, X+1):
        if X % i == 0:
            divisivel += 1
    if divisivel == 2:
        print(f'{X} eh primo')
    else:
        print(f'{X} nao eh primo')
