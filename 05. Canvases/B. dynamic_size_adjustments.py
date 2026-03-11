from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color


class ResponsiveCanvas(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0.8, 0.3, 0.3, 1)
            # self.rect = Rectangle(pos=self.pos, size=self.size): initial rectangle matching widget size.
            self.rect = Rectangle(pos=self.pos, size=self.size)
        # self.bind(pos=self.update_rect, size=self.update_rect): updates rectangle on window resize.
        # update_rect(): sets rectangle’s pos and size to match the widget.
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class CanvasApp(App):
    def build(self):
        return ResponsiveCanvas()


if __name__ == '__main__':
    CanvasApp().run()