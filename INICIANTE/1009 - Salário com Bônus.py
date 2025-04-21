nome = input()
salario = float(input())
vendas = float(input())

bonus = vendas * 0.15

salario_total = bonus + salario

print(f'TOTAL = R$ {salario_total:.2f}')
