

class myClass:

    def __init__(self):
        pass
    def hello(self):
            x=1+2
            return x
    def hello2(self):
        b=self.hello()+4
        return b



m=myClass()
print(m.hello2())