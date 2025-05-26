import ac
import acsys

from .graphics import Color
from .memory import *
from .font import FontAlignment, Font
from . import *

class _GenericElement:
    def __init__(self, object_id,
        text: str,
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
        font: Font,
        render_function = None
    ):
        self._object_id = object_id
        self.text = text
        self.size = size
        self.position = position
        self.background_opacity = background_opacity
        self.background_visible = background_visible
        self.border_visible = border_visible
        if background_texture is None:
            background_texture = None
        else:
            self.set_background_texture_path(background_texture)
        self.font_alignment = font_alignment
        self.font_color = font_color
        self.visible = visible
        self.font_size = font_size
        self.font = font
        self.on_render = render_function

    
    @property
    def size(self) -> 'tuple[float, float]':
        """
        The size of the element. (tuple[float, float])
        """
        return self._size

    @size.setter
    def size(self, size: 'tuple[float, float]') -> None:
        self._size = size
        ac.setSize(self._object_id, *size)

    @property
    def position(self) -> 'tuple[float, float]':
        """
        The position of the element. (tuple[float, float])
        """
        return ac.getPosition(self._object_id)
    
    @position.setter
    def position(self, position) -> None:
        ac.setPosition(self._object_id, *position)

    @property
    def text(self) -> str:
        """
        The text of the element.
        """
        return ac.getText(self._object_id)

    @text.setter    
    def text(self, text: str):
        log(ac.setText(self._object_id, text))

    @property
    def background_opacity(self) -> float:
        """
        The background opacity of the element.
        """
        return self._background_opacity

    @background_opacity.setter
    def background_opacity(self, opacity: float):
        if not (0 <= opacity <= 1):
            raise ValueError("Opacity must be between 0 and 1.")
        self._background_opacity = opacity
        ac.setBackgroundOpacity(self._object_id, opacity)
    
    @property
    def background_visible(self) -> bool:
        """
        The visibility of the background of the element.
        """
        return self._background_visible

    @background_visible.setter
    def background_visible(self, arg: bool = True) -> None:
        self._background_visible = arg
        ac.drawBackground(self._object_id, 1 if arg else 0)

    @property
    def border_visible(self) -> bool:
        """
        The visibility of the border of the element.
        """
        return self._border_visible
    
    @border_visible.setter
    def border_visible(self, arg: bool = True):
        self._border_visible = arg
        ac.drawBorder(self._object_id, 1 if arg else 0)

    def get_background_texture_path(self) -> str:
        """
        Get the background texture path of the element.
        """
        return self.background_texture

    def set_background_texture_path(self, path: str):
        """
        Set the background texture path of the element. Path starts from the assettocorsa root folder.
        """
        self.background_texture = path
        if path is not None:
            ac.setBackgroundTexture(self._object_id, path)

    @property
    def font_alignment(self) -> FontAlignment:
        """
        The font alignment of the element.
        """
        return self._font_alignment
    
    @font_alignment.setter
    def font_alignment(self, alignment: FontAlignment):
        if not isinstance(alignment, FontAlignment):
            raise ValueError("Alignment must be an instance of FontAlignment enum.")
        self._font_alignment = alignment
        ac.setFontAlignment(self._object_id, alignment.name)

    @property
    def visible(self) -> bool:
        """
        The visibility of the element.
        """
        return self._visible

    @visible.setter
    def visible(self, arg: bool = True):
        """
        Set the visibility of the element.
        """
        self._visible = arg
        ac.setVisible(self._object_id, 1 if arg else 0)

    @property
    def font_color(self) -> Color:
        """
        The font color of the element.
        """
        return self._font_color
    
    @font_color.setter
    def font_color(self, color: Color):
        if not isinstance(color, Color):
            raise ValueError("Color must be an instance of Color class.")
        self._font_color = color
        ac.setFontColor(self._object_id, *color.ac_rgba())

    @property
    def on_render(self):
        """
        The render function of the element.
        The first argument of the function must be the delta time.
        """
        return self._render_function
    
    @on_render.setter
    def on_render(self, func) -> None:
        if func is None:
            self._render_function = None
            return
        if not callable(func):
            raise ValueError("Render function must be a callable function.")
        self._render_function = func
        ac.addRenderCallback(self._object_id, func)

    @property
    def font_size(self) -> float:
        """
        The font size of the element.
        """
        return self._font_size
    
    @font_size.setter
    def font_size(self, size: float):
        if not isinstance(size, (int, float)):
            raise ValueError("Font size must be a number.")
        if size < 0:
            raise ValueError("Font size can't be less than 0.")
        self._font_size = size
        ac.setFontSize(self._object_id, size)

    @property
    def font(self) -> Font:
        """
        The font of the element.
        """
        return self._font
    
    @font.setter
    def font(self, font: Font):
        if not isinstance(font, Font):
            raise ValueError("Font must be an instance of Font class.")
        self._font = font
        if font.initialized:
            ac.setCustomFont(0, self._object_id, font.name, 1 if font.italic else 0, 1 if font.bold else 0)


