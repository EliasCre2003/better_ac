import ac

class Font:
    def __init__(self, 
        name: str = None, 
        italic: bool = False, 
        bold: bool = False
    ):
        self.name = name
        self.italic = italic
        self.bold = bold

        self.initialized = False
        if name is None: return
        if ac.initFont(0, name, 1 if italic else 0, 1 if bold else 0) == -1:
            raise ValueError("Font '{}' not found.".format(name))
        self.initialized = True
    

class FontAlignment:
    """
    An enum-like class that stores all the font alignment modes.
    """
    def __init__(self, name: str):
        self.name = name


FontAlignment.LEFT = FontAlignment("left")
FontAlignment.RIGHT = FontAlignment("right")
FontAlignment.CENTER = FontAlignment("center")