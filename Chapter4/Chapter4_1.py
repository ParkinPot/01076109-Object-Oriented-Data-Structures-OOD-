def process_queue(commands):
    q = []
    outputs = []

    for cmd in commands:
        cmd = cmd.strip()
        if cmd.startswith("E"):
            _, val = cmd.split()
            val = int(val)
            q.append(val)
            index = len(q) - 1
            outputs.append(f"Add {val} index is {index}")
        elif cmd == "D":
            if q:
                popped = q.pop(0)
                outputs.append(f"Pop {popped} size in queue is {len(q)}")
            else:
                outputs.append("-1")

    if q:
        remaining = [str(x) for x in q]
        outputs.append(f"Number in Queue is :  {remaining}")
    else:
        outputs.append("Empty")

    return outputs


input_line = input("Enter Input : ")
commands = input_line.split(',')

result = process_queue(commands)
for line in result:
    print(line)

# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา



# E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผลค่าที่ทำการ enqueue และ index ของตัวที่ทำการเพิ่มเข้าไป

# D                 ให้ทำการ dequeue ตัวที่อยู่หน้าสุดของ Queue ออกและแสดงตัวเลขที่เอาออกและแสดงขนาดของ Queue

#                     หลังจากทำการ dequeue แล้ว

# *** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty ***

# Enter Input : E 10,E 20,E 30,E 40,D,E 50,E 60,D,D,D,D,D,D
# Add 10 index is 0
# Add 20 index is 1
# Add 30 index is 2
# Add 40 index is 3
# Pop 10 size in queue is 3
# Add 50 index is 3
# Add 60 index is 4
# Pop 20 size in queue is 4
# Pop 30 size in queue is 3
# Pop 40 size in queue is 2
# Pop 50 size in queue is 1
# Pop 60 size in queue is 0
# -1
# Empty
