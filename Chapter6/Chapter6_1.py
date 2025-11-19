def fibo(number):
    if number <= 2:
        return 1
    else:
        return fibo(number - 1) + fibo(number - 2)

n = int(input("Enter Number : "))
print(f"fibo({n}) = {fibo(n)}")

# หาลำดับ Fibonacci ของ input ที่รับเข้ามาโดยใช้ Recursive