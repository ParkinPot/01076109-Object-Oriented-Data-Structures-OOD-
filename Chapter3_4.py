class Stack:
    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)
        print(f"Stack push {data} index of {arr[data]}")

    def pop(self):
        if not self.isEmpty():
            popped = self.list.pop()
            print(f"Stack pop")
            return popped
        return None

    def peek(self):
        if not self.isEmpty():
            return self.list[-1]
        return None

    def isEmpty(self):
        return self.list == []

print("*****Big leg on the right side*****")
input_str = input("Enter input: ")
arr = list(map(int, input_str.strip().split()))

output = [-1] * len(arr)
stack = Stack()

for i in range(len(arr)):
    while not stack.isEmpty() and arr[i] > arr[stack.peek()]:
        top_index = stack.peek()
        print(f"input[{i}]({arr[i]}) is greater than input[top of stack]({arr[top_index]})")
        popped_index = stack.pop()
        output[popped_index] = arr[i]
        print(f"Output: {output}")
    stack.push(i)

print(f"Output: {output}")

# input จะเป็น string เป็น format 1 2 3 4 5 ให้แปลงเป็น list ก่อน   Output เป็น list ที่มีขนาดเท่ากับ input
# โดยใน index ที่ตรงกันจะแสดงเลขที่มากกว่าและอยู่ใกล้ที่สุดทางด้านขวา(index มากกว่า)ที่อยู่ใน list ของ input ถ้าไม่มีจะเป็น -1 เช่น

# input -->  [1,2,3,4,5]
# output --> [2,3,4,5,-1]

# input  --> [5,1,3,2,6]
# output --> [6,3,6,6,-1]

# อนุญาตให้ใช้่ list ในส่วนของ Input และ Output เท่านั้น และต้องใช้ stack ในการหา Output

# HINT1: Stack เก็บ index
# HINT2: สร้าง Output list ที่มีแต่ -1 มาก่อน

# Skeleton code:
# class Stack:
#     def __init__(self):
#         self.list = []
    
#     def push(self,data):
#         pass

#     def pop(self):
#         pass
    
#     def peek(self): #ใช้ดู top of stack
#         pass
    
#     def isEmpty(self):
#         return self.list == []