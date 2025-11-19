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
            return -1 if node == None else node.height

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
        if not node is None:
            self._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self._printTree(node.left, level + 1)

    def maxSumPath(self):
        path, total = self._maxSumPath(self.root)
        print("Path with maximum sum:", " + ".join(map(str, path)), "=", total)

    def _maxSumPath(self, node):
        if node is None:
            return [], 0
        if node.left is None and node.right is None:
            return [node.data], node.data

        left_path, left_sum = self._maxSumPath(node.left)
        right_path, right_sum = self._maxSumPath(node.right)

        if left_sum > right_sum:
            return [node.data] + left_path, node.data + left_sum
        else:
            return [node.data] + right_path, node.data + right_sum

nums = list(map(int, input("Enter tree nodes: ").split()))
tree = AVLTree()
for n in nums:
    tree.add(n)

tree.printTree()

tree.maxSumPath()

# นักผจญภัยกับต้นแอปเปิลทองคำ

# ในป่าลึกลับแห่งหนึ่ง มี ต้นแอปเปิลทองคำหายาก ที่ออกผลเพียงครั้งเดียวในรอบ 100 ปี
# ผลแอปเปิลทองคำแต่ละผลมี ค่าความสำคัญเป็นตัวเลข แต่ละผลจะเติบโตอยู่บน ต้นไม้ AVL Tree ที่รากคือจุดเริ่มเดินทางของนักผจญภัย

# น้องๆในฐานะนักผจญภัยต้องเก็บ แอปเปิลทองคำที่มีค่ามากที่สุด จากรากไปยังใบภายในครั้งเดียว!
# นักผจญภัยสามารถเดินจาก root ไปยัง leaf ทีละ node และต้องเลือกเส้นทางที่ทำให้ผลรวมค่าของแอปเปิลทองคำ มากที่สุด

# สรุป

# รับ input เป็นชุดตัวเลขแทนค่าผลแอปเปิลแต่ละ node
# สร้าง AVL Tree
# หา path จาก root → leaf ที่ผลรวมค่าผลแอปเปิลทองคำ มากที่สุด
# แสดง path และผลรวม