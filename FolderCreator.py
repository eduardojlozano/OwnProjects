"""
Modulo que crea una carpeta en el mismo directorio de trabajo, si no existe, y la abre
Creado por:
@eduardojlozano@gmail.com
5/2021
"""

import os
import subprocess


def create_folder(dir_name):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    print(f'Creating folder {dir_name} on {desktop}...')
    new_directory = os.path.normpath(os.path.join(desktop, dir_name))
    print(new_directory)
    if os.path.isdir(new_directory):
        print('Carpeta ya existente')
        subprocess.Popen(f'explorer /select/, {new_directory}')
    else:
        os.mkdir(new_directory)
        subprocess.Popen(f'explorer /select/, {new_directory}')
        print('Carpeta creada con exito!')


if __name__ == "__main__":
    create_folder('tasks')
