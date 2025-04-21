n1,n2,n3,n4 = input().split(" ")

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1*2) + (n2*3) + (n3*4) + (n4*1))/10

if media >= 7:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')

elif media < 5:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')        
    
elif 5 <= media < 7:
    exame = float(input())
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    print(f'Nota do exame: {exame:.1f}')
    media_final = (media + exame) / 2
    if media_final >= 5:
        print('Aluno aprovado.')
        print(f'Media final: {media_final:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {media_final:.1f}')
else:
    print('Aluno reprovado.')
