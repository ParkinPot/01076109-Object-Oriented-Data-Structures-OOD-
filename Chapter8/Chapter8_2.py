class AVLTree:
    class AVLNode:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()

        def __str__(self):
            return str(self.data)

        def setHeight(self):
            a = self.getHeight(self.left)
            b = self.getHeight(self.right)
            self.height = 1 + max(a, b)
            return self.height

        def getHeight(self, node):
            return -1 if node is None else node.height

        def balanceValue(self):
            return self.getHeight(self.right) - self.getHeight(self.left)

    def __init__(self, root=None):
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
                root.right = self._add(root.right, data)

            root = self.rebalance(root)
            return root

    def rotateLeftChild(self, root):
        newroot = root.right
        root.right = newroot.left
        newroot.left = root

        root.setHeight()
        newroot.setHeight()

        return newroot

    def rotateRightChild(self, root):
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

    def printTree(self):
        self._printTree(self.root)
        print()

    def _printTree(self, node, level=0):
        if node is not None:
            self._printTree(node.right, level + 1)
            print('    ' * level + str(node.data))
            self._printTree(node.left, level + 1)


def check_same_tree(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is not None and node2 is not None:
        return (
            node1.data == node2.data and
            check_same_tree(node1.left, node2.left) and
            check_same_tree(node1.right, node2.right)
        )
    return False  


Tree1 = AVLTree()
Tree2 = AVLTree()

Tree1_inp, Tree2_inp = input("Enter Tree1/Tree2 : ").split("/")
Tree1_inp = Tree1_inp.split()
Tree2_inp = Tree2_inp.split()

for data in Tree1_inp:
    Tree1.add(int(data))

for data in Tree2_inp:
    Tree2.add(int(data))

print("Tree 1")
Tree1.printTree()

print("Tree 2")
Tree2.printTree()

if check_same_tree(Tree1.root, Tree2.root):
    print("Same Tree")
else:
    print("Different Tree")

# Same Tree Or Not?

# ให้หาว่า AVL Tree ทั้งสองเป็นต้นเดียวกันหรือไม่ โดยให้แสดง Tree ทั้งสองต้นด้วย ต้นเดียวกันคือมีจำนวน node เท่ากัน

# ทุก node มีค่าเหมือนกันและอยู่ในตำแหน่งเดียวกัน ก็คือต้องหน้าตาเหมือนกันเป๊ะ ๆ



# >>> การรับ input

# เลขของ Tree#1 คั่นด้วย space ตามด้วย / เลขของ Tree#2 คั่นด้วย space

# Enter Tree1/Tree2 : 1 2 3 4 5/3 2 4 1 5



# >>> skeleton code เพื่อประหยัดเวลา ใช้หรือไม่ใช้ก็ได้

# def check_same_tree(Tree1, Tree2):

#     pass

       

# Tree1 = AVL()

# Tree2 = AVL()



# Tree1_inp, Tree2_inp = (input("Enter Tree1/Tree2 : ")).split("/")

# Tree1_inp = Tree1_inp.split()

# Tree2_inp = Tree2_inp.split()



# for data in Tree1_inp:

#     Tree1.insert(int(data))



# for data in Tree2_inp:

#     Tree2.insert(int(data))

   

# print("Tree 1")    

# Tree1.print_tree()



# print()

# print("Tree 2")

# Tree2.print_tree()



# print()

# if check_same_tree(Tree1.root, Tree2.root):

#     print("Same Tree")

# else:

#     print("Different Tree")