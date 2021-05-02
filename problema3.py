import random

nombre = input('Ingrese su Nombre: ')
apellido = input('Ingrese su Apellido: ')
try:
    if nombre and apellido:
        clave = f'{nombre[0].upper()}{random.randrange(1, 999)}{apellido[-2:]}'
        print(clave)
        input("Presiones cualquier tecla para finalizar")
    else:
        print('No ha ingresado valores')
except Exception as error:
    print(error)