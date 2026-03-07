# mywidget.py
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty
from kivy.clock import Clock


class MyWidget(BoxLayout):
    """
    Business‑logic side of the UI.
    """

    # ------------------------------------------------------------------
    # Public properties that the KV file can bind to.
    # ------------------------------------------------------------------
    counter = NumericProperty(0)               # internal numeric state
    display_text = StringProperty("Counter: 0")  # shown in the Label

    # ------------------------------------------------------------------
    # Lifecycle hook – called once the widget is added to the window.
    # ------------------------------------------------------------------
    def on_kv_post(self, base_widget):
        """
        Called after the KV rule has been applied.
        Good place to initialise things that depend on the UI being ready.
        """
        # Ensure the displayed text matches the initial counter value
        self.update_display()

    # ------------------------------------------------------------------
    # Helper to keep the label in sync with the counter.
    # ------------------------------------------------------------------
    def update_display(self):
        self.display_text = f"Counter: {self.counter}"

    # ------------------------------------------------------------------
    # Method bound to the Button in the KV file.
    # ------------------------------------------------------------------
    def increase_counter(self):
        """Increment the counter and refresh the label."""
        self.counter += 1
        self.update_display()

    # ------------------------------------------------------------------
    # Example of reacting to property changes automatically.
    # ------------------------------------------------------------------
    def on_counter(self, instance, value):
        """
        Kivy automatically calls `on_<prop_name>` whenever the property changes.
        Here we could trigger additional side‑effects (e.g., logging).
        """
        print(f"[MyWidget] Counter changed to {value}")