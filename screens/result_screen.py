from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from core.score import score

class ResultScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.add_widget(Label(text=f"Your Score: {score}"))
