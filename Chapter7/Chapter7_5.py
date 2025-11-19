class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTreeVisual(root, indent="", last='updown'):
    if root:
        print(indent, end='')
        if last == 'updown': 
            print("Root----", end='')
            indent += "       "
        elif last == 'right': 
            print("R----", end='')
            indent += "       "
        elif last == 'left': 
            print("L----", end='')
            indent += "       "
        print(root.val)
        printTreeVisual(root.left, indent, 'left')
        printTreeVisual(root.right, indent, 'right')

def buildTreeLevelOrder(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        node = queue.pop(0)
        if i < len(nodes):
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
            i += 1
        if i < len(nodes):
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
            i += 1
    return root


def mirrorTreeAtDepth(root, target_depth, current_depth=0):
    if not root:
        return
    if target_depth == 0:
        mirrorTree(root)
        return

    if current_depth == target_depth - 1:
        root.left, root.right = root.right, root.left
        mirrorTree(root.left)
        mirrorTree(root.right)
    else:
        mirrorTreeAtDepth(root.left, target_depth, current_depth + 1)
        mirrorTreeAtDepth(root.right, target_depth, current_depth + 1)

def mirrorTree(root):
    if root:
        root.left, root.right = root.right, root.left
        mirrorTree(root.left)
        mirrorTree(root.right)


def levelOrderTraversal(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    return result

raw = input(" *** Mirror Tree ***\nEnter nodes in level-order,depth : ").strip()
nums, depth = raw.split(',')
nums = list(map(int, nums.split()))
depth = int(depth)

root = buildTreeLevelOrder(nums)
print("before mirror:", levelOrderTraversal(root))
printTreeVisual(root)

mirrorTreeAtDepth(root, depth)
print("after mirror :", levelOrderTraversal(root))
printTreeVisual(root)

# คุณได้รับ Binary Tree ซึ่งสร้างจาก ลำดับตัวเลขแบบ level-order แต่ละตัวแทนโหนดของต้นไม้ โหนดแต่ละตัวอาจมีลูกทางซ้ายหรือขวา


# คุณต้องเขียนฟังก์ชันเพื่อ สลับโหนดซ้าย-ขวา (mirror) ของต้นไม้ ตั้งแต่ระดับที่กำหนดเป็นต้นไป ระดับเริ่มนับจากรากเป็น 0

# สร้างต้นไม้จากรายการ nodes
# แสดงต้นไม้ก่อน mirror (ทั้งแบบ list และ visual)
# สลับโหนดซ้าย-ขวาตั้งแต่ระดับ depth เป็นต้นไป
# แสดงต้นไม้หลัง mirror


# code แสดงผล

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def printTreeVisual(root, indent="", last='updown'):
#     if root != None:
#         print(indent, end='')
#         if last == 'updown': 
#             print("Root----", end='')
#             indent += "       "
#         elif last == 'right': 
#             print("R----", end='')
#             indent += "       "
#         elif last == 'left': 
#             print("L----", end='')
#             indent += "       "
#         print(root.val)
#         printTreeVisual(root.left, indent, 'left')
#         printTreeVisual(root.right, indent, 'right')
