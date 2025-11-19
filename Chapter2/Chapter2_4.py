def sum(arr):
    result = []
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == 5:
                    triplet = sorted([arr[i], arr[j], arr[k]])
                    if triplet not in result:
                        result.append(triplet)
    return result

input_str = input("Enter Your List : ")
array = list(map(int, input_str.split()))

if len(array) < 3:
    print("Array Input Length Must More Than 2")
else:
    print(sum(array))


# จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 พจน์ใดๆใน Array ที่มีผลรวมเท่ากับ 5 สำหรับ Array ที่มีข้อมูลข้างในเป็นจำนวนจริง ***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป***

# Enter Your List : -25 -10 -7 -3 2 4 8 10
# [[-7, 2, 10], [-7, 4, 8]]

# Enter Your List : -3 2 4 6 8 10
# [[-3, 2, 6]]

# Enter Your List : -100 100
# Array Input Length Must More Than 2

# Enter Your List : 5 -5 5 -5 5 -5 5 5 -5 -5 -5 -5 5
# [[-5, 5, 5]]
