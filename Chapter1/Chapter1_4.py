print("*** Fun with Drawing ***")
n = int(input("Enter input : "))

for i in range(0,n):
    for j in range(0,n-i-1): 
        print(".", end = "")

    print("*", end = "")

    if i == 0:
        print("." * (2*(n-1)-1), end = "")
        print("*", end = "")
        for j in range(0,n-i-1):
            print(".", end = "")
    elif i > 0:
        print("+" * (2*i-1), end = "*")

        for j in range(0,2*(n-i-1) - 1):
                print(".", end = "")
        if i < n-1:
                print("*", end = "")
        else:
             print("", end = "")

        print("+" * (2*i-1), end = "*")
        for j in range(0,n-i-1): 
                print(".", end = "")

    print("")

for i in range(1,2*n-1):
    for j in range(0,i):
        print(".", end="")
    
    print("*", end = "")

    for j in range(0,2*n-2-i):
        print("+", end = "")

    for j in range(1,2*n-2-i):
        print("+", end = "")

    if i == 2*n-2:   
        print("", end = "")
    elif i < 2*n-1:
        print("*", end = "")

    for j in range(0,i):
        print(".", end="")

    print("")




    

