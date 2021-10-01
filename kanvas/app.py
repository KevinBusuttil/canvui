# app.py
from .ui.core import Form, Widget
from .ui.textbox import Textbox

class kanvas:

    def run(self):      
        print("Hello World...")

        form = Form()

        text01 = Textbox()
        text01.x = 10
        text01.y = 20
        text01.width = 150
        text01.height = 100
        text01.label = "Enter name"

        form.addWidget(text01)
        form.show()




