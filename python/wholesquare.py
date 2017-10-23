import math

def mysolution(A,B):
    def issqr(i):
        i = math.sqrt(abs(i))
        if i - int(abs(i)) == 0:
            return i;
        return 0
    for x in range(A,B+1):
        if issqr(x): print(x)
    return

def solution(A, B):
    def issqr(i):
        for x in range(1,int(abs(A/2))):
        return x*x in list(range(A, B+1))
        
    res = 0
    for x in range(A,B+1):
        if issqr(x): res += 1
    return res


mysolution(-4, 17)
print("Sol", solution(-4, 17))