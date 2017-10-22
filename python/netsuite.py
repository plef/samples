#!/usr/bini/python
__doc__ = """
This sample program should accept a sequence of numbers on input, and produce
sequence of these numbers wihtout duplicate numbers.

E.g.: 1,2,2,3,3,4 -> 1,2,3,4

Usage: %s <sequence>
""" % (__file__)

import sys

def main(seq):
   print type(seq)
   if len(seq) == 0:
	print __doc__
	return
   seq.sort()

   res = []
   for x in seq:
	 if not x in res: res.append(x)
   print repr(seq) + " -> " + repr(res)

l = [] if len(sys.argv) < 2 else list(x for x in sys.argv[1] if x != ',')
print type(sys.argv), sys.argv
main(l)
