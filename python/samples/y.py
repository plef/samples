"""Tento string prijde do __doc__ modulu y.py, jako dokumentacni retezec modulu
 Tady pokracuje.
 
 Modul na hrani v Pythonu."""

import math
import sys

print (sys.version)

n = 4
a = [ ]

# Machinery

def circle(r):
    return (float(r)**2*math.pi)
    
def fact(n = 1, dim = 1):
    return 1 if n < 2 else n * fact(n-dim, dim)

def fillup(ar, n):
    if n > 0: fillup(ar, n - 1)
    if not n in ar: ar.append(n)
    

class Clsfoo:
    "Toto je drida na hrani. Tento retezec se uklada do __doc__ teto tridy"
    # Class variable, like a static, class variable in a C++ class - shared among instances!
    # .. BUT!!! To change the shared object, remeber to refer it via Clsfoo, not the class
    # object instance, which will be either newly defined, if used at the left side of an assignment,
    # or undefined (raising error) if used as rvalue!
    __quack_counter = 0
    __last_reseter = None
    
    def __init__(self, name = None):
        self.name = name
        
    def reset(self):
        Clsfoo.__quack_counter = 0
        Clsfoo.__last_reseter = self        
    
    def quack(this, x, y):
        Clsfoo.__quack_counter += 1
        print ("Quack {a} and {b} is {ab}".format(a=x, b=y, ab=x + y))
        print (repr(this))
    
    # to know repr() built-in on how to print this class object, define __repr__:
    def __repr__(self):
        if Clsfoo.__last_reseter != None: print ("Quacking was reset by %s" % (Clsfoo.__last_reseter.name))
        return ("Quacked so far: %d" % (Clsfoo.__quack_counter))
        
class Clsbar(Clsfoo): pass

class Clsempty: pass


def main():
    factorials = {0:1, 1:1}
    surfaces = {}
    dim = 2
    for n in a:
        surfaces[n] = circle(n)
        factorials[n] = fact(int(n), dim)
    print ("Circle surfaces:", surfaces)
    print ('Factorials (by {0}): {1}'.format(dim,factorials))
    

# The fun part
print ("n: ", n)
fillup(a , int(n))
print ("ar: ", a)

main()
#circle(n)
#print (n, "! = ", fact(int(n)))

foo = Clsbar()
foo.quack(1, 2)
foo.quack("1","2")
bar = Clsbar
# bar is referring to class, not class instance object:
if bar is Clsfoo: print ("bar is Clsfoo")
else:
    print (type(bar))
# bar.quack(3,4) .. error, missing 3rd param - could be only bar.quack(foo, 3,4)
bar.quack(foo, 3,4)


print ("""Bye bye
...Mr. 'merican pye.""")

astr = "abcdefgh"
print (astr[0:-3], astr[3], astr[0:-10], astr[:2])
print(astr[::2], astr[::-1])

print (max(("1","2","3")))
print (math.exp(1), round(math.e, 2))

print ("fact(), i.e. with default values: %d" % (fact()))

if ("python").find("th", 0, 3): print ("ok".capitalize())
print("python".find("ooo"))

# string is separator for elements in sequence passed to join(). Separator seems to be never used after last element of that sequence
aseq = ("a","bc","d") # or [x,...] or {x:y,...}
print (".".join(aseq))
print ("012".join("abc"))
print ("012".join("a"))
print ("012".join(["abc", "def"]))
print ("012".join(("abc", "+-*", ".")))
print ("012".join({"ab":"+-", "cd":"01"}))
print ("+".join(list(map(str,[1.4, 4.21])))) # in 2.7, map reruns list, in 3.6 it returns iterator, so its very different what we get from map() across versions

print ("HELLO".ljust(10,"-").rjust(15)) # the fill character must e 1 character long, so passing e.g. "--" produces error

if 0:
    # Only in Python 3.x
    # When we run above program, it produces following result −
    # th3s 3s str3ng 2x1mpl2....w4w!!!
    from string import maketrans   # Required to call maketrans function.
    intab = "aeiou"
    outtab = "12345"
    trantab = maketrans(intab, outtab)
    astr = "this is string example....wow!!!"
    print (astr.translate(trantab))
    pass # Need some thing to visually end a python suite? 'pass' can be used. Or comment (#) 
    
