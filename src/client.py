import socket

HOST = '127.0.0.1'
PORT = 5001

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print("Conectado al servidor.")

        while True:
            message = input("Escribe un mensaje (o 'DESCONEXION' para salir): ")
            client_socket.sendall(message.encode("utf-8"))

            if message.upper() == "DESCONEXION":
                print("Desconectando del servidor.")
                break

            response = client_socket.recv(1024)
            print("Respuesta del servidor:", response.decode("utf-8"))

if __name__ == '__main__':
    start_client()
