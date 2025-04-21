EPR = 0
EHD = 0
intruso = 0

def imprime():
    global EPR, EHD, intruso  
    print(f'EPR: {EPR}')
    print(f'EHD: {EHD}')
    print(f'INTRUSOS: {intruso}')
    EPR = 0
    EHD = 0
    intruso = 0

def lista(n):
    global EPR, EHD, intruso  
    for i in range(n):
        matricula, sigla = input().split()
        if sigla == 'EPR':
            EPR += 1
        elif sigla == 'EHD':
            EHD += 1
        else:
            intruso += 1
    imprime()

while True:
    try:
        n = int(input())
        lista(n)  
    except EOFError:  
        break