print ("a b c d".split(" ",2))

astr = """abc
def
ghi
jkl"""

print (astr.splitlines())
print (astr.splitlines(0))
print (astr.splitlines(1))
print (astr.splitlines(2))
print (astr.splitlines(50))

# Like rjust(), but it's intended for numbers, so it uses "0" as fillchar, and it respects sign ("-") for negative numbers at the right place
print ("-23".zfill(5))

print ("aBcD0+-.\n".swapcase())

mseq = [1,2,3,7,8]
mseqi = [4,5,6]
mseq[3:] = mseqi + mseq[len(mseqi):]  # BRUTAL!!! Slicing can be realized via any expression, like function call ? :D
print (mseq)

def cmp_python3(a, b):
    return (a > b) - (a < b)

# In case of coercion betw. int and str, in python 2 if operands are different type,
# the name of type determines the result of comparison: 100 < "2" is True, bec. 'string' > 'int'

print (cmp_python3([0], [0]))
print (cmp_python3([0], [1]))
print (cmp_python3([1], [0]))
#print (cmp_python3([0], ["0"]))          # error - cannot compare int and str
print (cmp_python3([0], [1, "0"]))
print (cmp_python3([0, "1"], [1, "0"]))
#print (cmp_python3([1, 1], [1, [1]]))    # error - compare int and list
print (cmp_python3("1", "02"))
print (cmp_python3("1", "12"))
print (cmp_python3("1", "10"))
print (cmp_python3("100", "2"))

print (sorted("210"))
print (sorted("210cab"))
#print (sorted(["x01", 210, "cab"]))       # error - compare int and str

print (True)
print (None)
print ({}, [], ())
print (0 == 0)
#print (None < None)    # error, NoneType cannot be orderd with anything else, nor with NoneType
#print (False == 0 < True < {} < [] < ()) .. only in python 2, whre it compares different types (where cannot interpret into number) by name, i.e. 'dict' < 'list' < 'string' < 'tuple'
print (False == 0 < True)  # True, False, 0 ... all is numeric type

print ("['abc'] < ['x'] ? ", ["abc"] < ["x"]) # ... does not compare lengths, it sees 'a' < 'x' here!
print ("['abc', 'a'] < ['x'] ?", ["abc", "a"] < ["x"]) # ... likewise...
print ("abc" < "x")

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print (sorted(student_tuples, key=lambda student: student[2]))   # sort by age

from functools import total_ordering

@total_ordering
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    # Define how print() should represent this object
    def __repr__(self):
        return repr((self.brand, self.year))
    
    # .. or, if imported functools.total_ordering and define __eq__ and one of 'rich comparison methods' (e.g. __lt__)
    # then the @total_ordering decorator adds the rest of 'rich comparison methods' and the class becomes "orderable"
    def __eq__(self, other): return self.year == other.year
    def __lt__(self, other): return self.year < other.year
    
car_objects = [
   Car("Ford", 1988),
   Car("Alfa Romeo", 1977),
   Car("Pontiac", 1966)
]
print (str(car_objects))
print ((car_objects,))
print (sorted(car_objects, key=lambda car: car.brand))
print (sorted(car_objects)) # ... now, thanks to @total_ordering
   
s = ["abc"]
s.extend("de")
print (s)

# tuples... to make tuple of 1 element, comma must postifx it. Parentheses are opt.
tuple1 = 5,
tuple1 = (5,)

print (tuple1, 3, (3,))
print (4,)

# to fill a sequence, a 'sequence-comprehension' can be used:
print ([x for x in "abc"])

tupfromlist = tuple([1,2,3, "abc"])
print (tupfromlist)

# dicts: keys must be immutable objects (string, number or tuple), so e.g. ["abc"] cannot be a key, while "abc" can
# if more identical keys occur, last assignment wins

dict = {1:"a", 2:"b", 1:"c"}
print (dict, dict[1])
print (type(True))
print (dict.get(4, None))


import time, calendar

lt = time.localtime(time.time())
print ("\n", time.asctime(lt), "\n", calendar.month(lt[0], lt[1]))


def sum(*ops):
    tot = 0
    for op in ops: tot += op
    return tot

