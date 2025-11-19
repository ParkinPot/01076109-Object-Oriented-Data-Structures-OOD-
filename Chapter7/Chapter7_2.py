class Queue:
    def __init__(self, values=None):
        self.values = values if values is not None else []

    def enqueue(self, val):
        self.values.append(val)

    def dequeue(self):
        return self.values.pop(0)

    def peek(self):
        return self.values[0]

    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)

class BST:
    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key

        def __repr__(self):
            return f"Node({self.val})"
        
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = self.Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = self.Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = self.Node(key)
            else:
                self._insert(node.right, key)

    def __str__(self):
        return self._print_tree(self.root, 0)
    
    def _print_tree(self, node, level):
        if node is None:
            return ""
        result = self._print_tree(node.right, level + 1)
        result += " " * 4 * level + f"{node.val}\n"
        result += self._print_tree(node.left, level + 1)
        return result
    
    def BFS(self):
        if not self.root:
            return []
        
        result = []
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.dequeue()
            result.append(node.val)

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return result
    
    def PIDSADAN(self):
        if not self.root:
            return []
        
        result = []
        
        def traverse(node):
            if node is None:
                return
            result.append(node.val)
            traverse(node.right)
            traverse(node.left)

        traverse(self.root)
        return result

print("******BFS Pis-sa-dan******")
T = BST()
numbers = list(map(int, input("Enter numbers: ").split()))
for i in numbers:
    root = T.insert(i)
print(T)
print(f"BFS: {T.BFS()}")
print(f"BFS Pid-Sa-Dan: {T.PIDSADAN()}")

# Breadth First Search หรือ BFS คือการหา node ในกราฟ ในกรณีนี้คือ BST โดยจะไล่หาไปทีละ level เริ่มจาก root
# ในข้อนี้นักศึกษาต้องแปลงจาก tree เป็น list โดยใช้หลักการของ BFS ในการ traverse
# Example:
#                                 root
#              1.1                        1.2
#     2.1               2.2                        2.3
# 3.1    3.2      3.3    3.4               3.5

# จะได้ [root, 1.1, 1.2, 2.1, 2.2, 2.3, 3.1, 3.2, 3.3, 3.4, 3.5]
 
# ถ้านักศึกษาทำ BFS ได้แล้วจะพบว่ามีการใช้ Data structure ที่เคยเรียนผ่านมาแล้วอันนึงช่วย ทีนี้นักสึกษาต้องทำ BFS แบบพิสดารโดยใช้ Data structure 
# อันใหม่ในการทำ tree traversal และแปลงเป็น list
# โดย Output จะเป็น [root, 1.2,  2.3, 3.5, 1.1, 2.2, 3.4, 3.3, 2.1, 3.2, 3.1]

# อนุญาติให้ list ในการเก็บ Output ของการ traversal เท่านั้น

# Skeleton:

# class BST:
#     class Node:
#         def __init__(self, key):
#             self.left = None
#             self.right = None
#             self.val = key
#         def __repr__(self):
#             return f"Node({self.val})"
#     def __init__(self):
#         self.root = None
#     def insert(self, key):
#         pass
#     def _insert(self, node, key):
#         pass

#     def __str__(self):
#         return self._print_tree(self.root, 0)
#     def _print_tree(self, node, level):
#         if node is None:
#             return ""
#         result = self._print_tree(node.right, level + 1)
#         result += " " * 4 * level + f"{node.val}\n"
#         result += self._print_tree(node.left, level + 1)
#         return result


