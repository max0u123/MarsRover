# tests/test_rover.py

import pytest
from src.models import Point, Orientation
from src.rover import Rover

@pytest.fixture
def setup_rover():
    return Rover(Point(0, 0), Orientation.NORTH, (10, 10))

def test_move_forward(setup_rover):
    setup_rover.avancer()
    assert setup_rover.position.x == 0 and setup_rover.position.y == 1, "Failed to move forward correctly"

def test_move_backward(setup_rover):
    setup_rover.reculer()
    assert setup_rover.position.x == 0 and setup_rover.position.y == 9, "Failed to move backward correctly"

def test_turn_left(setup_rover):
    setup_rover.tourner_gauche()
    assert setup_rover.orientation == Orientation.WEST, "Failed to turn left correctly"

def test_turn_right(setup_rover):
    setup_rover.tourner_droite()
    assert setup_rover.orientation == Orientation.EAST, "Failed to turn right correctly"
