import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 12345
# Creamos el socket
c = socket.socket()
#Nos conectamos al servidor
c.connect((SERVER_ADDRESS, SERVER_PORT))

# Comenzamos a enviar información al servidor desde nuestro teclado
try:
    input = raw_input
except NameError:
    pass

print("Conectado al servidor: " + str((SERVER_ADDRESS, SERVER_PORT)))
while True:
    try:
        data = input("Digite mensaje:  ")
    except EOFError:
        print("\nBien, chao")
        break

    if not data:
        print("No se puede enviar datos vacíos!")
        print("Ctrl-D [or Ctrl-Z en Windows] para salir")
        continue

# Convertimoslos datos en bytes. (solo para Python 3)
    data = data.encode()

# Enviamos
    c.send(data)

# Recibimos respuesta desde el servidor
    data = c.recv(2048)
    if not data:
        print("Server abended. Exiting")
        break

# Convertimos la respuesta en un string
    data = data.decode()

    print("Got this string from server:")
    print(data + '\n')

c.close()
