import ac
import acsys

from .graphics import Color
from .memory import *
from .font import FontAlignment, Font
from . import *

class _GenericElement:
    def __init__(self, object_id,
        text,
        size,
        position,
        background_opacity: float,
        background_visible: bool,
        border_visible: bool,
        background_texture: str,
        font_alignment: FontAlignment,
        font_color: Color,
        visible: bool,
        font_size: int,
        font: Font
    ):
        self.object_id = object_id
        self.text = text
        self.set_size(*size)
        log(1)
        self.set_position(*position)
        log(2)
        self.set_background_opacity(background_opacity)
        log(3)
        self.set_background_visible(background_visible)
        log(4)
        self.set_border_visible(border_visible)
        log(5)
        if background_texture is None:
            background_texture = None
        else:
            self.set_background_texture(background_texture)
        log(6)
        self.set_font_alignment(font_alignment)
        log(7)
        self.set_font_color(font_color)
        log(8)
        self.set_visible(visible)
        log(9)
        self.set_font_size(font_size)
        log(10)
        self.set_font(font)
        log(11)

    
    def set_size(self, width: float, height: float) -> None:
        """
        Set the size of the element.
        """
        self.size = width, height
        ac.setSize(self.object_id, width, height)

    def get_size(self):
        """
        Get the size of the element. (tuple[float, float])
        """
        return self.size

    def set_position(self, x: float, y: float) -> None:
        """
        Set the position of the element.
        """
        self.position = x, y
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
        self.text = text
        ac.setText(self.object_id, text)

    def set_background_opacity(self, opacity: float) -> None:
        """
        Set the background opacity of the element. Opacity must be between 0 and 1.
        """
        if not (0 <= opacity <= 1):
            raise ValueError("Opacity must be between 0 and 1.")
        self.background_opacity = opacity
        ac.setBackgroundOpacity(self.object_id, opacity)
    
    def set_background_visible(self, arg: bool = True) -> None:
        """
        Draw the background of the element.
        """
        self.background_visible = arg
        ac.drawBackground(self.object_id, 1 if arg else 0)

    def set_border_visible(self, arg: bool = True) -> None:
        """
        Draw the border of the element.
        """
        self.border_visible = arg
        ac.drawBorder(self.object_id, 1 if arg else 0)

    def set_background_texture(self, path: str) -> None:
        """
        Set the background texture of the element. Path starts from the assettocorsa root folder.
        """
        self.background_texture = path
        if path is not None:
            ac.setBackgroundTexture(self.object_id, path)

    def set_font_alignment(self, alignment: FontAlignment) -> None:
        """
        Set the font alignment of the element.
        """
        # ac.console(alignment.name.lower())
        self.font_alignment = alignment
        ac.setFontAlignment(self.object_id, alignment.name)


    def set_visible(self, arg: bool = True) -> None:
        """
        Set the visibility of the element.
        """
        self.visible = arg
        ac.setVisible(self.object_id, 1 if arg else 0)

    def set_font_color(self, color: Color) -> None:
        """
        Set the font color of the element.
        """
        self.font_color = color
        log(ac.setFontColor(self.object_id, *color.ac_rgba()))

    def add_render_callback(self, callback) -> None:
        """
        Add a callback to the element when it is rendered.
        The first argument of the callback must be the delta time.
        """
        if not callable(callback):
            raise ValueError("Callback must be a callable function.")
        ac.addRenderCallback(self.object_id, callback)

    def set_font_size(self, size: int) -> None:
        """
        Set the font size of the element.
        """
        self.font_size = size
        ac.setFontSize(self.object_id, size)

    def set_font(self, font: Font) -> None:
        """
        Set the font of the element.
        """
        self.font = font
        if font.initialized:
            ac.setCustomFont(0, self.object_id, font.name, 1 if font.italic else 0, 1 if font.bold else 0)


