from rover import Rover

def main():
    rover = Rover(0, 0, 'N')

    commands = ['F', 'R', 'F', 'R', 'F', 'R', 'F', 'R']

    for command in commands:
        if command == 'F':
            rover.avancer()
        elif command == 'B':
            rover.reculer()
        elif command == 'L':
            rover.tourner_gauche()
        elif command == 'R':
            rover.tourner_droite()

        print(rover.obtenir_etat())

if __name__ == "__main__":
    main()
