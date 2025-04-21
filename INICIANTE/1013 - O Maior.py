a, b, c = input().split(" ")

a = int(a)
b = int(b)
c = int(c)

MaiorAB=(a+b+abs(a-b))/2

if MaiorAB > c:
    print(f'{MaiorAB:.0f} eh o maior')
else:
    print(f'{c:.0f} eh o maior')
