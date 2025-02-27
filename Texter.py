import math
from System.visualElements.ElemList import ElemList
from System.visualElements.ElemInfo import ElemInfo
from System.visualElements.KeyBoard import KeyBoard
from System.Drivers.LCD import lcd

class Texter:
    def __init__(self, name):
        self.start = False
        self.tick = 0
        self.init_moment = 0.0
        self.render_modal = None
        self.x = 0
        self.y = 0
        self.system = None
        self.name = name
        self.app_storage = {}
        f = open('text.txt')
        initial_input = f.read()
        f.close()
        self.list_elems = ElemList(lcd, [ElemInfo(lcd, "B - save"), ElemInfo(lcd, "X - exit"), ElemInfo(lcd, "A - up"), ElemInfo(lcd, "Y - down"), KeyBoard(lcd, initial_input)])
        self.val_to_render = ''
        
        
    def run_app_commands(self, system):
        self.system = system
        return self
    def __save__(self):
        for i in range(len(self.list_elems.list)):
            if (isinstance(self.list_elems.list[i], KeyBoard)):
                f = open("text.txt","w")
                print(self.list_elems.list[i].input)
                f.write(self.list_elems.list[i].input)
                f.close()
    def cont(self, tick, key):
        self.tick+=0.01
        show_cursor = round(math.sin(tick*100))
        take = False
        if key == "X":
            self.system.ask_to_start(App("ENOTIK"))
        
        if key == "up":
            self.y-=1
        
        if key == "down":
            self.y+=1
        
        if key == "left":
            self.x-=1
        
        if key == "right":
            self.x+=1
        
        if key == "ctrl":
            take = not take
        
        if key == "B":
            self.init_moment = self.tick
            self.render_modal = "DONE"
            self.__save__()
        
        if (self.init_moment):
            if (self.tick - self.init_moment) > 0.1:
                self.render_modal = None
                self.init_moment = 0
                
        val = self.list_elems.render(self.y, self.x, take, show_cursor, self.render_modal)
        
        self.system.stop()
