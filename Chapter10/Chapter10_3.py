class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self, size, max_col):
        self.size = size
        self.max_col = max_col
        self.table = [None] * size
        self.full_message_shown = False

    def print_table(self):
        for i in range(self.size):
            print(f"#{i+1}\t{self.table[i]}")
        print("---------------------------")

    def is_full(self):
        return all(x is not None for x in self.table)

    def hashing(self, key):
        return sum(ord(ch) for ch in key) % self.size

    def insert(self, data):
        if self.is_full():
            if not self.full_message_shown:
                print("This table is full !!!!!!")
                self.full_message_shown = True
            return

        index = self.hashing(data.key)
        collision = 0

        while collision < self.max_col:
            new_index = (index + collision**2) % self.size
            if self.table[new_index] is None:
                self.table[new_index] = data
                self.print_table()
                return
            else:
                print(f"collision number {collision+1} at {new_index}")
                collision += 1

        print("Max of collisionChain")
        self.print_table()

        if self.is_full() and not self.full_message_shown:
            print("This table is full !!!!!!")
            self.full_message_shown = True


print(" ***** Fun with hashing *****")
inp = input("Enter Input : ").split('/')
table_info, data_info = inp[0].split(), inp[1].split(',')
size, max_col = int(table_info[0]), int(table_info[1])

h = hash(size, max_col)

for d in data_info:
    key, value = d.split()
    h.insert(Data(key, value))