class Button(_GenericElement):
    def __init__(self, app: 'AppWindow',
        text: str = "Title",
        size = (50, 50),
        position = (0, 0),
        background_opacity: float = 1.0,
        background_visible: bool = True,
        border_visible: bool = True,
        background_texture: str = None,
        font_alignment: FontAlignment = FontAlignment.CENTER,
        background_color: Color = Color(0, 0, 0, 1),
        font_color: Color = Color(255, 255, 255, 1),
        visible: bool = True,
        font_size: int = 12,
        font = Font(),
    ):
        object_id = ac.addButton(app.object_id, text)
        super().__init__(object_id,
            text = text,
            size = size,
            position = position,
            background_opacity = background_opacity,
            background_visible = background_visible,
            border_visible = border_visible,
            background_texture = background_texture,
            font_alignment = font_alignment,
            font_color = font_color,
            visible = visible,
            font_size = font_size,
            font = font
        )
        self.set_background_color(background_color)

    def set_background_color(self, color: Color) -> None:
        """
        Set the background color of the element.
        """
        self.background_color = color
        ac.setBackgroundColor(self.object_id, *color.ac_rgb())


    def add_on_click_callback(self, callback) -> None:
        """
        Add a callback to the button when it is clicked.
        """
        ac.addOnButtonClickListener(self.object_id, callback)

    
class Graph(_GenericElement):

    def __init__(self, app: 'AppWindow',
        minimum_value: float = 0.0,
        maximum_value: float = 1.0,
        maximum_points: int = 100,
        text: str = "Graph",
        size = (0, 0),
        position = (0, 0),
        background_opacity: float = 1.0,
        background_visible: bool = True,
        border_visible: bool = True,
        background_texture: str = None,
        font_alignment: FontAlignment = FontAlignment.CENTER,
        font_color: Color = Color(255, 255, 255, 1),
        visible: bool = True,
        font_size: int = 12,
        font = Font()
    ):
        log("Creating graph with text: {}".format(text))
        object_id = ac.addGraph(app.object_id, text)
        log(object_id)
        super().__init__(
            object_id,
            text,
            size,
            position,
            background_opacity,
            background_visible,
            border_visible,
            background_texture,
            font_alignment,
            font_color,
            visible,
            font_size,
            font
        )
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value
        self.maximum_points = maximum_points
        log(ac.setRange(self.object_id, minimum_value, maximum_value, maximum_points-1))
        log(ac.setRange(self.object_id, minimum_value, maximum_value, maximum_points))
        self._next_serie_index = 0
    
    # def add_serie(self, serie: Serie):
    #     """
    #     Add a new series to the graph.
    #     """
    #     index = len(self.series)
    #     serie = Serie(self.object_id, index, color)
    #     self.series.append(serie)
    #     ac.addGraphSerie(self.object_id, index, *color.ac_rgb())
    #     return serie


class Serie:
    def __init__(self, graph: Graph, color: Color):
        """
        Initialize a new series for the graph.
        """
        self._graph = graph
        self._index = graph._next_serie_index
        graph._next_serie_index += 1
        self._color = color
        self._data = []
        ac.addSerieToGraph(graph.object_id, *color.ac_rgb())
        
    def add_data_point(self, data_point: float):
        """
        Add a data point to the series.
        """
        self._data.append(data_point)
        if len(self._data) > self._graph.maximum_points:
            self._data.pop(0)
        ac.addValueToGraph(self._graph.object_id, self._index, data_point)

    def add_multiple_data_points(self, data_points):
        """
        Add multiple data points to the series.
        """
        self._data.extend(data_points)
        data_points = data_points[-self._graph.maximum_points:]
        for data_point in data_points:
            ac.addValueToGraph(self._graph.object_id, self._index, data_point)


class AppWindow(_GenericElement):
    def __init__(self,
        text: str = "App",
        size = (100, 100),
        position = (0, 0),
        background_opacity: float = 0.5,
        background_visible: bool = True,
        border_visible: bool = True,
        background_texture: str = None,
        font_alignment: FontAlignment = FontAlignment.CENTER,
        font_color: Color = Color(255, 255, 255, 1),
        visible: bool = True,
        font_size: int = 12,
        font = Font()
    ):
        object_id = ac.newApp(text)
        super().__init__(
            object_id,
            text,
            size,
            position,
            background_opacity,
            background_visible,
            border_visible,
            background_texture,
            font_alignment,
            font_color,
            visible,
            font_size,
            font
        )

    
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
    
