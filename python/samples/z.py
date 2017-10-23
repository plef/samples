class ClsBase:
    def foo(self):
        print ("in base")
        
class ClsMain(ClsBase):
    def foo(self):
        print ("in derived")

# If we remove overload from derived (subclass), there is still the base version in superclass
m = ClsMain()
m.foo()
mainFooBkp = ClsMain.foo
del (ClsMain.foo)
m.foo()

# removing the base version while keeping overloaded version is also legal
ClsMain.foo = mainFooBkp
m.foo()
del (ClsBase.foo)
m.foo()


class Vect:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __repr__(self):
        return ("v = (%r, %r)" % (self.a, self.b))
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return ("[%r, %r]" % (self.x, self.y))
    
    def move(self, vect, t):
        self.x = vect.a*t + self.x
        self.y = vect.b*t + self.y
        return self
    
    
v = Vect(1,1)
p = Point(1,0)
print (v, p)
print (p.move(v, 3))

# Cool, this formatting... we can use .(dot) access on passed object directly in the format text!
# ... and save the length of the args to format() thatnk to it! And make the forma tstring more readable!
# AWESOME
print ("Point is at {0.x} on x-axis and {0.y} on y-axis. This string required only one argument to format()!".format(p))
