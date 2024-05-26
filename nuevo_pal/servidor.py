import socket
import os
import sys
from Kata import Kata

p1 = Kata()
bufferSize = 4096
puerto_utilizado_archivo = "numero_puerto.txt"  # Nombre del archivo para guardar el puerto utilizado

def guardar_puerto_utilizado(puerto):
    with open(puerto_utilizado_archivo, "w") as file:
        file.write(str(puerto))

def obtener_puerto_guardado():
    try:
        with open(puerto_utilizado_archivo, "r") as file:
            puerto = int(file.read().strip())  # Leer el número de puerto del archivo y convertirlo a entero
            return puerto
    except FileNotFoundError:
        return None

def server(server_address, server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((server_address, server_port))
    s.listen(2)  # backlog

    print("Escuchando ...")

    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        child_pid = os.fork()
        if child_pid == 0:
            try:
                nombre_fichero = conn.recv(1024).decode("utf-8").strip()
                with open(nombre_fichero, "rb") as file:
                    data = file.read(bufferSize)
                    while data:
                        palabras = data.split()
                        palindromos = [palabra for palabra in palabras if p1.esPalindromo(palabra.decode("utf-8"))]
                        vocales = sum(p1.esVocal(palabra.decode("utf-8")) for palabra in palabras)
                        print("Palíndromos encontrados:", palindromos)
                        print("Número de vocales:", vocales)
                        for palindromo in palindromos:
                            conn.sendall(palindromo + b'\n')
                        conn.sendall(str(vocales).encode("utf8") + b'\n')
                        data = file.read(bufferSize)
                conn.sendall(b"fin_de_fichero\n")
            except FileNotFoundError:
                conn.sendall("Error al abrir el fichero\n".encode('utf-8'))
            finally:
                conn.close()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        address = "0.0.0.0"
        puerto = obtener_puerto_guardado() or 5130 # Obtener el número de puerto del archivo o usar 5150 por defecto
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        puerto = int(sys.argv[2])
    else:
        print("Error en los argumentos")
        exit(1)

    server(address, puerto)
