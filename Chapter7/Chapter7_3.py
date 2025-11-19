class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_recursive(self.root, data)
        
    def insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_recursive(node.left, data)
        else: # data >= node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_recursive(node.right, data)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def find_sum(self):
        if not self.root:
            return 0
        
        def traverse(node):
            if node is None:
                return 0
            left_sum = traverse(node.left)
            right_sum = traverse(node.right)
            return node.data + left_sum + right_sum

        return traverse(self.root)
    
    def multiply(self, multiplier):
        if not self.root:
            return 0
        
        def traverse(node):
            if node is None:
                return 0
            
            if node.data > multiplier:
                node.data *= multiplier
            
            traverse(node.left)
            traverse(node.right)

        traverse(self.root)
        
print("**Sum of tree**")
T = BST()
numbers, multiplier = input("Enter input : ").split('/')
numbers = list(map(int, numbers.split()))
unique_number = [] # avoid dupes
for number in numbers:
    if number not in unique_number:
        unique_number.append(number)
multiplier = int(multiplier)

for i in unique_number:
    T.insert(i)

print("\nTree before:")
T.printTree(T.root)
print(f"Sum of all nodes = {T.find_sum()}")

print("\nTree after:")
T.multiply(multiplier)
T.printTree(T.root)
print(f"Sum of all nodes = {T.find_sum()}")

# Sum of Tree

# จงหาผลรวมของ Binary Search Tree (BST)



# รับ input 2 ส่วน แยกด้วย /

# list ของตัวเลข

# ตัวเลข k

# 	    การทำงาน


# สร้าง BST จาก list ของตัวเลข (ถ้าเจอตัวเลขซ้ำจะไม่สร้าง node ใหม่)

# แสดง Tree ก่อนปรับค่า พร้อม ผลรวมของทุก node

# ตรวจสอบแต่ละ node ใน tree หาก node > k ให้คูณ node ด้วย k

# แสดง Tree หลังปรับค่า พร้อม ผลรวมของ node ใหม่