import asyncio
import websockets

async def send_commands():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("Connexion établie avec le serveur. Vous pouvez commencer à envoyer des commandes.")
        while True:
            command = input("------------------------------------------------------------\n Entrez une commande (avancer, reculer, gauche, droite, quitter): ")
            try:
                await websocket.send(command)
                await process_response(websocket, command)
            except websockets.exceptions.WebSocketException as e:
                print(f"Erreur lors de l'envoi de la commande: {e}")
            if command == 'quitter':
                break

async def process_response(websocket, command):
    response = await websocket.recv()
    print(f"Réponse du serveur: {response}")

asyncio.run(send_commands())