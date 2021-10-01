class Screen:
    def __init__(self) -> None:
        pass    
    pass

class Form:
    def __init__(self) -> None:
        self.widgets = []
        pass    

    def addWidget(self, widget):
        self.widgets.append(widget)
        pass

    def show(self):
        pass

    pass

class Widget:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0        

    pass
