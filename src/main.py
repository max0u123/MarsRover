import asyncio
from rover import Rover
from models import Point, Orientation
from websocket_implementation import WebSocketImplementation
from conf import Config

class MissionControl:
    def __init__(self, rover):
        self.rover = rover
        self.controller = WebSocketImplementation(rover)

    async def run(self):
        try:
            await self.controller.start_server(Config.HOST, Config.PORT)
        except KeyboardInterrupt:
            print("Mission Control shut down")

if __name__ == "__main__":
    rover = Rover(Point(0, 0), Orientation.NORTH, Config.PLANET_SIZE)
    mission_control = MissionControl(rover)
    asyncio.run(mission_control.run())
