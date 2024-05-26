# Cliente-Servidor de Palíndromos y Números Capicúa

En este directorio se encuentran los archivos que conforman la solución al sistema cliente-servidor para verificar si una cadena de texto es un palíndromo y si un número es capicúa.

## Sobre el Proyecto

Este proyecto consiste en un sistema cliente-servidor que utiliza sockets UDP de Internet para proporcionar información sobre si una cadena de texto es un palíndromo y si un número es capicúa.

## Punto de Escucha del Servidor

El servidor escucha las peticiones en el puerto UDP número 16013.

## Aplicación: Cliente-Servidor de Palíndromos y Números Capicúa

El sistema cliente-servidor tiene las siguientes características:

1. **Servidor UDP:**
   - Atiende peticiones en el puerto UDP número 16013.
   - Responde a los mensajes enviados desde el cliente con información sobre si la cadena de texto introducida es un palíndromo y si el número introducido es capicúa.

## Herramientas

Para ejecutar esta aplicación se necesita:

- Un sistema operativo Unix compatible (como Linux o macOS).
- Python 3.x instalado en el sistema.

## Cómo Ejecutar la Aplicación

### Ejecutar el Servidor

Para ejecutar el servidor, utiliza el siguiente comando:

python3 servidor.py


### Ejecutar el Cliente 

pytest cliserv.py

### Ejecutar los test 

pytest cliserv.py



