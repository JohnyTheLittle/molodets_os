import random

class Elem:
    def __init__(self, lcd, content):
        self.id = "".join([chr(random.randint(97, 122)) for x in range(10)])
        print(self.id+" "+content)
        self.content = content
        self.borders = False
        self.size = 1
    
    def toggle_borders(self):
        self.borders = not self.borders
