n = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
valor = n
print(n)
for nota in notas:
    qtd = valor // nota
    valor -= qtd * nota
    print(f'{qtd} nota(s) de R$ {nota},00')
    
        