class AppWindow(_GenericElement):
    def __init__(self,
        title: str = "App",
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
        title_position = (0, 0),
        font = Font()
    ):
        object_id = ac.newApp(title)
        log(object_id)
        super().__init__(
            object_id,
            "",
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
        self.title = title
        self.title_position = title_position


    @property
    def title(self) -> str:
        """
        The title of the app.
        """
        return self._title
    
    @title.setter
    def title(self, title: str) -> None:
        self._title = title
        ac.setTitle(self._object_id, title)

    @property
    def title_position(self) -> 'tuple[float, float]':
        """
        The position of the title.
        """
        self._title_position
    
    @title_position.setter
    def title_position(self, position) -> None:
        self._title_position = position
        ac.setTitlePosition(self._object_id, *position)

    def add_label(self, label: str):
        """
        Add a label to the app.
        """
        ac.addLabel(self._object_id, label)
    
    @property
    def icon_position(self) -> 'tuple[float, float]':
        """
        The position of the icon.
        """
        return self._icon_position
    
    @icon_position.setter
    def icon_position(self, position: 'tuple[float, float]') -> None:
        self._icon_position = position
        ac.setIconPosition(self._object_id, *position)

    @property
    def on_dismissed(self):
        """
        The function that is called when the app is dismissed.
        """
        return self._on_dismissed
    
    @on_dismissed.setter
    def on_dismissed(self, func) -> None:
        if func is None:
            self._on_dismissed = None
            return
        if not callable(func):
            raise ValueError("Dismissed function must be a callable function.")
        self._on_dismissed = func
        ac.addOnAppDismissedListener(self._object_id, func)

    @property
    def on_activated(self):
        """
        The function that is called when the app is activated.
        """
        return self._on_activated

    @on_activated.setter
    def on_activated(self, func) -> None:
        if func is None:
            self._on_activated = None
            return
        if not callable(func):
            raise ValueError("Activated function must be a callable function.")
        self._on_activated = func
        ac.addOnAppActivatedListener(self._object_id, func)


class Button(_GenericElement):
    def __init__(self, app: AppWindow,
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
        on_click = None
    ):
        object_id = ac.addButton(app._object_id, text)
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
        self._background_color = background_color
        self.on_click = on_click

    @property
    def background_color(self) -> Color:
        """
        The background color of the button.
        """
        return self._background_color
    
    @background_color.setter
    def background_color(self, color: Color) -> None:
        """
        Set the background color of the button.
        """
        if not isinstance(color, Color):
            raise ValueError("Color must be an instance of Color class.")
        self._background_color = color
        ac.setBackgroundColor(self._object_id, *color.ac_rgb())

    @property
    def on_click(self):
        """
        The function that is called when the button is clicked.
        """
        return self._on_click
    
    @on_click.setter
    def on_click(self, func) -> None:
        if func is None:
            self._on_click = None
            return
        if not callable(func):
            raise ValueError("Click function must be a callable function.")
        self._on_click = func
        ac.setClickFunction(self._object_id, func)

    
class Graph(_GenericElement):

    def __init__(self, app: AppWindow,
        range: 'tuple[float, float]' = (0.0, 1.0),
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
        object_id = ac.addGraph(app._object_id, text)
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
        self._range = range
        self._maximum_points = maximum_points
        ac.setRange(self._object_id, range[0], range[1], maximum_points)
        self._next_serie_index = 0

    @property
    def range(self) -> 'tuple[float, float]':
        """
        The value range of the graph.
        """
        return self._range
    
    @property
    def maximum_points(self) -> int:
        """
        The maximum number of data points in the graph. (read-only)
        """
        return self._maximum_points


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
        ac.addSerieToGraph(graph._object_id, *color.ac_rgb())

    @property
    def graph(self) -> Graph:
        """
        The graph to which this series belongs. (read-only)
        """
        return self._graph
    
    @property
    def color(self) -> Color:
        """
        The color of the series. (read-only)
        """
        return self._color
    
    def __getitem__(self, index: int) -> float:
        """
        Get a data point by index.
        """
        return self._data[index]
    
    def __len__(self) -> int:
        """
        Get the number of data points in the series.
        """
        return len(self._data)
        
    def add_data_point(self, data_point: float):
        """
        Add a data point to the series.
        """
        self._data.append(data_point)
        if len(self._data) > self._graph.maximum_points:
            self._data.pop(0)
        ac.addValueToGraph(self._graph._object_id, self._index, data_point)

    def add_multiple_data_points(self, data_points):
        """
        Add multiple data points to the series.
        """
        self._data.extend(data_points)
        data_points = data_points[-self._graph.maximum_points:]
        for data_point in data_points:
            ac.addValueToGraph(self._graph._object_id, self._index, data_point)


class Checkbox(_GenericElement):
    def __init__(self, app: AppWindow,
        name: str = "Checkbox",
        size = (25, 25),
        position = (50, 50),
        background_opacity: float = 1.0,
        background_visible: bool = True,
        border_visible: bool = True,
        background_texture: str = None,
        font_alignment: FontAlignment = FontAlignment.CENTER,
        font_color: Color = Color(255, 255, 255, 1),
        visible: bool = True,
        font_size: int = 12,
        font = Font(),
        on_change = None
    ):
        object_id = ac.addCheckBox(app._object_id, name)
        super().__init__(object_id,
            text = "",
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
        self.on_change = on_change

    @property
    def on_change(self):
        """
        The function that is called when the checkbox is changed.
        The first argument of the function must be the name of the checkbox, 
        and the second one is wether it is selected of not.
        """
        return self._on_change
    
    @on_change.setter
    def on_change(self, func):
        if func is None:
            self._on_change = None
            return
        if not callable(func):
            raise ValueError("Change function must be a callable function.")
        self._on_change = func
        ac.addOnCheckBoxChanged(self._object_id, func)

# _range = range
class Spinner(_GenericElement):
    def __init__(self, app: AppWindow,
        name: str = "Spinner",
        value: float = 0.0,
        range: 'tuple[float, float]' = (0.0, 1.0),
        step: float = 0.1,
        size = (100, 25),
        position = (50, 50),
        background_opacity: float = 1.0,
        background_visible: bool = True,
        border_visible: bool = True,
        background_texture: str = None,
        font_alignment: FontAlignment = FontAlignment.CENTER,
        font_color: Color = Color(255, 255, 255, 1),
        visible: bool = True,
        font_size: int = 12,
        font = Font(),
        on_change = None
    ):
        object_id = ac.addSpinner(app._object_id, name)
        super().__init__(object_id,
            text = "",
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
        self.range = range
        self.value = value
        self.on_change = on_change
        self.step = step


    @property
    def value(self) -> float:
        """
        The current value of the spinner.
        The value must be within the range of the spinner.
        """
        result = ac.getValue(self._object_id)
        log(result)
        return result
    
    @value.setter
    def value(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError("Value must be a float.")
        if value < self.range[0] or value > self.range[1]:
            raise ValueError("Value must be within the range {}.".format(self.range))
        ac.setValue(self._object_id, value)

    @property
    def range(self) -> 'tuple[float, float]':
        """
        The range of the spinner.
        """
        return self._range

    @range.setter
    def range(self, range: 'tuple[float, float]') -> None:
        self._range = range
        ac.setRange(self._object_id, range[0], range[1])
        # ac.setStep(self._object_id, range.step)

    @property
    def step(self) -> float:
        """
        The step of the spinner.
        """
        return self._step
    
    @step.setter
    def step(self, step: float) -> None:
        if step <= 0:
            raise ValueError("Step must be greater than 0.")
        self._step = step
        ac.setStep(self._object_id, step)

    @property
    def on_change(self):
        """
        The function that is called when the spinner value is changed.
        The first argument of the function must be the name of the spinner, 
        and the second one is the new value.
        """
        return self._on_change
    
    @on_change.setter
    def on_change(self, func):
        if func is None:
            self._on_change = None
            return
        if not callable(func):
            raise ValueError("Change function must be a callable function.")
        self._on_change = func
        ac.addOnSpinnerChanged(self._object_id, func)