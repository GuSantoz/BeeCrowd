A, B = input().split(" ")

A = int(A)
B = int(B)

if (B>A):
    RESTO = B%A
else:
    RESTO = A%B

if RESTO == 0:
    print("Sao Multiplos")
    
else:
    print("Nao sao Multiplos")