mysum = sum

print (sum())
print (sum(0))
print (sum(1))
print (sum(1,2))
print (sum(1,2,3))
print (mysum(1,2,3))

for s in dir():
    if "__" in s and s in globals().keys(): print (s.ljust(15), globals()[s])

def func():
    "nothing"
    myvar = "hello"
    print ("Locals: ", locals())

func()


# (!) finally: cannot be used at the same time with else:
# (!) finally: does not eat the exception; it will re-raise it for higher level handling
# (!) except: wihtout exception tyupe arguments msut be th elast statement in list of except <E>: clauses,
# as it is the most generic clause, even more genereic than except Exception:, which captures
# the top parent af all exceptions.

try:
    x = 5/0
except IOError: pass 
except Exception as e:
    print ("Ooops! ... ", e)
except: pass    
else:
    print ("Fine")

foo.quack(1,2)
gunman = Clsfoo("Gunman")
gunman.reset()
print ("Foo repr: ", foo)
print ("Gunman repr:", gunman)
#print (Clsfoo.__last_reseter) # error ... __<attrname> makes the attr hidden to outside world
print (Clsfoo._Clsfoo__last_reseter) # ... however, if I know its name, it can be still referred since Python internally just renames such an attribute using parent class name

# Hmm, if I add a new attribute to object, does tha timpact entire class?
# ===> NO!
gunman.has_weapon = True
print ("Has foo got a weapon?", hasattr(foo, "has_weapon"))
print ("Has gunman got a weapon?", hasattr(gunman, "has_weapon"))

# Hm. And can I add class vairables?
# ===> YES OF COURSE!!
Clsfoo.has_head = True
print ("Has Clsfoo a head?", hasattr(Clsfoo, "has_head"))
print ("Has foo got a head?", hasattr(foo, "has_head"))
print ("Has gunman got a head?", hasattr(gunman, "has_head"))

# Wow. I can add even methods... AWESOME!!!
# ... BUT, it seems that if adding to instance, only lambda can be removed. 
gunman.shoot = lambda: "BANG!"
print ("Can gunman shoot?", hasattr(gunman, "shoot"))
print ("Can foo shoot?", hasattr(foo, "shoot"))
print (gunman.shoot())
gunman.shoot = lambda s: ("BANG!" + s)
print (gunman.shoot("BANG!!!"))
del gunman.shoot
#del gunman.quack # Error, there's no class instance attribute 'quack'
#... to remove quack(), class object must be used for del


# Hey, what if NOW redefine quack() for the class?
# (not using lambda since lambda cannot use commands, only expressions; lambda is an expression in practice)
def newquack(object):
    print ("QUACK! by", object.name)
    
Clsfoo.quack = newquack
#foo.quack(1, 2)   # ... error - method has different arg list now
#gunman.quack(1, 2) # ... dtto
foo.quack()
gunman.quack()

# Can I do this at object-level?
# ... NOPE, BUT....we can actually add instance variable, which happens to be a callable object. In this case,
# be aware that Python does NOT pass the *self* reference in the call, so it must be mentioned explciitly!
gunman.quack = newquack 
gunman.quack(gunman) # 'object' in 'newquack' definition is superfluous; but must be present in the call of 'quack', as the funct def requires it; or if we actually need it.
foo.shoot = newquack
foo.shoot(foo)
del foo.shoot # ok, shoot is an attr
del gunman.quack # ok, quack is Clsfoo method, but we've added attr of same name, so we can remove it again
gunman.quack() # ...and here, the original class method is accesible again

# Huh, ok. So gunman is not a duck! Can I delete it?
# ... NO! Methods can be removed only for entire classes, not for their objects, unlike instance variables
del Clsfoo.quack
#del Clsfoo.shoot # error ... there no such method in Clsfoo

# Ok, so can I remove instance variable?
# ... YES
del gunman.has_weapon


print ("""In summary, it seems that variables and methods can be added, re-assigned or removed at any time for
a class. For objects of this class, a form of functors can be added, re-assigned or removed by means of object
attributes. BUT, these are not true class methods, they are still common instance variables (attributes), only
that they are callable. The difference shows up when we find out that we have no *self* in these functors passed
automatically - it must be passed explicitly, in each call.""")