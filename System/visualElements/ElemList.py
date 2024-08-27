from System.visualElements.BigElem import BigElem
from System.visualElements.Elem import Elem
from System.visualElements.ElemInfo import ElemInfo
from System.visualElements.KeyBoard import KeyBoard
from System.visualElements.KeyBoard import NumBoard
from System.visualElements.ModalElem import ModalElem
from System.visualElements.TextElem import TextElem

class ElemList:
    def __init__(self, lcd, elemslist):
        self.list = elemslist
        self.lcd = lcd
        self.set_of_selected = {}
    
    def mark(self, selected):
        self.set_of_selected.add(selected)
    
    def select(self, id):
        print(id)
    
    def add(self, elem):
        self.list.append(elem)
        
        
    def render(self, i_p = 0, j_p = 0, ctrl = None, show_cursor = 0, render_modal = ""):
        set_of_skips = set()
        response_from_rendered = None
        for i in range(len(self.list)):
            elem = self.list[i]
            content = elem.content
            x = 10 if i < 4 else 100
            y = (i*40)%+160 + 40
            
            if (y in set_of_skips):
                y+=40
            
            if render_modal:
                self.lcd.printstring(str(render_modal), 60, 120, 3, self.lcd.colour(0, 255, 0))
                continue
            
            if (elem.borders):
                self.lcd.rect(x, y, 80, 40, self.lcd.colour(0,255,0))
                
            if (isinstance(elem, ElemInfo)):
                elem.render(y)
            elif (isinstance(elem, Elem)):
                self.lcd.printstring(" " + content, x+5, y + 25, elem.size, self.lcd.colour(0,255,0))
            
            if (isinstance(elem, BigElem)):
                self.lcd.rect(10, y, 180, 40, self.lcd.colour(255,0,0))
                self.lcd.printstring(" " + content, x+20, y + 5, elem.size, self.lcd.colour(0,255,0))
            
            if (isinstance(elem, KeyBoard)):
                response_from_rendered = elem.render(i_p, j_p, ctrl, show_cursor)
            elif (isinstance(elem, NumBoard)):
                response_from_rendered = elem.render(i_p, j_p, ctrl, show_cursor)
            elif (isinstance(elem, TextElem)):
                st = ''
                last_index = 0
                for i in range(len(elem.content)):
                    st+=elem.content[i]
                    if (len(st) == 20):
                        self.lcd.printstring(" " + st, x, y + 5 + i, elem.size, self.lcd.colour(0,255,0))
                        st = ''
                    last_index = i
                if (st):
                    self.lcd.printstring(" " + st, x, y + 5 + last_index + 1, elem.size, self.lcd.colour(0,255,0))
                    
                self.lcd.rect(10, y+10, 180, last_index+8, self.lcd.colour(0,0,255))
        
        return response_from_rendered
