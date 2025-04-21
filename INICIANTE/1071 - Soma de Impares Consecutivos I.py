x = int(input())
y = int(input())

acum = 0

if x > y:
    y = y + 1
    while y < x:
        if y % 2 != 0:
            acum = acum + y
        y = y + 1
else:
    x = x + 1
    while y > x:
        if x % 2 != 0:
            acum = acum + x
        x += 1
print(acum)
