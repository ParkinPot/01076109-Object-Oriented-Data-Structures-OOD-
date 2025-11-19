class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" → " if current.next else "\n")
            current = current.next

    def reverse_k_group_alternate(self, k):
        if k <= 1 or self.head is None:
            return
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        current = self.head
        reverse = True
        while current:
            tail = current
            count = 0
            while count < k and tail:
                tail = tail.next
                count += 1
            if reverse:
                prev_next = prev.next
                next_current = tail
                prev_node = tail
                node = current
                for _ in range(count):
                    next_node = node.next
                    node.next = prev_node
                    prev_node = node
                    node = next_node
                prev.next = prev_node
                prev = prev_next
                current = tail
            else:
                for _ in range(count):
                    prev = current
                    current = current.next
            reverse = not reverse
        self.head = dummy.next

print(" *** Ant Army ***")
n = input("Input : ")
values, k = n.strip().split(',')
k = int(k)
values = list(map(int, values.strip().split()))

ll = LinkedList()
for v in values:
    ll.append(v)

print("Before :", end=" ")
ll.print_list()

ll.reverse_k_group_alternate(k)

print("After :", end=" ")
ll.print_list()
