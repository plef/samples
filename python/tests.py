# I guess this is most easy to reverse string:
# iterate backwards to produce a reversed copy of input.
# It is however O(n), but with overhead given by + operator
# which concatenates into new object in each iteration. I hope
# it's more clever than strcat() in C++, which iterates entire string
# to find a point of attachement.
def srev(s):
    o = str()
    for i in range(len(s)-1,-1, -1):
        o += s[i]
        pass
    return o

# If one would like to sovle it like i C++ etc in O(n/2),
# it is possible just via mutable object, as strings are immutable in  Python.
# So we got to convert input to list() and on return, convert th elist back
# to string by means of str.join() method.
def srev2(s):
    sz = len(s)
    o = list(s)
    for i in range(0, int(len(s)+1/2)):
        o[sz-i-1] = s[i]
    return str().join(o)

# But WOW. There is st called "extended slicing" as of 2.4!
# https://docs.python.org/2/whatsnew/2.3.html#extended-slices
def easyrev(s):
    return s[::-1]
def evenslice(s):
    return s[::2]
def oddslice(s):
    return s[1::2]

# BRUTAL, how to replace items at given indices with a single line of code?
def replace(seq, slicepattern, replseq):
    # Limitation: When assigning to an extended slice, the list on the right
    # hand side of the statement must contain the same number of items as the
    # slice it is replacing:
    assert(isinstance(slicepattern, slice))
    #assert(len(replseq) == (slicepattern.stop-slicepattern.start)/slicepattern.step)
    seq[slicepattern] = replseq
    return seq

hello = "Hello World!"
print(list(range(0,len(hello))))
print("{0}:{1}".format(hello,len(hello)))
print(srev(hello))
print(srev2(hello))
print(easyrev(hello))
print(evenslice(hello))
print(oddslice(hello))

# test of replace by means of slice object
l = list(range(10))
l[::2] = list("x"*5)
print(l)
l2 = l
replace(l2, slice(0,10,2), list("x"*5))
print(l2)
assert(l==l2)

# so...
def f():
    global hello
    print(str().join(replace(list(hello), slice(0,len(hello),2), list("-"*int((len(hello)+1)/2)))))
    
f()
hello += "-!-"# also check it works for different length (i.e. against the calc of (len(s)+1/2))
f()