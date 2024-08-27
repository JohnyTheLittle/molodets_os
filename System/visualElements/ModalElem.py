class ModalElem:
    def __init__(self, lcd, content):
        self.lcd = lcd
        self.content = content
        self.borders = None
        self.size = 1
    
    def render(self, lcd, y):
        self.lcd.rect(100, 100, 50, 50, self.lcd.colour(0,225,0))
        self.lcd.printstring(self.content, 120, 120, self.size, self.lcd.colour(0, 255, 0))