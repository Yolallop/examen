import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dirServer = input("Introduce la dirección del servidor: ")
server_address = (dirServer, 2227)
sock.connect(server_address)

queQuiereElCliente = input("Introduce el número que deseas traducir: ")

try:
    solicitudEnBytes = queQuiereElCliente.encode("utf8")
    sock.sendall(solicitudEnBytes)

    data = sock.recv(1024)
    while data:
        print("Respuesta del servidor:", data.decode("utf8"))
        data = sock.recv(1024)

finally:
    time.sleep(1)
    print('\nCerrando socket...')
    sock.close()

