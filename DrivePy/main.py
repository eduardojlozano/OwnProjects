from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

import os

# Reemplazar el valor de la variable por el path del directorio que desea subir a Drive.
path = r"C:\Users\eduar\Desktop\prueba_Drive"

class Connection:
    def __init__(self):
        self.gauth = None

    def get_conn(self):
        try:
            # Debajo se realiza la autenticacion
            self.gauth = GoogleAuth()
            print(self.gauth)

            # Crea un webserver local y gestiona automaticamente la autenticacion.
            self.gauth.LocalWebserverAuth()
            drive = GoogleDrive(self.gauth)
            return drive
        except Exception as e:
            print(f"Error: {e}")

    def upload_files(self, drive):
        try:
            # Itera en el directorio deseado para subir archivo por archivo a drive.
            for x in os.listdir(path):
                f = drive.CreateFile({'title': x})
                f.SetContentFile(os.path.join(path, x))
                f.Upload()
                print('File uploaded: ' + x)

                # Debido a un error conocido en pydrive, si no vaciamos la variable utilizada para subir los archivos a
                # Google Drive, el archivo permanece abierto en la memoria y provoca una fuga de memoria, evitando así su eliminacion.
                f = None
            print('Archivos subidos a Drive con exito!!')
            input('Presiones cualquier tecla para finalizar...')
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    connObj = Connection()
    server = connObj.get_conn()
    connObj.upload_files(server)
