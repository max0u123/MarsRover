import pytest
import asyncio
from unittest.mock import Mock, patch
from src.websocket_implementation import WebSocketImplementation
from src.models import Point, Orientation
from src.rover import Rover

@pytest.mark.asyncio
@patch('websockets.serve')
@patch('websockets.WebSocketServerProtocol')
async def test_websocket_receives_message(mocked_ws, mocked_server):
    rover = Rover(Point(0, 0), Orientation.NORTH, (10, 10))
    websocket = WebSocketImplementation(rover)

    mocked_server.return_value = asyncio.Future()
    mocked_server.return_value.set_result(None)

    mocked_ws.recv.return_value = asyncio.Future()
    mocked_ws.recv.return_value.set_result("Command")
    mocked_ws.send = Mock()

    await websocket.start_server('localhost', 8765)

    mocked_ws.recv.assert_called_once()
    mocked_ws.send.assert_called_with("Command processed")