from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen


class MDEx(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
      
        # Screen() creates a layout container for Material Design widgets.
        screen = Screen()

        # MDLabel(...) creates a label with text, custom color, and alignment.
        label = MDLabel(
            text="Welcome!",
            # pos_hint={'center_x': 0.5, 'center_y': 0.5} centers the label in the screen.
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            # theme_text_color='Custom' + text_color=(...) applies the custom RGBA color to the text.
            theme_text_color="Custom",
            text_color=(0.9, 0.2, 0.5, 1),
            # halign='center' ensures the text is horizontally centered.
            halign="center"
        )

        # screen.add_widget(label) adds the label to the screen.
        screen.add_widget(label)
        # return screen returns the screen to be displayed as the root widget.
        return screen


# MDEx().run() creates and runs the application window.
MDEx().run()
