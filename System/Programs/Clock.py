import time
from System.visualElements.ElemList import ElemList
from System.visualElements.Elem import Elem
from System.visualElements.BigElem import BigElem
from System.visualElements.TextElem import TextElem
from System.Drivers.LCD import lcd

class Clock:
    def __init__(self, sys, name):
        self.start = False
        self.tick = 0
        self.x = 0
        self.system = sys
        self.name = name
        self.app_storage = {}
        self.list_elems = ElemList(lcd,
                                   [BigElem(lcd,""),
                                    TextElem(lcd, "To go wrong in one's own way is better than to go right in someone else's. ( Fyodor Dostoevsky)")
                                    ])
        
        
    def run_app_commands(self, system):
        return self
    
    def cont(self, tick, key):
        self.tick+=0.01
            
            
        if key == "X":
            self.system.stop()
        
        if (self.tick <= 10000):
            t = time.gmtime()
            (year, month, mday, hour, minute, second, weekday, yearday) = t
            t = str(hour)+":"+str(minute)+":"+str(second)
            self.list_elems.list[0].content = t
            self.list_elems.render()
        
