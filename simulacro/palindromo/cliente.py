import socket
import sys
from palindromo_capicua import Cliserv

def main():
    sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dir_socket = input("Introduzca la dirección del servidor (recuerde 127.0.0.1): ") 
    puerto = input("Introduzca el puerto del servidor(recurde 16015): ")
    if not dir_socket:
        dir_socket = 'localhost'
    if not puerto:
        puerto = '16015'

    devuelve = Cliserv()
    peticion = devuelve.pide()
    sc.sendto(peticion.encode('utf8'), (dir_socket, int(puerto)))

    data, _ = sc.recvfrom(1024)
    sys.stdout.write(data.decode('utf8').strip()) 
    print("\n")
    sc.close()

if __name__ == "__main__":
    main()
