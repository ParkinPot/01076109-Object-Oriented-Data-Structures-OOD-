def bubblesort(array):
    n = len(array)

    if n <= 1:
        print(f"last step : {array} move[None]")
        return

    if all(array[k] <= array[k+1] for k in range(n-1)):
        print(f"last step : {array} move[None]")
        return

    for i in range(n - 1):
        swapped = False
        last_moved = None
        mid_sorted = False

        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
                last_moved = array[j + 1]

                if all(array[k] <= array[k + 1] for k in range(n - 1)):
                    if j < (n - 2 - i):
                        mid_sorted = True

        if not swapped:
            print(f"last step : {array} move[None]")
            return

        if mid_sorted:
            print(f"{i+1} step : {array} move[{last_moved}]")
            print(f"last step : {array} move[None]")
            return

        if all(array[k] <= array[k + 1] for k in range(n - 1)):
            print(f"last step : {array} move[{last_moved}]")
            return
        else:
            print(f"{i+1} step : {array} move[{last_moved}]")

n = list(map(int, input("Enter Input : ").split()))
bubblesort(n)