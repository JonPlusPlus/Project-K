# import kivy ensures the Kivy library is available.
import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.11.1')


# App is the base class for creating Kivy applications.
# class MyFirstKivyApp(App) defines the application class.
# This class sets up the GUI and contains all the application logic.
# MyFirstKivyApp() creates an instance of the application.
class MyFirstKivyApp(App):
    # build() method returns the root widget, which in this case is a Label displaying “Hello World!”.
    def build(self):
        # Label is a widget used to display text in the application window.
        return Label(text="Hello World!")


if __name__ == '__main__':
    # .run() starts the Kivy event loop and displays the window with the Label widget.
    MyFirstKivyApp().run()
