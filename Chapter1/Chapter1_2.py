print("*** multiplication or sum ***")
num1, num2 = map(int, input("Enter num1 num2 : ").split())
if num1*num2 <= 1000:
    print("The result is ", end = "")
    print(num1*num2)
else:
    print("The result is ", end = "")
    print(num1+num2)

# รับ input จำนวนเต็มสองจำนวน หากผลคูณของทั้งสองจำนวนมีค่าเกิน 1000 ให้ show ผลรวมของจำนวนทั้งสอง 
# แต่หากผลคูณมีค่าน้อยกว่าหรือเท่ากับ 1,000 ให้ show ผลคูณของจำนวนทั้งสอง

