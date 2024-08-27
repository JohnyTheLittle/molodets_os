import os
from System.Programs.MainApp import MainApp
import random
import time
import utime


class Queue:
    def __init__(self, sys, initialApp):
        self.sys = sys
        self.init_app = initialApp
        self.q = [initialApp]
        self.len = 1
    
    def pop(self):
        item = self.q.pop()
        self.len = len(self.q)
        return item
    
    def enqueue(self, app):
        self.q.insert(0, app)
        self.len = len(self.q)


class System:
    def __init__(self, lcd, keyA, keyB, keyX, keyY, up, down, right, left, ctrl):
        self.id="".join([chr(random.randint(97, 122)) for x in range(10)])
        self.queue = Queue(self, MainApp(self, "Main"))
        self.lcd = lcd
        self.A = keyA
        self.B = keyB
        self.X = keyX
        self.Y = keyY
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        self.ctrl = ctrl
        self.terminated = None
        self.dispNone = False
        self.loader()
    
    
    def loader(self):
        self.lcd.rect(5, 5, self.lcd.width - 10, self.lcd.height - 10, self.lcd.colour(0,200,0))
        self.lcd.printstring("MOLODETS", 15, 8, 3, self.lcd.colour(0,200,0))
        self.lcd.show()
        self.lcd.printstring("v.0.0.0", 15, 60, 2, self.lcd.colour(0,200,0))
        self.lcd.show()
        self.lcd.printstring("Bud' molodtsom", 15, 100, 1, self.lcd.colour(0,200,0))
        self.lcd.printstring("accessing memory" + self.id, 15, 150, 1, self.lcd.colour(0,200,0))
        mem = os.listdir()
        self.lcd.printstring("|".join(mem), 15, 200, 1, self.lcd.colour(0,200,0))
        self.lcd.show()
        #self.wait()        
        
        while (self.queue.len):
            exit_code = self.__run_process__(self.queue.pop())
            print(f'exit_code={exit_code}')
        
    
    def demonstrate_items(self):
        p = 0
        
        for i in range(len(self.items_list)):
            p+=40
            self.print_small(self.items_list[i], p, 1)
        
    
    def __frame__(self, frame_name = "", pressed=None):
        self.lcd.fill(0)    
        self.lcd.rect(5, 5, self.lcd.width - 10, self.lcd.height - 10, self.lcd.colour(0,200,0))
        self.lcd.rect(5, 5, self.lcd.width - 10, 30, self.lcd.colour(0,200,0))
        self.lcd.printstring(frame_name, 15, 8, 2, self.lcd.colour(0,200,0))
        
        if (pressed == 'A'):
            self.lcd.rect(self.lcd.width - 45, self.lcd.height - 55, 40, 50, self.lcd.colour(0,200,0))
            self.lcd.printstring("A", self.lcd.width - 32, self.lcd.height - 190, 3, self.lcd.colour(0,255,255))
        else:
            self.lcd.rect(self.lcd.width - 45, self.lcd.height - 55, 40, 50, self.lcd.colour(0,200,0))
            self.lcd.printstring("A", self.lcd.width - 32, self.lcd.height - 190, 3, self.lcd.colour(0,255,0))
        
        if (pressed == 'B'):
            self.lcd.rect(self.lcd.width - 45, self.lcd.height - 105, 40, 50, self.lcd.colour(0,200,0))
            self.lcd.printstring("B", self.lcd.width - 32, self.lcd.height - 140, 3, self.lcd.colour(0,255,255))
        else:
            self.lcd.rect(self.lcd.width - 45, self.lcd.height - 105, 40, 50, self.lcd.colour(0,200,0))
            self.lcd.printstring("B", self.lcd.width - 32, self.lcd.height - 140, 3, self.lcd.colour(0,255,0))
        
        if (pressed == 'X'):
            self.lcd.rect(self.lcd.width - 45, self.lcd.height - 155, 40, 50, self.lcd.colour(0,200,0))
            self.lcd.printstring("X", self.lcd.width - 32, self.lcd.height - 90, 3, self.lcd.colour(0,255,255))
        else:
            self.lcd.rect(self.lcd.width - 45, self.lcd.height - 155, 40, 50, self.lcd.colour(0,200,0))
            self.lcd.printstring("X", self.lcd.width - 32, self.lcd.height - 90, 3, self.lcd.colour(0,255,0))
            
        if (pressed == 'Y'):
            self.lcd.rect(self.lcd.width - 45, self.lcd.height - 205, 40, 50, self.lcd.colour(0,200,0))
            self.lcd.printstring("Y", self.lcd.width - 32, self.lcd.height - 40, 3, self.lcd.colour(0,255,255))
        else:
            self.lcd.rect(self.lcd.width - 45, self.lcd.height - 205, 40, 50, self.lcd.colour(0,200,0))
            self.lcd.printstring("Y", self.lcd.width - 32, self.lcd.height - 40, 3, self.lcd.colour(0,255,0))
                
    
    def time(self):
        return utime.gmtime()
    
    
    def clr(self):
        self.dispNone = False
        
    
    def stop(self):
        self.terminate = True
        self.queue.enqueue(MainApp(self, "MAIN"))
    
    
    def wait(self, t=0):
        utime.sleep(t if t else 1)
    
    
    def ask_to_start(self, app):
        self.terminate = True
        self.queue.enqueue(app)
        return
        
        
    def __run_process__(self, app):
        #Process header
        self.terminate = False
        self.id = "".join([chr(random.randint(97, 122)) for i in range(10)])
        pressed = ""
        tick = 0
        app = app.run_app_commands(self)
        
        #Main thread
        while (not self.terminate):
            print(tick)
            
            if (self.terminate):
                print(self.id, "terminated")

            
            self.__frame__(app.name+" t="+str(round(tick, 5)), pressed)
            
            app.cont(tick, pressed)
            self.lcd.show()
            
            if (self.A.value() == 0):
                pressed = "A"
            elif (self.B.value() == 0):
                pressed = "B"
            elif (self.Y.value() == 0):
                pressed = "Y"
            elif (self.X.value() == 0):
                pressed = "X"
            elif (self.up.value() == 0):
                pressed = "up"
            elif (self.down.value() == 0):
                pressed = "down"
            elif (self.left.value() == 0):
                pressed = "left"
            elif (self.right.value() == 0):
                pressed = "right"
            elif (self.ctrl.value() == 0):
                pressed = "ctrl"
            else:
                pressed = ""
            tick+=0.01
        
        self.__frame__("window::executed", pressed)
        return "EXIT 0"