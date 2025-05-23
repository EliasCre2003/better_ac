import ac
import acsys


class _GenericElement:
    def __init__(self, title: str):
        self.object_id = ...

    # def get_id(self) -> int:
    #     """
    #     Get the ID of the element.
    #     """
    #     return self.object_id
    
    def set_size(self, width: float, height: float) -> None:
        """
        Set the size of the element.
        """
        ac.setSize(self.object_id, width, height)

    


class App(_GenericElement):
    def __init__(self, title: str = "App"):
        self.object_id = ac.newApp(title)

    
    def set_title(self, title: str) -> None:
        """
        Set the title of the app.
        """
        ac.setTitle(self.object_id, title)