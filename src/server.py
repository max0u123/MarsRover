import socket
from infra.roverController import RoverController

def handle_client(client_socket, rover_controller):
    while True:
        command = client_socket.recv(1024).decode()
        if not command:
            break
        rover_controller.execute_command(command)
        client_socket.send("Commande reçue et exécutée".encode())

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5555))
    server_socket.listen(5)
    print("Serveur en attente de connexions...")

    (client_socket, address) = server_socket.accept()
    print(f"Connexion établie avec {address}")

    rover_controller = RoverController()
    rover_controller.run()

    handle_client(client_socket, rover_controller)
    client_socket.close()
