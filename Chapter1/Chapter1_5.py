print("*** Fun with countdown ***")
n = list(map(int, input("Enter List : ").split()))
result = []
i = 0

while i < len(n):
    temp = []

    if n[i] > 1:
        temp.append(n[i])
        while i + 1 < len(n) and n[i] - 1 == n[i + 1]:
            i += 1
            temp.append(n[i])
            if n[i] == 1:
                result.append(temp)
                break
        else:
            i -= len(temp) - 1  

    elif n[i] == 1:
        result.append([1])

    i += 1

print([len(result), result])


# อยากให้นักศึกษาช่วยหาลำดับการ Countdown จาก Input ที่รับเข้ามา โดยลำดับการ Countdown จะเป็นเลขเรียงลำดับ เช่น 2->1 , 3->2->1 โดยจะสิ้นสุดด้วย 1 เสมอ

# โดยผลลัพธ์ให้แสดง List ของ จำนวนลำดับที่เจอ และ แต่ละลำดับเป็นอย่างไร

# *** Fun with countdown ***
# Enter List : 4 8 3 2 1 2
# [1, [[3, 2, 1]]]


# *** Fun with countdown ***
# Enter List : 1 1 2 1
# [3, [[1], [1], [2, 1]]]
