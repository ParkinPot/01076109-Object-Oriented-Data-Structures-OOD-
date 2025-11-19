class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
        self.found_treasure = False

    def insert_value(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return self.root
        else:
            self.root = self._insert_helper(self.root, value)
            return self.root

    def _insert_helper(self, node, value):
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert_helper(node.left, value)
        elif value > node.value:
            node.right = self._insert_helper(node.right, value)
        return node

    def search_for_treasure(self, treasure_value, escape_value):
        return self._search_helper(self.root, treasure_value, escape_value)

    def _search_helper(self, node, treasure_value, escape_value):
        if node is None:
            return False

        explored_path.append(node.value)

        if node.value == treasure_value and not self.found_treasure:
            self.found_treasure = True
            print("Found Treasure !!!")

        if node.value == escape_value and self.found_treasure:
            print("Found Escape !!!")
            return True

        print("❌", end=" ")
        show_path(explored_path)

        left_result = self._search_helper(node.left, treasure_value, escape_value)
        if left_result:
            return True

        right_result = self._search_helper(node.right, treasure_value, escape_value)
        if right_result:
            return True

        explored_path.pop()
        return False

    def display_tree(self, node, depth=0):
        if node is not None:
            self.display_tree(node.right, depth + 1)
            print("     " * depth, node)
            self.display_tree(node.left, depth + 1)


def show_path(path_list):
    print(" -> ".join(map(str, path_list)))


explored_path = []
bst = BinarySearchTree()
raw_input, treasure_target, escape_target = [part for part in input("Enter Input : ").split("/")]
numbers = [int(num) for num in raw_input.split()]
treasure_target = int(treasure_target)
escape_target = int(escape_target)

for number in numbers:
    root = bst.insert_value(number)

bst.display_tree(root)
print("-------------------------------------------------")

if bst.search_for_treasure(treasure_target, escape_target):
    print("✅", end=" ")
    show_path(explored_path)
    print(">>> Mission Complete <<<")
else:
    print(">>> Mission Failed <<<")

# Treasure Hunting

# ให้หา path ในการเดินทางล่าสมบัติภายใน Binary Search Tree แล้วจึงหาทางออก โดยในแต่ละpathต้องไปยัง node ถัดไปเรื่อย ๆ 
# ไม่สามารถเดินทางกลับไปทางเดิมได้ ในการค้นหาเส้นทางที่เป็นไปได้ให้เริ่มจาก root เมื่อเจอทั้งสมบัติและทางออกแล้วให้หยุด



# >>> การรับ input รับ node แต่ละตัวคั่นด้วย space / treasure / escape 

# โดยให้นำ node ใน input ส่วนแรกไปสร้าง BST แล้วแสดง tree ออกมา

# >>> อธิบาย Test Case

# Enter Input : 8 3 10 1 4 9 12 0 2 11 13/10/11 #ส่วนแรกคือ BST, 10 คือ treasure, 11 คือ escape

#                 13

#            12

#                 11

#       10

#            9

#  8					#แสดง Binary Search Tree ที่สร้าง

#            4

#       3

#                 2

#            1

#                 0

# ------------------------------------------------- 

# ❌ 8					#หา path เริ่มจาก root เมื่อเจอ treasure หรือ escape ให้แสดง 

# ❌ 8 -> 3				#แสดง path ไปยังทุก ๆ node จนกว่าจะเจอครบ

# ❌ 8 -> 3 -> 1				

# ❌ 8 -> 3 -> 1 -> 0

# ❌ 8 -> 3 -> 1 -> 2

# ❌ 8 -> 3 -> 4

# Found Treasure !!!                                    #สมบัติที่เจอคือ 10

# ❌ 8 -> 10				

# ❌ 8 -> 10 -> 9

# ❌ 8 -> 10 -> 12

# Found Escape !!!                                        #ทางออกที่เจอคือ 11


# ✅ 8 -> 10 -> 12 -> 11		             

# >>> Mission Complete <<<                          #แสดง Mission Complete เมื่อเจอสมบัติแล้วเจอทางออก และ Failed เมื่อไม่สำเร็จ