import asyncio
from infra.roverController import RoverController

if __name__ == "__main__":
    controller = RoverController()
    asyncio.run(controller.run())
