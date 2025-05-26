class Sak:
    def __init__(self):
        self.sak = "sak"


    @property
    def sak(self):
        return self._sak
    
    @sak.setter
    def sak(self, value):
        self._sak = value

sak = Sak()

print(sak.sak)  # Output: sak