class Canvas:
    """A canvas can store shapes and render them to the screen.

    Attributes:
        -elements(list): A list of shapes and other elements added to the canvas.
        -width(int): The width of the canvas
        -height(int): The height of the canvas
    """
    
    def __init__(self, width = 10, height = 10):
        """Initialize a canvas
        Return: None
        """

        self.elements = []
        self.width = width
        self.height = height

    def add(self, shape):
        """Add a shape to the canvas.

        Arguments:
            -shape(Shape):The shape to add to the canvas.

        Return: None
        """
        self.elements.append(shape)
    
    def clear(self):
        """Clear all shapes from the canvas."""

        self.elements = []

    def render(self):
        """Render the contents of the canvas.

        Contents are rendered to standard output."""

        for y in range(0, self.height):
            for x in range(0, self.width):
                char = self.get_character_for_cell(x,y)
                print(char,end="  ")
            print('\n')
    
    def get_character_for_cell(self, x, y):
        """Get character that should be rendered in cell"""

        char = '.'
        for shape in self.elements:
            if shape.covering_pixel(x,y):
                char = shape.fill_char
        return char

class Shape:
    """An abstract class that all shapes should inherit from."""

    def covering_pixel(self, x, y):
        return False

    def set_fill_char(self,char):
        """Update the fill character.

        Arguments:
        -char(str): The new fill char.

        Return:
        None
        """
        self.fill_char = char

class Rectangle(Shape):
    """A rectangle."""

    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        """Initialize a rectangle.

        Arguments:
        -start_x(int): The x coordinate for the top left corner of the rect.
        -start_y(int): The y coordinate for the top left corner of the rect.
        -end_x(int): The x coordinate for the bottom right corner of rect.
        -end_y(int): The y coordinate for the bottom right corner of the rect.
        -fill_char(str): The character used to fill the rect.

        Return:
        None
        """

        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char

    def covering_pixel(self, x, y):
        return x >= self.start_x and x <= self.end_x and y >= self.start_y and y <= self.end_y


    def translate(self, axis, num):
        """Translate the rectangle.

        Arguments: 
        -axis(str): Either 'x' or 'y'
        -num(int): A positive or negative integer

        Return:
            None
        """

        if axis == 'x':
            self.start_x = self.start_x + num
            self.end_x = self.end_x + num
        elif axis == 'y':
            self.start_y = self.start_y + num
            self.end_y = self.end_y + num
        