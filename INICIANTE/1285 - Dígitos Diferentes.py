while True:
    try:
        N, M = input().split()
        N, M = int(N), int(M)
        qtd = 0

        for i in range(N, M + 1):
            if len(set(str(i))) == len(str(i)):
                qtd += 1
                
        print(qtd)
        
    except EOFError:
        break
