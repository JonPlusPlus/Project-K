# rounded_button_demo.py
# -------------------------------------------------
# Run with:  python rounded_button_demo.py
# -------------------------------------------------

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.0.0')   # make sure a recent Kivy version is installed

# ----------------------------------------------------------------------
# KV description (embedded as a string)
# ----------------------------------------------------------------------
kv = '''
<RoundedButton@Button>:
    # This rule defines a button whose canvas draws a rounded rectangle.
    # The actual Button widget still gets all its normal behavior.
    canvas.before:
        Color:
            rgba: self.background_color   # use the button's bg colour
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(16),]            # 16 dp corner radius (uniform)

BoxLayout:
    orientation: 'vertical'
    padding: dp(40)
    spacing: dp(20)

    # Center the button
    Widget:                         # spacer (top)
    RoundedButton:
        text: 'Rounded button'
        size_hint: None, None
        size: dp(200), dp(60)
        background_color: 0.2, 0.6, 0.9, 1   # light‑blue background
        color: 1, 1, 1, 1                  # white text
        on_release: app.on_button_press()
    Widget:                         # spacer (bottom)
'''

class DemoApp(App):
    def build(self):
        # Load the KV string and return the root widget (the BoxLayout)
        return Builder.load_string(kv)

    def on_button_press(self):
        print("✅ Rounded button clicked!")

if __name__ == '__main__':
    DemoApp().run()