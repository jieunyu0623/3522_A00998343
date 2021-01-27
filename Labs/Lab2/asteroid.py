from Labs.Lab2.vector import Vector


class Asteroid:
    """
    Asteroid class used to make a bunch of rocks (Asteroids) in the space.
    """

    id = 0

    def __init__(self, circumference_in_metres: int, position: Vector, velocity: Vector):
        """
        constructs the circumference, position and the velocity of the Asteroid object.
        :param circumference_in_metres: int
        :param position: Vector
        :param velocity: Vector
        """
        self.circumference = circumference_in_metres
        self.position = position
        self.velocity = velocity
        self.id = self.create_id()

    @staticmethod
    def create_id():
        """
        gives an unique id for each asteroid object created.
        :return: Asteroid.id
        """
        Asteroid.id += 1
        return Asteroid.id

    def get_circumference(self) -> float:
        """
        gets the circumference of the Asteroid object.
        :return: circumference
        """
        return self.circumference

    def get_position(self):
        """
        gets the position of the Asteroid object.
        :return: position
        """
        return self.position

    def get_velocity(self):
        """
        gets the velocity of the Asteroid object.
        :return: velocity
        """
        return self.velocity

    def get_id(self):
        """
        gets the unique id of the Asteroid object.
        :return: id
        """
        return self.id

    def set_circumference(self, circumference) -> None:
        """
        sets the circumference of the Asteroid object.
        :param circumference: int
        """
        self.circumference = circumference

    def set_position(self, position) -> None:
        """
        sets the position of the Asteroid object.
        :param position: Vector
        """
        new_pos = list(position)
        pos = list(self.position)
        pos[0] = new_pos[0]
        pos[1] = new_pos[1]
        pos[2] = new_pos[2]
        self.position = tuple(pos)

    def set_velocity(self, velocity) -> None:
        """
        sets the velocity of the Asteroid object.
        :param velocity: Vector
        """
        new_vel = list(velocity)
        vel = list(self.velocity)
        vel[0] = new_vel[0]
        vel[1] = new_vel[1]
        vel[2] = new_vel[2]
        self.velocity = tuple(vel)

    def move(self):
        """
        moves the Asteroid object with velocity.
        :return: position
        """
        pos = self.get_position()
        x_coord = pos.get_xCoord()
        y_coord = pos.get_yCoord()
        z_coord = pos.get_zCoord()
        velocity = self.get_velocity()
        pos.set_xCoord(x_coord + velocity.get_xCoord())
        pos.set_yCoord(y_coord + velocity.get_yCoord())
        pos.set_zCoord(z_coord + velocity.get_zCoord())
        return self.position

    def __str__(self):
        """
        string representation of an Asteroid object.
        :return: string
        """
        return f'Asteroid id: {self.id}  position: {self.position.to_tuple()} ' \
               f'circumference: {self.circumference}  velocity: {self.velocity.to_tuple()}'

