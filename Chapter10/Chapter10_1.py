def binarysearch(number, find):
    def calculate(index, length):
        percentile =  (index + 1) * 100 / length
        if percentile == 100:
            print("percentile :   100")
        else:
            print(f"percentile :   {float(percentile)}")

    low = 0 # low and high = index
    high = len(number) - 1
    
    if find<number[0]:
        print("\nindex      :   -1")
        print("percentile :   0")
        return

    if find>number[-1]:
        print("\nindex      :   999")
        print("percentile :   100")
        return

    while low<=high:
        mid = low + (high - low) // 2

        if number[mid] == find:
            print(f"\nindex      :   {float(mid)}")
            calculate(mid, len(number))
            return

        elif number[mid] < find:
            low = mid + 1
        else:
            high = mid - 1
    
    # no match
    index = high + (find - number[high]) / (number[low] - number[high])
    print(f"\nindex      :   {float(index)}")
    calculate(index, len(number))

inp = input("Enter Input : ")
number, find = inp.split('/')
number = list(map(float, number.split()))
find = float(find)
binarysearch(number, find)


