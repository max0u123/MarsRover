import socket

def main():
    # Crée un socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connexion au serveur
    client_socket.connect(("localhost", 8000))
    
    while True:
        # Saisie de la commande
        command = input("Entrez une commande pour le rover (avancer, reculer, gauche, droite, dodo): ")
        
        # Envoie de la commande au serveur
        client_socket.send(command.encode())
        
        # Réception de la réponse du serveur
        response = client_socket.recv(1024).decode()
        print(response)
        
        # Condition de sortie
        if command.lower() == 'quit':
            break
    
    # Fermeture du socket client
    client_socket.close()

if __name__ == "__main__":
    main()