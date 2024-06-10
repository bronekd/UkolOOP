import socket
import threading
import os

def handle_client(client_socket):
    try:
        #příjme název souboru od clienta
        filename = client_socket.recv(1024).decode()
        if not filename:
            return

        print(f"Received {filename}")

        with open(filename, "wb") as f:
            while True:
                #příjme data od klienta
                #print(f"Ve smyččce {filename} byl úspěšně přijat  ")
                data = client_socket.recv(1024)
                if not data:
                    break
                f.write(data)

        print(f"Soubor {filename} byl úspěšně přijat")
        client_socket.send(b"Transfer successful")
    except Exception as e:
        print(f"Client pri příjmání souboru: {e}")
        client_socket.send(b"Transfer failed")
    finally:
        client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9999))
    server.listen(5)
    print(f"Server naslouchá na portu 9999")

    while True:
        client_socket, addr = server.accept()
        print(f"Připojen Client: {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()