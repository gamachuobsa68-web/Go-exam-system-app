from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class HomeScreen(BoxLayout):
    def __init__(self, switch_to_exam, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.add_widget(Label(text="Oro Exam System"))

        btn = Button(text="Start Exam")
        btn.bind(on_press=switch_to_exam)
        self.add_widget(btn)
