from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle

class RoundedBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.2, 0.6, 0.9, 1)          # fill colour
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[20,]                 # 20‑pixel corner radius
            )
        # Keep the rectangle in sync with widget geometry
        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class DemoApp(App):
    def build(self):
        return RoundedBox(padding=20, size_hint=(None, None),
                          size=(300, 200))

if __name__ == '__main__':
    DemoApp().run()