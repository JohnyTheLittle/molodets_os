from System.Drivers.LCD import lcd
from System.visualElements.ElemList import ElemList
from System.visualElements.ElemInfo import ElemInfo
from System.visualElements.KeyBoard import NumBoard
import math
from math import sin, cos, log

class Calculator:
    def __init__(self, sys, name):
        self.start = False
        self.tick = 0
        self.init_moment = 0.0
        self.render_modal = False
        self.x = 0
        self.y = 0
        self.system = sys
        self.name = name
        self.app_storage = {}
        self.list_elems = ElemList(lcd, [ElemInfo(lcd, "B - calc"), ElemInfo(lcd, "X - exit"), NumBoard(lcd)])
        self.val_to_render = ''
        
        
    def run_app_commands(self, system):
        self.system = system
        return self
    
    def cont(self, tick, key):
        self.tick+=0.01
        show_cursor = round(math.sin(tick*100))
        take = False
        
        if key == "X":
            self.system.stop()
        
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
            for i in range(len(self.list_elems.list)):
                if (isinstance(self.list_elems.list[i], NumBoard)):
                    try:
                        self.render_modal = eval(self.list_elems.list[i].input)
                    except:
                        self.render_modal = "wrong input"
                        
        
        if (self.init_moment):
            if (self.tick - self.init_moment) > 0.1:
                self.render_modal = False
                self.init_moment = 0
                
        val = self.list_elems.render(self.y, self.x, take, show_cursor, self.render_modal)
        
