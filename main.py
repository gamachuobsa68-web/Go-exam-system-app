from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from screens.home import HomeScreen
from screens.exam import ExamScreen
from screens.result import ResultScreen

class Root(BoxLayout):
    pass

class OroExam(App):
    def build(self):
        self.root = BoxLayout()

        self.home()

        return self.root

    def home(self):
        self.root.clear_widgets()
        self.root.add_widget(HomeScreen(self.start_exam))

    def start_exam(self, instance):
        self.root.clear_widgets()
        self.root.add_widget(ExamScreen(self.show_result))

    def show_result(self):
        self.root.clear_widgets()
        self.root.add_widget(ResultScreen())

OroExam().run()
