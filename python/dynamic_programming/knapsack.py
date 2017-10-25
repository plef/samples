"""
    The Knapsack Problem
    
    See http://www.geeksforgeeks.org/solve-dynamic-programming-problem/
    
    Well, the knapsack problem exactly is at
    http://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/
    
    Here, I solve a little bit simplier form of it:
    
    Having a possiblity to take given weight of items N, determine all orders
    of items form set S, which can a man take into his knapsack so that the
    total weight of items is >equal< to given maximum weight.
    
    In other words, there are numbers in set S, the goal is to present all
    sum expressions equal to N, using the numbers form this set. Each number
    can be used anytimes, the order of items in sum expressions depends.
    
    E.g. N = 6
         S = [1,3,5]
         
    There is total 8 sums that make the 6 from 1,3,5:
    
    1+1+1+1+1+1
    1+1+1+3
    1+1+3+1
    1+3+1+1
    3+1+1+1
    3+3
    1+5
    5+1
    
    After several hours in the evenging, I got this idea to express the correct
    results in a tree. When I was imaginating that tree in my head, it became
    clear that the numbers from S are values of the tree edges. The tree starts
    from a root, continues over all possible valuable edges, until the length
    of each of the paths does not go over N. In those leafs, where the path length
    equals to N exactly, we have found the correct path.
    
    And voila! Next morning, during 10mins, I set up the depth walking through
    the tree by the correct condition (>=), added the cut condition marking correct
    result (N == 0) and saw it was all done! What a mistery previous evening, while
    it's actually just as easy!
    
"""

def knapsack(S, N):
    R = []

    # Walk the imaginery tree of ways how to represent Ni through a sum
    # of numbers from set S. Walk in depth, not wide.
    # In the imaginery tree, each edge has a value equal to given number
    # used in the sum. So, at the root node, the path traversed has length 0,
    # and in the leaf nodes, the length is equal to Ni (or grater than Ni,
    # which is not accepted result).
    # The path traversed is stored wihtin Pi, its length is immediately
    # recoverable form Ni
    def walk(Ni, Pi):
        if Ni == 0 and len(Pi):
            R.append(Pi)
            print(Pi)
            return
        for n in S:
            if Ni >= n:
                walk(Ni-n, Pi + [n])       
        
    walk(N,[])
    return R

# If we would like to count only how many sum exist
# Note: this can be memoized, as we repeatedly solve some numbers
# with _solve() in recursions.
# This is taken right from G4G portal, well they use Ni-n from N, I am going
# opposite way using Ni+n from 0, but otherwise it's equal algorithm.
# Note: using memoization, it's less complex than my knapsack() walking the tree
# (but that one could be also memoized of course)
# Note: the cache size itself depends on N, to stay safe, it shold grow dynamically according to needs, i.e. value of Ni+n 
# Note: it does not count with negative numbers (problem for memoization cache size)
# Note: it's easy to extend it so that it will collect also the sum expressions
#
# Memoization is generally slower than tabulation, also the code for it is easier, and
# it's generally easier to think of that code. See nice table of comparison of them at
#   http://www.geeksforgeeks.org/tabulation-vs-memoizatation/
#
def knapsackcount(S,N):
    memsz = N+sum(S)
    mem = [None]*memsz # the cache of memoization
    def _solve(Ni):
        nonlocal mem
        if Ni == N:
            return 1
        if Ni > N:
            return 0        
        sum = 0
        for n in S:
            if not (Ni+n) in mem:
                mem[Ni+n] = _solve(Ni+n) # memoize it
            sum += mem[Ni+n]
        return sum
            
    return _solve(0)

S = [1,3,5]
print ("Expressing all possible sums eaual to N, using numbers from ", S)
for N in range(0,7):
    print ("N: ", N)
    tot = len(knapsack(S, N))
    print("Total: %d (printed %d)" % (knapsackcount(S, N), tot))