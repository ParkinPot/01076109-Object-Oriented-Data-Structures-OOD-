def count(array):
    counts = {}
    for num in array:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    count_list = [(num, total) for num, total in counts.items()]

    for i in range(len(count_list)):
        for j in range(len(count_list)-1-i):
            if count_list[j][1] < count_list[j+1][1]:
                count_list[j], count_list[j+1] = count_list[j+1], count_list[j]

    for num, total in count_list:
        print(f"number {num}, total: {total}")

n = list(map(int, input("Enter list  of numbers: ").split()))
count(n)
