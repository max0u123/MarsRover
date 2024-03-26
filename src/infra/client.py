import socket

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5555))

    while True:
        command = input("Entrez une commande pour le rover: ")
        client_socket.send(command.encode())
        response = client_socket.recv(1024).decode()
        print("Réponse du serveur:", response)

    client_socket.close()
