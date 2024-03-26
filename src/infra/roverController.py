import asyncio
import websockets
from domain.rover import Rover
from domain.map import Map
from utils.printing import print_with_timestamp

class RoverController:
    def __init__(self):
        self.map = None
        self.rover = None

    async def async_input(self):
        """
        Obtient une entrée de l'utilisateur de manière asynchrone.
        """
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, input)

    async def handle_command(self, websocket, path):
        print_with_timestamp("Le programme de contrôle du rover a démarré.")
        try:
            while True:
                command = await websocket.recv()
                command = command.strip()
                print_with_timestamp(f"Command received from client: {command}")

                if command == 'avancer':
                    if not self.rover._check_collision(*self.rover._next_position(1)):
                        self.rover.avancer()
                        print_with_timestamp(f"Position actuelle du rover : {self.rover.obtenir_etat()}")
                        continue
                    else:
                        await websocket.send("Déplacement impossible car obstacle. Réessayez.")
                        continue
                elif command == 'reculer':
                    if not self.rover._check_collision(*self.rover._next_position(-1)):
                        self.rover.reculer()
                        print_with_timestamp(f"Position actuelle du rover : {self.rover.obtenir_etat()}")
                        continue
                    else:
                        await websocket.send("Déplacement impossible car obstacle. Réessayez.")
                        continue
                elif command == 'gauche':
                    self.rover.tourner_gauche()
                    print_with_timestamp(f"Position actuelle du rover : {self.rover.obtenir_etat()}")
                    continue
                elif command == 'droite':
                    self.rover.tourner_droite()
                    print_with_timestamp(f"Position actuelle du rover : {self.rover.obtenir_etat()}")
                    continue
                else:
                    print_with_timestamp(f"Mauvaise commande insérée par le client! {command}")
                    continue


        except websockets.ConnectionClosed:
            print_with_timestamp("Connexion WebSocket fermée.")


    async def run(self):
        await self.create_map()
        await self.create_rover()

        async with websockets.serve(self.handle_command, "localhost", 8765):
            await asyncio.Future()

    async def create_map(self):
        try:
            print_with_timestamp("Entrez la largeur de la carte : ")
            width = int(await self.async_input())
            print_with_timestamp("Entrez la hauteur de la carte : ")
            height = int(await self.async_input())
            print_with_timestamp("Entrez le nombre d'obstacles : ")
            num_obstacles = int(await self.async_input())
            if width <= 0 or height <= 0 or num_obstacles < 0:
                raise ValueError
        except ValueError:
            print_with_timestamp("Les valeurs entrées ne sont pas valides. Veuillez entrer des entiers positifs.")
            exit(1)

        self.map = Map(width, height)
        self.map.obstacles = self.map.generate_obstacles(num_obstacles)

    async def create_rover(self):
        """
        Crée un nouveau rover en demandant à l'utilisateur d'entrer les coordonnées et l'orientation.
        """
        try:
            print_with_timestamp("Entrez la coordonnée x du rover : ")
            x = float(await self.async_input())
            print_with_timestamp("Entrez la coordonnée y du rover : ")
            y = float(await self.async_input())
        except ValueError:
            print_with_timestamp("La valeur entrée n'est pas valide. Veuillez entrer un nombre.")
            exit(1)

        print_with_timestamp("Entrez l'orientation du rover (N, S, E ou O) : ")
        orientation = (await self.async_input()).upper()

        while orientation not in ['N', 'S', 'E', 'O']:
            print_with_timestamp("L'orientation entrée n'est pas valide. Veuillez entrer N, S, E ou O.")
            print_with_timestamp("Entrez l'orientation du rover (N, S, E ou O) : ")
            orientation = (await self.async_input()).upper()
        print_with_timestamp(f"En attente du lancement client ...")
            

        self.rover = Rover(x, y, orientation, obstacles=self.map.obstacles, map=self.map)
