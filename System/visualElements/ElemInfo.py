class ElemInfo:
    def __init__(self, lcd, content):
        print(lcd, content)
        self.lcd = lcd
        self.content = content
        self.borders = None
        self.size = 1
    def render(self, y):
        self.lcd.printstring(self.content, 120, y, self.size, self.lcd.colour(0, 255, 0))
