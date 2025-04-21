N = int(input())

for _ in range(N):
    pontosJ = 0
    pontosM = 0
    for i in range(6):
        if i <= 2:
            X, D = input().split()
            X, D = int(X), int(D)
            pontosJ += (X * D)
        else:
            X, D = input().split()
            X, D = int(X), int(D)
            pontosM += (X * D)
    if pontosJ > pontosM:
        print('JOAO')
    else:
        print('MARIA')
    
