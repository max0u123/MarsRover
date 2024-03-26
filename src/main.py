import threading
import subprocess
from infra.roverController import RoverController

def start_server():
    controller = RoverController()
    controller.run()

def start_client():
    # Exemple de démarrage du client (ici, on lance client.py comme un processus séparé)
    subprocess.run(["python", "./infra/client.py"])

if __name__ == "__main__":
    # Démarrer le serveur dans un thread
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # Démarrer le client (peut être exécuté depuis ici ou importé depuis un autre fichier)
    start_client()

    # Attendre que le serveur se termine (optionnel)
    # server_thread.join()
