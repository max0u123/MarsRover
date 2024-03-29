##################################################
#import asyncio
#import websockets
#
#async def send_commands():
#    uri = "ws://localhost:8765"
#    async with websockets.connect(uri) as websocket:
#        print("Connexion établie avec le serveur. Vous pouvez commencer à envoyer des commandes.")
#        while True:
#            command = input("------------------------------------------------------------\n Entrez une commande (avancer, reculer, gauche, droite, quitter): ")
#            try:
#                await websocket.send(command)
#                await process_response(websocket, command)
#            except websockets.exceptions.WebSocketException as e:
#                print(f"Erreur lors de l'envoi de la commande: {e}")
#            if command == 'quitter':
#                break
#
#async def process_response(websocket, command):
#    response = await websocket.recv()
#    print(f"Réponse du serveur: {response}")
#
#asyncio.run(send_commands())
##################################################
# Après DDD : 
# On a organisé le code autour de Rover et on a bien identifier chaque méthode de Rover.

import asyncio
import websockets

class RoverClient:
    def __init__(self, uri):
        self.uri = uri

    async def connect_to_server(self):
        self.websocket = await websockets.connect(self.uri)
        print("Connexion établie avec le serveur. Vous pouvez commencer à envoyer des commandes.")

    async def send_command(self, command):
        try:
            await self.websocket.send(command)
            await self.process_response()
        except websockets.exceptions.WebSocketException as e:
            print(f"Erreur lors de l'envoi de la commande: {e}")

    async def process_response(self):
        response = await self.websocket.recv()
        print(f"Réponse du serveur: {response}")

    async def close_connection(self):
        await self.websocket.close()

async def send_commands(rover_client):
    while True:
        command = input("------------------------------------------------------------\n Entrez une commande (avancer, reculer, gauche, droite, quitter): ")
        if command == 'quitter':
            await rover_client.close_connection()
            break
        await rover_client.send_command(command)

async def main():
    uri = "ws://localhost:8765"
    rover_client = RoverClient(uri)
    await rover_client.connect_to_server()
    await send_commands(rover_client)

asyncio.run(main())
