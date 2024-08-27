class NumBoard:
    def __init__(self, lcd, initial_input = ""):
        self.mapping = ["1234567890<", "+-/*().", ["sin", "cos", "log", "sqrt", "pow"]]
        self.content = None
        self.borders = None
        self.lcd = lcd
        self.input = initial_input
    
    def __keys__(self, i_pos = 0, j_pos = 0, ctrl = False):
        response = None
        for i in range(len(self.mapping)):
            for j in range(len(self.mapping[i])):
                if i == i_pos and j == j_pos:
                    if ctrl:
                        response = self.mapping[i][j]
                    if i == 2:
                        self.lcd.rect(j*35+10, 180+15*i+10, 40, 15, self.lcd.colour(0,255,0))
                    else:    
                        self.lcd.rect(j*15+10, 180+15*i+10, 15, 15, self.lcd.colour(0,255,0))
                if i == 2:
                    self.lcd.printstring(self.mapping[i][j], j*40+10, 180+15*i+10 + 3, 1, self.lcd.colour(0, 255, 0))
                else:
                    self.lcd.printstring(self.mapping[i][j], j*15+10 + 2, 180+15*i+10 + 3, 1, self.lcd.colour(0, 255, 0))
        return response
    
    def render(self, i_p = 0, j_p = 0, ctrl = None, show_cursor = 0):
        response_from_rendered = None
        response_from_rendered = self.__keys__(i_p, j_p, ctrl)
        
        if (response_from_rendered):
            if response_from_rendered == "<":
                self.input = self.input[0:len(self.input) - 1]
            elif response_from_rendered == "_":
                self.input+=" "
            else:
                self.input+=response_from_rendered
        row = ''
        rows = []
        for i in range(len(self.input)):
           if (i%12==0):
               rows.append(row)
           rows[-1]+=self.input[i]
        for i in range(len(rows)):
            self.lcd.printstring(rows[i], (len(rows[i])% 12) + 10, 50+(i*10), 1, self.lcd.colour(0,255,0))
        if show_cursor and rows:
            rows[-1]+="|"
            
        return response_from_rendered


class KeyBoard:
    def __init__(self, lcd, initial_input = ""):
        self.lcd = lcd
        self.mapping = ["qwertyuiop<", "asdfghjkl", "zxcvbnm_.,:"]
        self.content = None
        self.borders = None
        self.input = initial_input
    
    def __keys__(self, i_pos = 0, j_pos = 0, ctrl = False):
        response = None
        for i in range(len(self.mapping)):
            for j in range(len(self.mapping[i])):
                if i == i_pos and j == j_pos:
                    self.lcd.rect(j*15+10, 180+15*i+10, 15, 15, self.lcd.colour(0,255,0))
                    if ctrl:
                        response = self.mapping[i][j]
                self.lcd.printstring(self.mapping[i][j], j*15+10 + 2, 180+15*i+10 + 3, 1, self.lcd.colour(0, 255, 0))
        return response
    
    def render(self, i_p = 0, j_p = 0, ctrl = None, show_cursor = 0):
        response_from_rendered = None
        response_from_rendered = self.__keys__(i_p, j_p, ctrl)
        
        if (response_from_rendered):
            if response_from_rendered == "<":
                self.input = self.input[0:len(self.input) - 1]
            elif response_from_rendered == "_":
                self.input+=" "
            else:
                self.input+=response_from_rendered
        row = ''
        rows = []
        for i in range(len(self.input)):
           if (i%12==0):
               rows.append(row)
           rows[-1]+=self.input[i]
        for i in range(len(rows)):
            self.lcd.printstring(rows[i], (len(rows[i])% 12) + 10, 50+(i*10), 1, self.lcd.colour(0,255,0))
        if show_cursor and rows:
            rows[-1]+="|"
            
        return response_from_rendered
