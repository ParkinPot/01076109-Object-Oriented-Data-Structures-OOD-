class Queue:
    def __init__(self, init_list = []):
        self.list = init_list.copy()  
    
    def enqueue(self, data):
        self.list.append(data)
    
    def dequeue(self):
        if self.size > 0:
            return self.list.pop(0)
        return None
    
    def peek(self): #ใช้ดูตัวแรกของ Queue
        if self.size > 0:
            return self.list[0]
        return None
    
    @property
    def size(self):
        return len(self.list)
    
    def __str__(self):
        return str(self.list)

print("*****Hot Potato Game*****")
inp = input("Enter Input: ").split("/")
names = inp[0].split(",")
num_passes = int(inp[1])

q = Queue(names)

while q.size > 1:
    print(f"{q.peek()} is the first player holding the potato")
    for i in range(num_passes):
        passed = q.dequeue()
        q.enqueue(passed)
        print(f"  Potato passed to: {q.peek()}")
    
    eliminated = q.dequeue()
    print(f"Eliminated: {eliminated}. Remaining players: {q.list}")

print(f"\nThe winner is: {q.peek()}!")

# *****Hot Potato Game*****
# Enter Input: Tom,Jerry,Steve/5
# Tom is the first player holding the potato
#   Potato passed to: Jerry
#   Potato passed to: Steve
#   Potato passed to: Tom
#   Potato passed to: Jerry
#   Potato passed to: Steve
# Eliminated: Steve. Remaining players: ['Tom', 'Jerry']
# Tom is the first player holding the potato
#   Potato passed to: Jerry
#   Potato passed to: Tom
#   Potato passed to: Jerry
#   Potato passed to: Tom
#   Potato passed to: Jerry
# Eliminated: Jerry. Remaining players: ['Tom']

# The winner is: Tom!
