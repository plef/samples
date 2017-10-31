# file io, stdin

# pyhton 2.had raw_input() to read string, intpu() to read a evaluate string from input as a python code
# python3 has only input() to read string, eval() can be used to evaluate it.
n = eval(input("Enter python expression to evaluate, e.g 'max(1,3+5)' or anyting: "))

print (n)

fn = input("Enter filename to create/open:")
try:
    f = open(fn, "a")
except:
    print ("Could not create/open file", fn)
else:
    try:
        f.write(str(n))
        print("Evaluated input '{0}' writen to file '{1}' succesfully".format(n, fn))        
    except:
        print("Could not write the file", fn)
        raise
    finally:
        f.close()
        print("File closed. Now will read it:")        
        f = open(fn, "r")
        while True:
            s = f.read(10)
            if s: print (s)
            else: break
        f.close()
        
# More simple work with a file is done via with, it handles clsoe() automatically
# even if exception occurs:
with open("test.txt") as f:
    # Can iterate text files by lines also simplier:
    for line in f:
        print("Line of test.txt:", line)
    
# Reading from stdin cab be made via sys.stdin object
import sys

print ("stdin input:")
for s in sys.stdin.readline():  # Note: Thonny tells me only readline() is supported, and waits for some input, Enter ends it
    print (s)
