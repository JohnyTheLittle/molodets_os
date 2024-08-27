from System.Programs.Clock import Clock
from System.Programs.Calculator import Calculator
from System.Programs.Texter import Texter
from System.visualElements.ElemList import ElemList
from System.visualElements.Elem import Elem
from System.Drivers.LCD import lcd

class MainApp:
    def __init__(self, system, name):
        self.start = False
        self.tick = 0
        self.x = 0
        self.system = system
        self.name = name
        self.app_storage = {}
        self.list_elems = ElemList(lcd, [Elem(lcd, "CLOCK"), Elem(lcd, "TXT"), Elem(lcd, "CALC")])
    
    #def start(self):
        #self.system.__update__(self)
        
    def run_app_commands(self, system):
        self.system = system
        self.list_elems.add(Elem(lcd, "LED (B)"))
        self.list_elems.list[0].toggle_borders()
        return self
    
    def cont(self, tick, key):
        self.tick+=0.01
        
        if key == "up":
            self.list_elems.list[self.x].toggle_borders()
            self.x = (self.x - 1) if self.x > 0 else (len(self.list_elems.list) - 1)
            self.list_elems.list[self.x].toggle_borders()
            
        if key == "down":
            self.list_elems.list[self.x].toggle_borders()
            self.x = (self.x+1)%len(self.list_elems.list)
            self.list_elems.list[self.x].toggle_borders()
            
        if key == "B":
            #LED.toggle()
            print("hi mark")
            
        if key == "ctrl":
            if self.x == 0:
                self.system.ask_to_start(Clock(self.system, "clck"))
            if self.x == 1:
                self.system.ask_to_start(Texter(self.system, "letopisec"))
            if self.x == 2:
                self.system.ask_to_start(Calculator(self.system, "calculator"))
            
        if (self.tick <= 10000):
            self.list_elems.render()        

