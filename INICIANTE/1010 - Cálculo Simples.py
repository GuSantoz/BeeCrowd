cod_p1, n_p1, v_p1 = input().split(" ")
cod_p2, n_p2, v_p2 = input().split(" ")

cod_p1 = int(cod_p1)
n_p1 = int(n_p1)
v_p1 = float(v_p1)

cod_p2 = int(cod_p2)
n_p2 = int(n_p2)
v_p2 = float(v_p2)

preco_1 = n_p1 * v_p1
preco_2 = n_p2 * v_p2
total = preco_1 + preco_2

print(f'VALOR A PAGAR: R$ {total:.2f}')
