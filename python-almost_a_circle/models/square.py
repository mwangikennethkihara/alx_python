'''
Square Module - Contains the Square class that inherits from Rectangle
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    A class Square inherits from class Rectangle
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initialize a new Square instance

        Args:
            size (int): The size of the square's sides
            x (int): The x coordinate of the top left corner
            y (int): The y coordinate of the top left corner
            id (int): The id of the square
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for wsize."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns the string representation of the Square instance

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
