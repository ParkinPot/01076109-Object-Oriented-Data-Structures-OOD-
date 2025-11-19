def Rshift(n,s):
    return n >> s    

n,s = input("Enter number and shiftcount : ").split()

print(Rshift(int(n),int(s)))


# Right Shift คือการ เลื่อนบิตของเลขฐานสองไปทางขวา โดยแต่ละตำแหน่งที่เลื่อน จะ หารค่าด้วย 2 (โดยไม่เอาเศษ) ต่อการเลื่อน 1 ตำแหน่ง

# 8 right shift 1
# 8 = 1000 (ฐานสอง)
# 1000 >> 1 = 0100 = 4

# 3888 >> 4  =  3888 // 16 = 243
# Right Shift 4 ตำแหน่ง = หารด้วย 2⁴ = 16