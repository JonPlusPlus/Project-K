from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color


class BasicCanvas(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # with self.canvas: adds instructions to the widget’s canvas.
        with self.canvas:
            # Color(): sets the color for the next shape.
            Color(0.5, 0.7, 0.2, 1) # a green-ish colour
            # Rectangle(pos=..., size=...): draws a rectangle at the specified position and size.
            Rectangle(pos=(100, 100), size=(200, 100))
                #     pos: position of the shape relative to the window or widget.
                #     size: width and height of the shape.
                #     source: optional; image file to display inside the rectangle.
                #     Color(r, g, b, a): sets the color (0–1 values for red, green, blue, alpha).
                #     Bind pos and size if you want shapes to adjust when the widget changes.


class CanvasApp(App):
        def build(self):
            return BasicCanvas()


if __name__ == '__main__':
    CanvasApp().run()



