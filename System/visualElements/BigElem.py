import random
class BigElem:
    def __init__(self, lcd, content):
        self.id = "".join([chr(random.randint(97, 122)) for x in range(10)])
        print(self.id+" "+content)
        self.content = content
        self.borders = False
        self.size = 2
