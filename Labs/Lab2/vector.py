class Vector:
    """
    Vector class used to store coordinates of position and velocity.
    """

    def __init__(self, x, y, z):
        """
        constructs the x,y and z coordinates.
        :param x: int
        :param y: int
        :param z: int
        """
        self.x_coordinate = x
        self.y_coordinate = y
        self.z_coordinate = z

    def add(self, vector) -> None:
        """
        adds the vector passed to the coordinates.
        :param vector: tuple
        """
        vec = list(vector)
        self.x_coordinate += vec[0]
        self.y_coordinate += vec[1]
        self.z_coordinate += vec[2]

    def get_xCoord(self):
        """
        gets the x coordinate.
        :return: x_coordinate
        """
        return self.x_coordinate

    def get_yCoord(self):
        """
        gets the y coordinate.
        :return: y_coordinate
        """
        return self.y_coordinate

    def get_zCoord(self):
        """
        gets the z coordinate.
        :return: z_coordinate
        """
        return self.z_coordinate

    def set_xCoord(self, x_coord) -> None:
        """
        sets the x coordinate.
        :param x_coord: int
        """
        self.x_coordinate = x_coord

    def set_yCoord(self, y_coord) -> None:
        """
        sets the y coordinate.
        :param y_coord: int
        """
        self.y_coordinate = y_coord

    def set_zCoord(self, z_coord) -> None:
        """
        sets the z coordinate.
        :param z_coord: int
        """
        self.z_coordinate = z_coord

    def to_tuple(self):
        """
        makes the Vector type to tuple.
        :return: vectors
        """
        vectors = (self.get_xCoord(), self.get_yCoord(), self.get_zCoord())
        return vectors

    def __str__(self):
        """
        string representation of the class.
        :return: self.to_tuple()
        """
        print(self.to_tuple())







