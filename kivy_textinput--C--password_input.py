from kivy.app import App
from kivy.uix.textinput import TextInput


class PasswordApp(App):
    def build(self):
        return TextInput(hint_text='Enter password', password=True, multiline=False)
            #   text: initial text shown in the field.
            #   multiline (bool): True allows Enter/newlines; False makes it single-line.
            #   password (bool): hides characters (useful for password fields).
            #   hint_text: placeholder shown when text is empty.
            #   font_size: text size (e.g. '20sp' or 20).
            #   size_hint: control widget sizing in layouts.


if __name__ == '__main__':
    PasswordApp().run()