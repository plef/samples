class RBNode:
    def __init__(self, val = None, red = False):
        self.value = val
        self.isRed = red
        self.child = [None, None]
        
    def __repr__(self):
        return ("R" if self.isRed else "B") + "," + repr(self.value)
    
    def isRed(self):
        return not root == None and not self.isRed
    
class RBTree():
    root = None
    
    def contains(self, val):
        return not self.find(val) == None

    def find(self, val):
        def _f(root, val):
            if not root:
                return None
            if val == root.value:
                return root
            if val < root.value:
                return _f(root.child[0], val)
            if val > root.value:
                return _f(root.child[1], val)
            return None
        
        return _f(self.root, val)

    def balance(self, node):
        """
        Each insert brings possiblity of introducing RedViolation. Therefore, this method is
        used to rebalance the subtree with RedViolation to be proper RB subtree.
        See https://www.cs.cornell.edu/courses/cs3110/2014sp/lectures/11/red-black-trees.html
        for logic of the code:
        
        let balance = function
            Black, z, Node (Red, y, Node (Red, x, a, b), c), d            
          | Black, z, Node (Red, x, a, Node (Red, y, b, c)), d
          | Black, x, a, Node (Red, z, Node (Red, y, b, c), d)
          | Black, x, a, Node (Red, y, b, Node (Red, z, c, d)) ->
              Node (Red, y, Node (Black, x, a, b), Node (Black, z, c, d))
          | a, b, c, d -> Node (a, b, c, d)
        """           
        if node.isRed:
            return node
        doit = False
        if node.child[0] and node.child[0].isRed and \
           node.child[0].child[0] and node.child[0].child[0].isRed:
            z = node.value, y = node.child[0].value, x = node.child[0].child[0].value
            a = node.child[0].child[0].child[0]
            b = node.child[0].child[0].child[1]
            c = node.child[0].child[1]
            d = node.child[1]
            doit = True
        if node.child[0] and node.child[0].isRed and \
           node.child[0].child[1] and node.child[0].child[1].isRed:
            z = node.value
            x = node.child[0].value
            y = node.child[0].child[1].value
            a = node.child[0].child[0]
            b = node.child[0].child[1].child[0]
            c = node.child[0].child[1].child[1]
            d = node.child[1]
            doit = True
        if node.child[1] and node.child[1].isRed and \
           node.child[1].child[0] and node.child[1].child[0].isRed:
            x = node.value, z = node.child[1].value, y = node.child[1].child[0].value
            a = node.child[0]
            b = node.child[1].child[0].child[0]
            c = node.child[1].child[0].child[1]
            d = node.child[1].child[1]
            doit = True
        if node.child[1] and node.child[1].isRed and \
           node.child[1].child[1] and node.child[1].child[1].isRed:
            x = node.value, y = node.child[1].value, z = node.child[1].child[1].value
            a = node.child[0]
            b = node.child[1].child[0]
            c = node.child[1].child[1].child[0]
            d = node.child[1].child[1].child[1]
            doit = True
        if doit:
            newNode = RBNode(y, red=True)
            newNode.child[0] = RBNode(x, red=False)
            newNode.child[0].child[0] = a
            newNode.child[0].child[1] = b
            newNode.child[1] = RBNode(z, red=False)
            newNode.child[1].child[0] = c
            newNode.child[1].child[1] = d
            return newNode
        return node

    def insert(self, val):
        """
        Inserting black always causes BlackViolation, so insertion of red is preferred. \
        That makes possible need to rebalance, but RedRebalance is simplier than BlackRebalance.
    
        See https://www.cs.usfca.edu/~galles/visualization/RedBlack.html for visualisation.
        
        See https://www.cs.cornell.edu/courses/cs3110/2014sp/lectures/11/red-black-trees.html
        for logic of the code:
        
        let insert x s =
          let rec ins = function
            Leaf -> Node (Red, x, Leaf, Leaf)
          | Node (color, y, a, b) as s ->
              if x < y then balance (color, y, ins a, b)
              else if x > y then balance (color, y, a, ins b)
              else s in
          match ins s with
            Node (_, y, a, b) ->
              Node (Black, y, a, b)
            | Leaf -> (* guaranteed to be nonempty *)
                failwith "RBT insert failed with ins returning leaf"           
        """
        # As long as parameters are passed by value, changes to them do not
        # affect the object being refered by them, unless a class/instance
        # method is used to change its state internally. So, I'd move _ins()
        # into RBNode to avoid the ugly return value assignments from it.
        def _ins(node):
            if not node:
                # Slot for new child found; always insert Red
                return RBNode(val, red=True)
            if val < node.value:
                newNode = RBNode(node.value, node.isRed)
                newNode.child[0] = _ins(node.child[0])
                newNode.child[1] = node.child[1]
                return self.balance(newNode)
            if val > node.value:
                newNode = RBNode(node.value, node.isRed)
                newNode.child[1] = _ins(node.child[1])
                newNode.child[0] = node.child[0]
                return self.balance(newNode)
            return node
        self.root = _ins(self.root)
        self.root.isRed = False
        print("INS", val, self)
        pass
    
    def delete(self, val):
        print("DEL", val, self)
        pass
    
    def size(self): # up to 2^depth() - 1
        return 0
    
    def bdepth(self):
        return 0
    
    def depth(self):
        return 0
    
    # Check the tree strucutore conforms to RB tree definition
    # - root is black (not required)
    # - node is either black or red
    # - if node is red, nor parent nor child can be red
    # - path from root to any None node must be of same black length (count of black nodes) = the balance rule
    # - it's a binary tree, so for each node, left subtree contains lower values than, right
    # subtree greater values than the node
    def validate(self):        
        def validate_color(root):
            if not root: return True
            if root.isRed and all(map(lambda node: node and node.isRed, root.child)): # both children None or black
                raise Exception("RedViolation", root)
                return False
            return all(map(validate_color, root.child)) # validate both children
        def validate_btree(root):
            if not root: return True
            if (root.child[0] and root.child[0].value >= root.value) or \
               (root.child[1] and root.child[1].value <= root.value):
                raise Exception("BTreeValueViolation", root)
                return False
            return all(map(validate_btree, root.child))
        def validate_bdepth(root):
            if not root: return 1
            ld = validate_bdepth(root.child[0])
            rd = validate_bdepth(root.child[1])
            if all([ld,rd]) and not rd == ld:
                raise Exception("BlackDepthViolation", root, ld, rd)
                return False
            return ld if root.isRed else ld + 1
        
        return validate_color(self.root) and \
               validate_btree(self.root) and \
               validate_bdepth(self.root)
    
    def __repr__(self):
        def walk(node):            
            if not node:
                return "[Nil]"
            #print(node, id(node), id(node.child[0]))
            assert(not node == node.child[0])
            assert(not node == node.child[1])            
            s = "(%s,%s,%s)" % (repr(node), walk(node.child[0]), walk(node.child[1]))
            return s
        s = walk(self.root)
        return s
    
    
# --------------------------------------------------------------------------------    
    
rb = RBTree()
print("Tree:", rb)
for v in (5,1,3,4,0):
    rb.insert(v)
    print("FIND ", v, rb.find(v))
    print ("VALID") if rb.validate() else print ("!INVALID!")  

print ("Final Tree is valid:", rb)
