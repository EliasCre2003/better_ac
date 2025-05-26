import ac
import acsys

from .vectors import Vector2D
from .better_ac import log


GL_LINES = 0
GL_LINES_STRIP = 1
GL_TRIANGLES = 2
GL_QUADS = 3


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


class Texture:
    """
    A class to handle textures in Assetto Corsa.
    """
    def __init__(self, path: str):
        self.path = path
        self.texture_id = ac.newTexture(path)


class Vertex:
    def __init__(self, x: float, y: float, color: Color):
        """
        Initialize a vertex with x, y coordinates and a color.
        
        :param x: The x-coordinate of the vertex.
        :param y: The y-coordinate of the vertex.
        :param color: A Color object representing the color of the vertex.
        """
        self.x = x
        self.y = y
        self.color = color

    def vector(self) -> Vector2D:
        """
        Returns a Vector2D representation of the vertex, i.e., only the x and y coordinates.
        """
        return Vector2D(self.x, self.y)


class Drawable:
    """
    A base class for drawable objects.
    """
    def draw(self):
        """
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the draw method.")



class Line(Drawable):
    """
    A class to represent a line that can be drawn.
    """
    def __init__(self, start: Vertex, end: Vertex):
        self.start = start
        self.end = end

    def draw(self):
        ac.glBegin(GL_LINES)
        ac.glColor4f(*self.start.color.ac_rgba())
        ac.glVertex2f(self.start.x, self.start.y)
        ac.glColor4f(*self.end.color.ac_rgba())
        ac.glVertex2f(self.end.x, self.end.y)
        ac.glEnd()


class Triangle(Drawable):
    def __init__(self, v1: Vertex, v2: Vertex, v3: Vertex):
        """
        Initialize a triangle with three vertices.
        
        :param v1: The first vertex of the triangle.
        :param v2: The second vertex of the triangle.
        :param v3: The third vertex of the triangle.
        """
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def is_inside(self, point: Vector2D) -> bool:
        """
        Check if a point is inside the triangle using barycentric coordinates.
        
        :param point: A Vector2D object representing the point to check.
        :return: True if the point is inside the triangle, False otherwise.
        """
        b1 = Triangle._sign(point, self.v1.vector(), self.v2.vector()) < 0
        b2 = Triangle._sign(point, self.v2.vector(), self.v3.vector()) < 0
        b3 = Triangle._sign(point, self.v3.vector(), self.v1.vector()) < 0
        return b1 == b2 == b3
    
    @staticmethod
    def _sign(v1: Vector2D, v2: Vector2D, v3: Vector2D) -> float:
        return (v2.x - v1.x) * (v3.y - v1.y) - (v2.y - v1.y) * (v3.x - v1.x)
    
    def sign(self) -> float:
        """
        Calculate the signed area of the triangle formed by the vertices.
        """
        return Triangle._sign(self.v1.vector(), self.v2.vector(), self.v3.vector())

    def is_convex(self) -> bool:
        """
        Check if the triangle is convex by evaluating the sign of the area.
        """
        return self.sign() < 0
    
    def draw(self):
        """
        Draw the triangle using OpenGL.
        """
        ac.glBegin(GL_TRIANGLES)
        ac.glColor4f(*self.v1.color.ac_rgba())
        ac.glVertex2f(self.v1.x, self.v1.y)
        ac.glColor4f(*self.v2.color.ac_rgba())
        ac.glVertex2f(self.v2.x, self.v2.y)
        ac.glColor4f(*self.v3.color.ac_rgba())
        ac.glVertex2f(self.v3.x, self.v3.y)
        ac.glEnd()


class Shape(Drawable):
    """A base class for shapes that can be drawn."""
    def __init__(self, vertices, triangles):
        self.vertices = vertices
        self.triangles = triangles

    # DOESN'T REALLY WORK YET
    @staticmethod
    def polygon(points, color: Color) -> 'Shape':
        """
        Create a shape from a list of vertices by converting them into triangles.
        
        :param points: A list of Vector2D objects representing the corners of the polygon.
        :return: A Shape object containing the triangles that make up the polygon.
        """
        if len(points) < 3:
            raise ValueError("A polygon must have at least 3 vertices.")
        triangles = []
        indices = list(range(len(points)))
        i = 0
        while len(indices) > 3:
            if i == len(indices):
                break
            i1 = indices[i-1]
            i2 = indices[i]
            i3 = indices[(i + 1) % len(indices)]
            p1, p2, p3 = points[i1], points[i2], points[i3]
            triangle = Triangle(
                Vector2D(p1.x, p1.y, color), 
                Vector2D(p2.x, p2.y, color),
                Vector2D(p3.x, p3.y, color)
            )
            if not triangle.is_convex():
                i += 1
                continue
            ear_found = True
            for j in indices:
                if j in (i1, i2, i3):
                    continue
                if triangle.is_inside(points[j].vector()):
                    ear_found = False
                    break
            if ear_found:
                triangles.append(triangle)
                indices.pop(i)
                i = 0
            else:
                i += 1
        if len(indices) == 3:
            p1, p2, p3 = [points[i] for i in indices]
            triangles.append(
                triangle = Triangle(
                    Vector2D(p1.x, p1.y, color), 
                    Vector2D(p2.x, p2.y, color),
                    Vector2D(p3.x, p3.y, color)
                )
            )
        return Shape(points, triangles)

    def draw(self, fill: bool = True):
        """
        Draw the shape by rendering all triangles.
        """
        if fill:
            for triangle in self.triangles:
                triangle.draw()
            return
        ac.glBegin(GL_LINES_STRIP)
        for vertex in self.vertices:
            ac.glColor4f(*vertex.color.ac_rgba())
            ac.glVertex2f(vertex.x, vertex.y)
        ac.glEnd()


class Quad(Drawable):
    """
    A class to represent a quad that can be drawn.
    """
    def __init__(self, x: float, y: float, width: float, height: float, color: Color):
        """
        Initialize a quad with position, size, and color.
        
        :param x: The x-coordinate of the quad's top-left corner.
        :param y: The y-coordinate of the quad's top-left corner.
        :param width: The width of the quad.
        :param height: The height of the quad.
        :param color: A Color object representing the color of the quad.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        ac.glColor4f(*self.color.ac_rgba())
        ac.glQuad(self.x, self.y, self.width, self.height)


class TexturedQuad(Drawable):
    """
    A class to represent a quad with a texture that can be drawn.
    """
    def __init__(self, x: float, y: float, width: float, height: float, texture: Texture):
        """
        Initialize a textured quad with position, size, and texture.
        
        :param x: The x-coordinate of the quad's top-left corner.
        :param y: The y-coordinate of the quad's top-left corner.
        :param width: The width of the quad.
        :param height: The height of the quad.
        :param texture: A Texture object representing the texture to apply to the quad.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.texture = texture

    def draw(self):
        ac.glQuadTextured(self.x, self.y, self.width, self.height, self.texture.texture_id)

