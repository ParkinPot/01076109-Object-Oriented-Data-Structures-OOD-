def move_to_front(books, requests):
    def search(char, array): # find index
        for i in range(len(array)):
            if array[i] == char:
                return i
            
    total_cost = 0
    storage = []
    
    for i in range(len(requests)):
        current_index = search(requests[i], books)
        if current_index is not None:
            record = books[:]
            books[1:current_index + 1] = record[:current_index]
            books[0] = record[current_index]
            total_cost += current_index+1
            print(f"Search {requests[i]} -> found at {current_index + 1} move to front ->  {' '.join(books)}")
        elif current_index is None and requests[i] not in storage:
            storage.append(requests[i])
            print(f"Search {requests[i]} -> not found -> {' '.join(books)}")
            total_cost += len(books) + 1
        else:
            books.insert(0, requests[i]) # or books = [requests[i] + books]
            print(f"Search {requests[i]} -> add new book ->  {' '.join(books)}")
            total_cost += 1
    
    print(f"\nFinal books: {' '.join(books)}")
    print(f"Total cost: {total_cost}")


print("This is your BOOK!!!")
inp = input("Enter input: ").split('/')
books = inp[0].split()
requests = inp[-1].split()
move_to_front(books, requests)
