class MyClass:
    counter = 0

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod_increment(self):
        self.counter +=1
        return 'static method called'


c = MyClass

c.staticmethod_increment(c)

c.staticmethod_increment(c)

f = MyClass



print(f"We love steve {c.counter} many times")