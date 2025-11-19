class AVLTree:
    class AVLNode:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()
        
        def __str__(self):
            return str(self.data)

        def setHeight(self):
                a = self.getHeight(self.left)
                b = self.getHeight(self.right)
                self.height = 1 + max(a,b)
                return self.height

        def getHeight(self, node):
            return -1 if node == None else node.height

        def balanceValue(self):      
            return self.getHeight(self.right) - self.getHeight(self.left)

    def __init__(self, root = None):
        self.root = None if root is None else root

    def add(self, data):
        self.root = self._add(self.root, data)

    def _add(self, root, data):
        if root is None:
            return self.AVLNode(data)
        else:
            if int(data) < int(root.data):
                root.left = self._add(root.left, data)
            else:
                root.right = self._add(root.right,  data)
                
            root = self.rebalance(root)
            return root
        
    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, root, data):
        if not root:
            return root  # not found

        if int(data) < int(root.data):
            root.left = self._delete(root.left, data)
        elif int(data) > int(root.data):
            root.right = self._delete(root.right, data)
        else:
            # Case 1: no child
            if not root.left and not root.right:
                return None
            # Case 2: one child
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Case 3: two children → find inorder successor
            else:
                successor = self._minValueNode(root.right)
                root.data = successor.data
                root.right = self._delete(root.right, successor.data)

        # update height + rebalance
        root = self.rebalance(root)
        return root

    def _minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

        

    def rotateLeftChild(self, root) :
        newroot = root.right
        root.right = newroot.left
        newroot.left = root

        root.setHeight()
        newroot.setHeight()

        return newroot


    def rotateRightChild(self, root) :
        newroot = root.left
        root.left = newroot.right
        newroot.right = root

        root.setHeight()
        newroot.setHeight()

        return newroot
    
    
    def rebalance(self, root):
        root.setHeight()
        balance = root.balanceValue()

        if balance > 1:
            if root.right.balanceValue() < 0:
                root.right = self.rotateRightChild(root.right)
            root = self.rotateLeftChild(root)

        elif balance < -1:
            if root.left.balanceValue() > 0:
                root.left = self.rotateLeftChild(root.left)
            root = self.rotateRightChild(root)

        return root


    def postOrder(self):
        print("AVLTree post-order : ", end='')
        self._postOrder(self.root)
        print()

    def _postOrder(self, root):
        if root:
            self._postOrder(root.left)
            self._postOrder(root.right)
            print(root.data, end=' ')

    def printTree(self):

        self._printTree(self.root)

        print()

    def _printTree(self, node , level=0):

        if not node is None:

            self._printTree(node.right, level + 1)

            print('     ' * level, node.data)

            self._printTree(node.left, level + 1)

avl1 = AVLTree()

inp = input('Enter Input : ').split(',')

for i in inp:

    if i[:2] == "AD":

        avl1.add(i[3:])

    elif i[:2] == "PR":

        avl1.printTree()

    elif i[:2] == "PO":


        avl1.postOrder()