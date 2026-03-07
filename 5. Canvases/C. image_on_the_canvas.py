from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color


class ImageCanvas(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # Rectangle(source='flower.jpg', pos=self.pos, size=self.size): Draws the image on the widget canvas.
            self.rect = Rectangle(source='flower.jpg', pos=self.pos, size=self.size)
            # Color(1, 1, 1, 0.15): Adds a subtle white overlay with 15% opacity to make the image look soft and bright.
            Color(1, 1, 1, 0.15)
            self.overlay = Rectangle(pos=self.pos, size=self.size)
        # self.bind(pos=..., size=...): Keeps the image and overlay aligned with the widget when the window is resized.
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.overlay.pos = self.pos
        self.overlay.size = self.size


class CanvasApp(App):
    def build(self):
        return ImageCanvas()


if __name__ == '__main__':
    CanvasApp().run()