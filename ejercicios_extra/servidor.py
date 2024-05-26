import socket
from KataRomanos import KataRomanos

p1 = KataRomanos()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 2227)
print('Estableciendo conexión con {} en el puerto {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print("Conexión establecida con:", client_address)
        while True:
            data = connection.recv(1024)
            if not data:
                break
            decodeData = data.decode("utf8")
            print("Datos recibidos:", decodeData)

            def es_numero_romano(decodeData):
                simbolos_romanos = ["I", "V", "X", "L", "C", "D", "M"]
                for caracter in decodeData:
                    if caracter not in simbolos_romanos:
                        return False
                return True
            
            def contiene_numeros_y_letras(decodeData):
                contiene_letras = False
                contiene_numeros = False
                for caracter in decodeData:
                    if caracter.isalpha():
                        contiene_letras = True
                    elif caracter.isdigit():
                        contiene_numeros = True
                return contiene_letras and contiene_numeros

            if contiene_numeros_y_letras(decodeData):
                mensaje = "ERROR"
                connection.sendall(mensaje.encode("utf8"))
                break
            elif decodeData.isdigit():
                numero_entero = int(decodeData)
                numero_traducido = p1.entero_a_romano(numero_entero)
                numero_convertido_en_cadena = str(numero_traducido)
                numero_binario = numero_convertido_en_cadena.encode("utf8")
                connection.sendall(numero_binario)
            elif es_numero_romano(decodeData):  # Llamada a la función es_numero_romano
                romanoConvertidoEntero = p1.romano_a_entero(decodeData)
                entero_string = str(romanoConvertidoEntero)
                entero_bytes = entero_string.encode("utf8")
                connection.sendall(entero_bytes)

    finally:
        connection.close()

