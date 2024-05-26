import socket
from palindromo_capicua import Cliserv

puerto_utilizado= "puerto_utilizado.txt"

def guardar_puerto_utilizado(puerto):
    with open(puerto_utilizado, "w") as file:
        file.write(str(puerto))

def obtener_puerto_guardado():
    try:
        with open(puerto_utilizado, "r") as file:
            puerto = file.read().strip()
            return puerto
    except FileNotFoundError:
        return None

##def validar_ip(direccion):
    partes = direccion.split('.')
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit() or not 0 <= int(parte) <= 255:
            return False
    return True
###
def procesar_peticion(peticion):
    devuelve = Cliserv()
    peticion = peticion.strip()
    if len(peticion) == 1:  # Si es solo un carácter
        if peticion.isdigit():
            respuesta = "NO CAPICUA"
        else:
            respuesta = "NO PALINDROMO"
    elif peticion.isdigit():  # Si es solo un número
        if devuelve.esCapicua(peticion):
            respuesta = "SI capicua"
        else:
            respuesta = "NO capicua"
    else:  # Si es una cadena de texto o una secuencia de números
        if devuelve.esPalindromo(peticion.lower().replace(" ", "")):
            respuesta = "SI palindromo"
        else:
            respuesta = "NO palindromo"
    return respuesta

def main():
    ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reutilizar la dirección y el puerto
    
    dir_socket = input("Introduce la dirección del servidor (por defecto '127.0.0.1'): ").strip()
    if not dir_socket:
        dir_socket = '127.0.0.1'
    ###elif not validar_ip(dir_socket):
      ##  print("Dirección IP no válida. Usando dirección por defecto '127.0.0.1'.")
       ## dir_socket = '127.0.0.1'
    
    puerto = obtener_puerto_guardado() or 16015
    puerto_input = input(f"Introduce el puerto del servidor (por defecto {puerto}): ").strip()
    if puerto_input:
        try:
            puerto = int(puerto_input)
            print("El puerto debe estar en el rango 0-65535. Usando puerto por defecto.")
            puerto = 16015
        except ValueError:
            print("Puerto no válido. Usando puerto por defecto.")
            puerto = 16015

    try:
        ss.bind((dir_socket, puerto))
        print(f"El servidor está escuchando conexiones UDP en {dir_socket} : {puerto}")
        guardar_puerto_utilizado(puerto)  # Guardar el puerto en el archivo
    except Exception as e:
        print(f"Error al asignar una dirección al servidor: {e}")
        return

    while True:
        data, dirc = ss.recvfrom(1024)
        peticion = data.decode('utf8')
        respuesta = procesar_peticion(peticion)
        ss.sendto(respuesta.encode('utf8'), dirc)

    ss.close()

if __name__ == "__main__":
    main()
