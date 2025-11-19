class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def sort(self):
        itr = self.head
        found_zero = False
        before_zero = []
        after_zero = []
        while itr:
            if itr.data == '0' and not found_zero:
                found_zero = True
                after_zero.append(itr.data)
            elif found_zero:
                after_zero.append(itr.data)
            else:
                before_zero.append(itr.data)

            itr = itr.next

        self.head = None
        for data in after_zero + before_zero:
            self.insert_at_end(data)

    def print(self):
        itr = self.head
        linked_string = ''
        while itr:
            linked_string += str(itr.data) + ' <- ' if itr.next else str(itr.data)
            itr = itr.next

        print(linked_string)

print(" *** Locomotive ***")
n = LinkedList()
n.insert_values(input("Enter Input : ").split())
print("Before : ", end = "")
n.print()
n.sort()
print("After : ", end = "")
n.print()

# มีรถไฟอยู่ขบวนหนึ่ง โดยรถไฟนั้นจะมีหมายเลขกำกับตู้แต่ละตู้อยู่และรถไฟก็มีหัวรถจักรอยู่

# แต่หัวรถจักรดันไปต่อกับตู้รถไฟอยู่ พี่ต้องการให้น้อง ๆ ทำการแบ่งขบวนรถไฟออก

# โดยให้หัวรถจักรอยู่ข้างหน้าสุด และส่วนตู้ที่เหลือให้ทำการต่อกับตู้สุดท้ายโดยไม่มีการเปลี่ยนลำดับของตู้

# ซึ่งพี่จะให้หมายเลข 0 แทนเป็นหัวรถจักร ส่วน หมายเลขอื่นจะเป็นตู้รถไฟ

# เช่น 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6

# เป็น 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1 ( ให้ใช้ singly linked list)



#  *** Locomotive ***
# Enter Input : 2 3 1 0 4 5 6
# Before : 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6
# After : 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1


#  *** Locomotive ***
# Enter Input : 1 2 3 0
# Before : 1 <- 2 <- 3 <- 0
# After : 0 <- 1 <- 2 <- 3

