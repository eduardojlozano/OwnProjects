n = int(input('Ingreses numero n: '))
c = int(input('Ingreses numero c: '))

count = 0

for i in range(1, n+1):
    if count != c:
        if n % i == 0:
            print(i)
            count += 1
    else:
        break