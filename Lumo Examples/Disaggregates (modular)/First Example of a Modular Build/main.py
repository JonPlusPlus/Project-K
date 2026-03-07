# main.py
import os
from kivy.app import App
from kivy.lang import Builder
from mywidget import MyWidget

# ----------------------------------------------------------------------
# Option 1 – Automatic loading (recommended if you follow the naming rule)
# ----------------------------------------------------------------------
# If the KV file is named exactly like the App class (lowercase, without
# the "App" suffix) Kivy loads it automatically.  In this example we
# *explicitly* load it to make the flow obvious.
kv_path = os.path.join(os.path.dirname(__file__), "mywidget.kv")
Builder.load_file(kv_path)


class MyApp(App):
    """
    The top‑level Kivy Application.
    """

    def build(self):
        """
        Return the root widget of the UI.
        """
        # Instantiating MyWidget will automatically apply the <MyWidget>
        # rule from mywidget.kv because we already loaded the file.
        return MyWidget()


if __name__ == "__main__":
    MyApp().run()