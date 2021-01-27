import math
import random
import time
from datetime import datetime

from Labs.Lab2.asteroid import Asteroid
from Labs.Lab2.vector import Vector


class Controller:
    """
    Controller class used to simulate Asteroid random movements.
    """
    asteroid_list = []

    def __init__(self):
        """
        creates 100 asteroid objects.
        """

        for _ in range(100):
            radius = random.randint(1, 4)
            circumference = 2 * math.pi * radius

            x_position = random.randint(0, 100)
            y_position = random.randint(0, 100)
            z_position = random.randint(0, 100)
            position = Vector(x_position, y_position, z_position)

            x_velocity = random.randint(0, 5)
            y_velocity = random.randint(0, 5)
            z_velocity = random.randint(0, 5)
            velocity = Vector(x_velocity, y_velocity, z_velocity)

            asteroid = Asteroid(circumference, position, velocity)
            Controller.asteroid_list.append(asteroid)

    def simulate(self, seconds):
        """
        simulates the randomly generated asteroids movements with random velocity
        and random position.
        :param seconds:
        """
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")
        print('Simulation Start Time: ' + current_time)
        print('')
        print('Moving Asteroids!')
        print('--------------------')

        for asteroid in Controller.asteroid_list:
            position = asteroid.get_position()
            x_coord = position.get_xCoord()
            y_coord = position.get_yCoord()
            z_coord = position.get_zCoord()

            print("Asteroid %d Moved! Old Pos: %s -> New Pos: %s" % (
                asteroid.get_id(), asteroid.get_position().to_tuple(), asteroid.move().to_tuple()))

            new_position = asteroid.get_position()
            new_x_coord = new_position.get_xCoord()
            new_y_coord = new_position.get_yCoord()
            new_z_coord = new_position.get_zCoord()

            x_coord_diff = new_x_coord - x_coord
            y_coord_diff = new_y_coord - y_coord
            z_coord_diff = new_z_coord - z_coord

            coord_diff = (x_coord_diff, y_coord_diff, z_coord_diff)

            print("Asteroid %d is currently at %s and moving "
                  "at %s meters per second. It has a circumference of %f" % (
                      asteroid.get_id(), asteroid.get_position().to_tuple(), coord_diff,
                      asteroid.get_circumference()))

            time.sleep(seconds/100)


def main():
    """
    the main.
    """
    print('running...')


if __name__ == '__main__':
    main()
    c = Controller()
    c.simulate(100)
