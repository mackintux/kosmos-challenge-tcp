import socket

HOST = '127.0.0.1'
PORT = 5001

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f'Waiting for a connection from {HOST}:{PORT}')

        while True:
            conn, addr = server_socket.accept()

            with conn:
                print(f'Connected by: {addr}')

                while True:
                    data = conn.recv(1024)

                    if not data:
                        break

                    message = data.decode("utf-8").strip()
                    print(f'Message Received: {message}')

                    if message.upper() == "DESCONEXION":
                        print("Closing connection with client.")
                        conn.sendall("CLOSING CONNECTION".encode("utf-8"))
                        break
                    else:
                        response = message.upper()
                        conn.sendall(response.encode("utf-8"))
                        print(f'Response Sent: {response}')

if __name__ == '__main__':
    start_server()
