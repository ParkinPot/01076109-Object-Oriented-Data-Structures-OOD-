def Combination(input_list, combo = [], answer = []):
    if not input_list:
        if combo:
            answer.append(combo.copy()) # avoid mutability (combo can be changed)
        return answer
    
    combo.append(input_list[0])
    Combination(input_list[1:], combo, answer)

    combo.pop()
    Combination(input_list[1:], combo, answer)

    return answer

n = list(map(int, input("Enter Input: ").split()))
print(f"Output: {Combination(n)}")

# หาทุกความเป็นไปได้ในการจับกลุ่มสมาชิกใน input list พูดง่ายๆก็ Combination ในความน่าจะเป็นนั่นแหละ

# บังคับใช้ recursive function นะจ๊ะ

# คำเตือน!!!!
# --- อย่า return [ ] เพราะจะเป็นเหมือนการ return f"{some_thing}" output ไม่ออก

# HINT: ฟังก์ชันเรียกใช้ตัวเอง 2 รอบ คือ การลือก element ใส่ในคำตอบ กับ การข้ามตัวนั้นไป 

# Skeleton:

# def Combination(input_list, answer = []):
#     pass
