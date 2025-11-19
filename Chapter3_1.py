print("***Always 5 or 10***")
n = list(map(int, input("Enter Input : ").split()))
stack = []
stack.append(n[0])
last = n[0]

for i in range(1, len(n)):
    if last + n[i] == 5 or last - n[i] == 5 or n[i] - last == 5 or last + n[i] == 10 or last - n[i] == 10 or n[i] - last == 10:
        stack.append(n[i])
        last = n[i]

print("Output :", *stack)

# ให้รับตัวเลขเข้ามาเป็น list และสร้าง stack ขึ้นมา โดยต้องเก็บเฉพาะตัวเลขที่เมื่อนำมาบวกหรือลบกับตัวบนสุดของ stack 
# แล้วได้ผลลัพธ์เท่ากับ 5 หรือ 10 หลังจากนั้นแสดงผลลัพธ์!

