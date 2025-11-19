class Queue:
    def __init__(self, init_list=[]):
        self.list = init_list[:]
    
    def enqueue(self, data):
        self.list.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.list.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.list[0]
        return None

    def is_empty(self):
        return len(self.list) == 0

    def __len__(self):
        return len(self.list)

    def __str__(self):
        return str(self.list)

def organization_queue_simulator(commands):
    org_queues = {}           
    main_queue = Queue()      

    for cmd in commands:
        if cmd.startswith("en"):
            number = int(cmd.split()[1])
            org_id = int(str(number)[0])
            print(f"Enqueued: {number}")

            if org_id not in org_queues:
                org_queues[org_id] = Queue()
                main_queue.enqueue(org_id)

            org_queues[org_id].enqueue(number)
            queue_state = []
            for oid in main_queue.list:
                queue_state.append(org_queues[oid].list)
            print("Queue state:", queue_state)

        elif cmd == "de":
            if main_queue.is_empty():
                print("Queue is empty")
                continue

            front_org = main_queue.peek()
            person = org_queues[front_org].dequeue()
            print(f"Dequeued: {person}")

            if org_queues[front_org].is_empty():
                main_queue.dequeue()
                del org_queues[front_org]

            queue_state = []
            for oid in main_queue.list:
                queue_state.append(org_queues[oid].list)
            print("Queue state:", queue_state)

print(" ***Queue of Queue of Queue of ...*** ")
user_input = input("Enter Input : ")
commands = [cmd.strip() for cmd in user_input.split(',')]
organization_queue_simulator(commands)

# ระบบคิวองค์กร (Organization Queue)

# โปรแกรมจำลองระบบคิวที่จัดการการเข้าคิวของผู้ใช้โดยจัดกลุ่มตามองค์กร โดยใช้เลขหลักแรกของตัวเลขแทนองค์กรนั้น ๆ

# รายละเอียดโปรแกรม

# โปรแกรมจะรับคำสั่ง enqueue (en) และ dequeue (de) ในรูปแบบข้อความ  
# และแสดงสถานะของคิวหลังการดำเนินการแต่ละขั้นตอน

# การทำงานของโปรแกรม
# - เลขหลักแรกของตัวเลขแทน **องค์กร**  
# - ตัวเลขแต่ละตัวแทนผู้ที่เข้าคิว (เช่น 201 คือผู้จากองค์กร 2)  
# - เมื่อ enqueue ตัวเลข โปรแกรมจะจัดกลุ่มผู้เข้าคิวตามองค์กรโดยรวมผู้ที่มีองค์กรเดียวกันไว้ในคิวย่อยเดียวกัน  
# - คิวหลักจะเก็บคิวย่อยของแต่ละองค์กรตามลำดับที่องค์กรนั้นเข้าคิวครั้งแรก  
# - เมื่อ dequeue จะให้บริการคนแรกของคิวย่อยองค์กรที่อยู่หน้าสุดในคิวหลัก  
# - ถ้าคิวย่อยองค์กรใดว่างเปล่า จะถูกลบออกจากคิวหลัก   รูปแบบ Input
# en <number>, en <number>, ..., de, de, ...

# ตัวอย่าง
# en 201,en 101,en 102,en 202,de,de,de,de
# คำอธิบาย
# Enqueued: 201
# เพิ่มหมายเลข 201 เข้าไปในคิวขององค์กร 2 → คิวปัจจุบัน: [[201]]
# Enqueued: 101
# เพิ่มหมายเลข 101 เข้าไปในคิวขององค์กร 1 → คิวปัจจุบัน: [[201], [101]]
# Enqueued: 102
# เพิ่มหมายเลข 102 เข้าไปในคิวองค์กร 1 ต่อจาก 101 → คิวปัจจุบัน: [[201], [101, 102]]
# Enqueued: 202
# เพิ่มหมายเลข 202 เข้าไปในคิวองค์กร 2 ต่อจาก 201 → คิวปัจจุบัน: [[201, 202], [101, 102]]
# Dequeued: 201
# นำหมายเลขแรกในคิวองค์กร 2 ออก คือ 201 → คิวปัจจุบัน: [[202], [101, 102]]
# Dequeued: 202
# นำหมายเลขถัดไปในคิวองค์กร 2 ออก คือ 202 → คิวองค์กร 2 ว่าง จึงลบออก → คิวปัจจุบัน: [[101, 102]]
# Dequeued: 101
# นำหมายเลขแรกในคิวองค์กร 1 ออก คือ 101 → คิวปัจจุบัน: [[102]]
# Dequeued: 102
# นำหมายเลขถัดไปในคิวองค์กร 1 ออก คือ 102 → คิวองค์กร 1 ว่าง จึงลบออก → คิวปัจจุบัน: []

# ตัวอย่าง Output
# Enqueued: 201
# Queue state: [[201]]
# Enqueued: 101
# Queue state: [[201], [101]]
# Enqueued: 102
# Queue state: [[201], [101, 102]]
# Enqueued: 202
# Queue state: [[201, 202], [101, 102]]
# Dequeued: 201
# Queue state: [[202], [101, 102]]
# Dequeued: 202
# Queue state: [[101, 102]]
# Dequeued: 101
# Queue state: [[102]]
# Dequeued: 102
# Queue state: []

#  ***Queue of Queue of Queue of ...*** 
# Enter Input : en 101,de,de,de
# Enqueued: 101
# Queue state: [[101]]
# Dequeued: 101
# Queue state: []
# Queue is empty
# Queue is empty
