A,B,C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)
PI = 3.14159

TRIANGULO = (A * C)/2
CIRCULO = PI * C**2
TRAPEZIO = ((A + B) * C)/2
QUADRADO = B * B
RETANGULO = A * B

print(f'TRIANGULO: {TRIANGULO:.3f}')
print(f'CIRCULO: {CIRCULO:.3f}')
print(f'TRAPEZIO: {TRAPEZIO:.3f}')
print(f'QUADRADO: {QUADRADO:.3f}')
print(f'RETANGULO: {RETANGULO:.3f}')
