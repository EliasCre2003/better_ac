import ac
import acsys

class Texture:
    """
    A class to handle textures in Assetto Corsa.
    """
    def __init__(self, path: str):
        self.path = path
        self.texture_id = ac.newTexture(path)


def draw_textured_quad(x: float, y: float, width: float, height: float, texture: Texture):
    """
    Draws a textured quad at the specified position and size.
    
    :param x: The x-coordinate of the quad's top-left corner.
    :param y: The y-coordinate of the quad's top-left corner.
    :param width: The width of the quad.
    :param height: The height of the quad.
    :param texture: The Texture object to use for the quad.
    """
    ac.glQuadTextured(x, y, width, height, texture.texture_id)

