import socket

def send_file(filename):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9999))

    #odeslání názvu souboru
    print(f"Odesílám název souboru: {filename}")
    client.send(filename.encode())

    #čtení v binárním režimu
    with open(filename, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client.send(data)

    response = client.recv(1024)
    print(response.decode())
    client.close()

if __name__ == '__main__':
    filename = input('Zadej název souboru pro odeslání: ')
    send_file(filename)