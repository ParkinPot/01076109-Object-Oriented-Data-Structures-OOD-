def weirdSubtract(n,s):
    for _ in range(s):
        if not n:
            return 0
        elif n[-1] == 0:
            n.pop()
        else:
            n[-1] -= 1
    return ''.join(map(str, n))

n, s = input("Enter num and sub : ").split()
n = list(map(int, n))
s = int(s)
print(weirdSubtract(n,s))


# จงสร้างฟังก์ชัน weirdSubstract โดยรับ parameter n,k โดยมีเงื่อนไขคือ

# หาก n ลงท้ายด้วย 0 ให้ตัด 0 ตัวสุดท้ายทิ้ง 

# หากไม่ใช่ ให้ทำการลดค่า n ลง 1 ค่า

# โดยทำซ้ำทั้งหมด k รอบ

# ตัวอย่าง เช่น n = 21 , k =3

# ดังนั้นทำซ้ำ 3 รอบโดย

# รอบที่ 1 : n จะลดค่าลง 1 เหลือเป็น 20

# รอบที่ 2 : n จะตัด 0 ตัวสุดท้ายทิ้งเหลือเป็น 2

# รอบที่ 3 : n จะลดค่าลง 1 เหลือเป็น 1

# ค่าที่จะ return ค่า 1 ออกมา

# def weirdSubtract(n,k):

# 	### Enter Your Code Here ###

# n,s = input("Enter num and sub : ").split()

# print(weirdSubtract(int(n),int(s)))

