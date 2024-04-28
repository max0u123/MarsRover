# src/websocket_implementation.py

import asyncio

class WebSocketImplementation:
    def __init__(self, rover):
        self.rover = rover

    async def start_server(self, host, port):
        server = await asyncio.start_server(
            self.handle_client_connection, host, port)
        async with server:
            await server.serve_forever()

    async def handle_client_connection(self, reader, writer):
        print("WebSocket server started.")

        while True:
            data = await reader.read(100)
            message = data.decode()
            addr = writer.get_extra_info('peername')

            print(f"Received {message} from {addr}")

            if message == "AVANCER":
                self.rover.avancer()
            elif message == "RECULER":
                self.rover.reculer()
            elif message == "GAUCHE":
                self.rover.tourner_gauche()
            elif message == "DROITE":
                self.rover.tourner_droite()

            print(f"Rover position: {self.rover.position}, orientation: {self.rover.orientation}")

            response = "Message received"
            writer.write(response.encode())
            await writer.drain()
