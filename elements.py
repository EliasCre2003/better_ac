import ac
import acsys

from .misc import Color, FontAlignment
from .memory import *

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

    def set_position(self, x: float, y: float) -> None:
        """
        Set the position of the element.
        """
        ac.setPosition(self.object_id, x, y)

    def get_position(self):
        """
        Get the position of the element. (tuple[float, float])
        """
        return ac.getPosition(self.object_id)
    
    def get_text(self) -> str:
        """
        Get the text of the element.
        """
        return ac.getText(self.object_id)
    
    def set_text(self, text: str) -> None:
        """
        Set the text of the element.
        """
        ac.setText(self.object_id, text)

    def set_background_opacity(self, opacity: float) -> None:
        """
        Set the background opacity of the element. Opacity must be between 0 and 1.
        """
        if not (0 <= opacity <= 1):
            raise ValueError("Opacity must be between 0 and 1.")
        ac.setBackgroundOpacity(self.object_id, opacity)
    
    def set_background_visible(self, arg: bool = True) -> None:
        """
        Draw the background of the element.
        """
        ac.drawBackground(self.object_id, 1 if arg else 0)

    def set_border_visible(self, arg: bool = True) -> None:
        """
        Draw the border of the element.
        """
        ac.drawBorder(self.object_id, 1 if arg else 0)

    def set_background_texture(self, path: str) -> None:
        """
        Set the background texture of the element. Path starts from the assettocorsa root folder.
        """
        ac.setBackgroundTexture(self.object_id, path)

    def set_font_alignment(self, alignment: FontAlignment) -> None:
        """
        Set the font alignment of the element.
        """
        # ac.console(alignment.name.lower())
        ac.setFontAlignment(self.object_id, alignment.name)

    def set_background_color(self, color: Color) -> None:
        """
        Set the background color of the element.
        """
        ac.setBackgroundColor(self.object_id, *color.ac_rgb())

    def set_visible(self, arg: bool = True) -> None:
        """
        Set the visibility of the element.
        """
        ac.setVisible(self.object_id, 1 if arg else 0)

    def set_font_color(self, color: Color) -> None:
        """
        Set the font color of the element.
        """
        ac.setFontColor(self.object_id, *color.ac_rgba())

    def add_render_callback(self, callback) -> None:
        """
        Add a callback to the element when it is rendered.
        """
        ac.addRenderCallback(self.object_id, callback)

    def set_font_size(self, size: float) -> None:
        """
        Set the font size of the element.
        """
        ac.setFontSize(self.object_id, size)

    


class Button(_GenericElement):
    def __init__(self, button_id: int):
        self.object_id = button_id

    def add_on_click_callback(self, callback) -> None:
        """
        Add a callback to the button when it is clicked.
        """
        ac.addOnButtonClickListener(self.object_id, callback)


class AppWindow(_GenericElement):
    def __init__(self, title: str = "App"):
        self.object_id = ac.newApp(title)

    
    def set_title(self, title: str) -> None:
        """
        Set the title of the app.
        """
        ac.setTitle(self.object_id, title)

    def add_label(self, label: str) -> int:
        """
        Add a label to the app.
        """
        return ac.addLabel(self.object_id, label)
    
    def add_button(self, title: str) -> Button:
        """
        Add a button to the element.
        """
        button_id = ac.addButton(self.object_id, title)
        return Button(button_id)
    
    def set_icon_position(self, x: float, y: float) -> None:
        """
        Set the position of the icon.
        """
        ac.setIconPosition(self.object_id, x, y)

    def set_title_position(self, x: float, y: float) -> None:
        """
        Set the position of the title.
        """
        ac.setTitlePosition(self.object_id, x, y)

    def add_on_activated_callback(self, callback) -> None:
        """
        Add a callback to the app when it is activated.
        """
        ac.addOnAppActivatedListener(self.object_id, callback)

    def add_on_dismissed_callback(self, callback) -> None:
        """
        Add a callback to the app when it is dismissed.
        """
        ac.addOnAppDismissedListener(self.object_id, callback)
    
