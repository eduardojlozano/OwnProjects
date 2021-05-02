import math

n = int(input("Ingrese un numero entero: "))
i = 0

suma = 0

while i < n:
    print(f'{(1 + i) * math.pow((-1), i) } / {math.pow(n-2, i)}')
    result = ((1 + i) * math.pow((-1), i) / math.pow(n-2, i))
    print(result)
    print('\n')
    suma = suma + result
    i += 1
    result = 0

print(f'Resultado: {suma}')
