import random
class TextElem:
    def __init__(self, lcd, content):
        self.lcd = lcd
        self.id = "".join([chr(random.randint(97, 122)) for x in range(10)])
        self.content = content
        self.borders = False
        self.size = 1
