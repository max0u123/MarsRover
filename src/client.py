import asyncio
import websockets

async def send_commands():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("Connexion établie avec le serveur. Vous pouvez commencer à envoyer des commandes.")
        while True:
            command = input("Entrez une commande (avancer, reculer, gauche, droite) : ")
            await websocket.send(command)
            if command == 'exit':  # Marqueur spécial pour terminer les commandes
                break

asyncio.run(send_commands())
