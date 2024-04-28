class CommandInterpreter:
    def __init__(self, rover):
        self.rover = rover

    def execute_command(self, command):
        if command == 'F':
            self.rover.avancer()
        elif command == 'B':
            self.rover.reculer()
        elif command == 'L':
            self.rover.tourner_gauche()
        elif command == 'R':
            self.rover.tourner_droite()
