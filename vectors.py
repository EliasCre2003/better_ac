class Vector3D:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, structure = None):
        if structure is None:
            self.x = x
            self.y = y
            self.z = z
        else:
            self.x = structure[0]
            self.y = structure[1]
            self.z = structure[2]

    def __str__(self):
        return "({:.2f}, {:.2f}, {:.2f})".format(self.x, self.y, self.z)
    
    def __repr__(self):
        return str(self)
    

class Vector4D:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, w: float = 0, structure = None):
        if structure is None:
            self.x = x
            self.y = y
            self.z = z
            self.w = w
        else:
            self.x = structure[0]
            self.y = structure[1]
            self.z = structure[2]
            self.w = structure[3]

    def __str__(self):
        return "({:.2f}, {:.2f}, {:.2f}, {:.2f})".format(self.x, self.y, self.z, self.w)
    
    def __repr__(self):
        return str(self)