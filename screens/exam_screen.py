from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from core.questions import questions
from core.score import add_score

class ExamScreen(BoxLayout):
    def __init__(self, go_result, **kwargs):
        super().__init__(**kwargs)
        self.index = 0
        self.go_result = go_result
        self.orientation = "vertical"

        self.q_label = Label()
        self.add_widget(self.q_label)

        self.load_question()

    def load_question(self):
        q = questions[self.index]
        self.q_label.text = q["q"]

        self.clear_widgets()
        self.add_widget(self.q_label)

        for opt in q["options"]:
            btn = Button(text=opt)
            btn.bind(on_press=self.check_answer)
            self.add_widget(btn)

    def check_answer(self, instance):
        if instance.text == questions[self.index]["answer"]:
            add_score()

        self.index += 1

        if self.index < len(questions):
            self.load_question()
        else:
            self.go_result()
