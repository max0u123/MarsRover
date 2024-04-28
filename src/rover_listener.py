
from command_interpreter import CommandInterpreter

class RoverListener:
    def __init__(self, rover, iface):
        self.rover = rover
        self.iface = iface
        self.command_interpreter = CommandInterpreter(rover)

    async def listen_to_commands(self):
        print("Starting to listen to commands via WebSocket.")
        await self.iface.start_server()

    def process_command(self, command):
        print(f"Processing command: {command}")
        self.command_interpreter.execute_command(command)
