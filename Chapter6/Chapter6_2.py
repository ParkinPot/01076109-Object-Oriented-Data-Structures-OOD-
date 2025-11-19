def lucky_number(number, count = 1):
    def sum_of_digits(num):
        if num == 0:
            return 0
        else:
            return (num % 10) + sum_of_digits(num // 10)
        
    total = sum_of_digits(number)
    if len(str(total)) > 1:
        print(f"Sum #{count} : {total}")
    elif len(str(total)) == 1:
        print(f"Lucky Number: {total}")
        return
    
    lucky_number(total, count + 1)

n = int(input("Enter Input: "))
lucky_number(n)

# Lucky Number

# หาผลรวมของเลขทุกหลักเรื่อยๆ จนกว่าจะได้เลขหลักเดียว

# >>> การรับ input รับตัวเลขจำนวนเต็มบวกค่าเดียว

# >>> อธิบาย Test Case

# Enter Input: 666

# Sum #1 : 18 		 (6 + 6 + 6 = 18)

# Lucky Number: 9		(1 + 8 = 9)

# *** Recursion only ห้ามใช้ loop

# เพิ่มเติม ข้อควรระวัง ที่อาจทำให้ web grader เกิดการ bug เช่น แสดงผลเพี้ยน, error

# prompt ใน input ไม่ตรงตาม test case เช่น input("Enter input :")

# การใช้ " หรือ ' ชนิดเดียวกันซ้อนกัน เช่น f"this is {" ".join(error)}"

# ใช้ switch case

# return f string เช่น return f"{eiei}" ออกมาจาก function