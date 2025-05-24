
# from .enum import Enum


class Color:
    """
    A class to represent colors in RGB(A) format.
    """

    def __init__(self, red: int, green: int, blue: int, alpha: float = 1):
        """
        Initialize the color with red, green, blue, and alpha values.
        """
        if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
            raise ValueError("RGB values must be between 0 and 255.")
        if not (0 <= alpha <= 1):
            raise ValueError("Alpha value must be between 0 and 1.")

        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    
    def ac_rgb(self):
        """
        Converts the RGB parts of the color to the format used by the AC.
        """
        return self.red / 255, self.green / 255, self.blue / 255
    
    def ac_rgba(self):
        """
        Converts the RGBA parts of the color to the format used by the AC.
        """
        return self.red / 255, self.green / 255, self.blue / 255, self.alpha


