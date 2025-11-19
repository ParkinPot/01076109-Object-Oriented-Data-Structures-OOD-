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

group_count = 0

def process(item, q, limit):
    global group_count
    limit = int(limit)

    if q.size() == limit:
        group_count += 1
        print(f"Group {group_count} : ", end='')
        while q.size() > 1:
            print(q.dequeue(), end=', ')
        print(q.dequeue())
        process(item, q, limit)
        return

    if item == 'Yellow' and ('Blue' not in q.values or ('Blue' in q.values and 'Red' in q.values)):
        q.enqueue(item)
    elif item == 'Pink' and ('Green' not in q.values or ('Blue' in q.values and 'Green' in q.values)):
        q.enqueue(item)
    elif item == 'Green' and ('Pink' not in q.values or ('Blue' in q.values and 'Pink' in q.values)):
        q.enqueue(item)
    elif item == 'Blue' and ('Yellow' not in q.values or ('Yellow' in q.values and 'Red' in q.values)):
        q.enqueue(item)
    else:
        if item in ['Yellow', 'Pink', 'Green', 'Blue'] and not q.is_empty():
            rejected.enqueue(item)
        else:
            q.enqueue(item)

print("***Make a group***")
raw_input = input("Enter input : ")
max_size, items_str = raw_input.split(',')
items_str += ' E'

main_queue = Queue()
rejected = Queue()

for token in items_str.split():
    process(token, main_queue, max_size)

while not main_queue.is_empty():
    if main_queue.peek() == 'E':
        main_queue.dequeue()
    else:
        rejected.enqueue(main_queue.dequeue())

print("Rejected : ", end='')
if rejected.is_empty():
    print('None')
else:
    while rejected.size() > 1:
        print(rejected.dequeue(), end=', ')
    print(rejected.dequeue())

# คุณครูกุ๊กจะกำหนดจำนวนสมาชิกและรายชื่อนักเรียนทั้งหมด ให้พวกเราช่วยจัดกลุ่มโดยห้ามใช้ list ให้หน่อย

# นักเรียนแต่ละคนมีชื่อดังนี้ Green, Red, Blue, Yellow, Pink โดยอาจมีนักเรียนที่ชื่อซ้ำกัน
# เงื่อนไขการจัดกลุ่ม    Green ห้ามอยู่กลุ่มเดียวกับ Pink เว้นแต่ในกลุ่มนั้นมี Blue อยู่ด้วย
#                                Blue ห้ามอยู่กลุ่มเดียวกับ Yellow เว้นแต่ในกลุ่มนั้นมี Red อยู่ด้วย

# ให้จัดกลุ่มสมาชิกตามลำดับที่ได้รับ โดยแต่ละกลุ่มต้องมีจำนวนสมาชิกตามที่กำหนด
# แสดงผลลัพธ์เป็นจำนวนกลุ่มที่จัดได้สำเร็จ สมาชิกในแต่ละกลุ่ม และคนที่จัดกลุ่มไม่สำเร็จ

# ***Make a group***
# Enter input : 3, Pink Green Yellow Blue Red Green Pink Blue Red Yellow Green
# Group 1 : Pink, Yellow, Red
# Group 2 : Green, Blue, Red
# Rejected : Green, Blue, Pink, Yellow, Green
