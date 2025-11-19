class LinkedList:
    class Node:
        def __init__(self, data = None, next = None):
            self.data = data 
            self.next = next
        
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0
    
    def append(self,data):
        if self.head is None:
            self.head = self.Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = self.Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.append(int(data))

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def __str__(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node.data))
            node = node.next
        return '->'.join(ans)
    
    def sort(self):
        print("_______________________________________")
        for _ in range(self.get_length()-1):
            itr = self.head
            while itr and itr.next:
                if int(itr.data) > int(itr.next.data):
                    print("")
                    print(f"Swapping {itr.data} and {itr.next.data}")
                    itr.data, itr.next.data = itr.next.data, itr.data
                    print(f"List: {self}")
                itr = itr.next
        print("_______________________________________") 
    
print("*****Bubble Sort Linked List*****")
n = LinkedList()
n.insert_values(input("Enter Input: ").split(','))
print(f"Input List: {n}")
n.sort()
print(f"Sorted List: {n}")

# ข้อนี้ง่ายๆ ทำ Bubble sort ที่เราคุ้นเคยใน Linked-List

# อนุญาตให้มี list แค่ 2 ที่คือตอนใช้ split() และใน __str__() ใน Skeleton code เท่านั้น นอกเหนือจากนั้นต้องใช้ Linked-List

# class LinkedList:
#     class Node:
#         pass
        
#     def __init__(self):
#         self.head = None
#         self.tail = self.head
#         self.size = 0
    
#     def append(self,data):
#         pass


#     def __str__(self):
#         ans = []
#         node = self.head
#         while node:
#             ans.append(str(node))
#             node = node.next
#         return '->'.join(ans)