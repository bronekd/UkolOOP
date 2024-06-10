
import socket
import threading
import os

def handle_client(client_socket):
    try:
        filename = ""
        #příjme název souboru od clienta
        while "::END::" not in filename:
            filename += client_socket.recv(1024).decode()

        filename = filename.replace("::END::", "")

        #rozdělení názvu
        base, ext = os.path.splitext(filename)
        new_filename = f"{base}_prijato{ext}"

        print(f"Received {new_filename}")

        with open(new_filename, "wb") as f:
            #data = "b"
            while True:
                #příjme data od klienta
                chunk = client_socket.recv(1024)
                if not chunk:
                    break
                if b"::END_DATA::" in chunk:
                    data += chunk.replace(b"::END_DATA::", b"")
                    f.write(data)
                    break
                f.write(chunk)

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


