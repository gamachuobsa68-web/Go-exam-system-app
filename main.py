from kivy.app import App
from kivy.uix.label import Label

class OroExam(App):
    def build(self):
        return Label(text="Oro Exam System Started")

OroExam().run()
