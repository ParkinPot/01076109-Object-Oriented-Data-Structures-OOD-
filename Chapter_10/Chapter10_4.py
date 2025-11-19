def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n

class HashTable:
    def __init__(self, size, max_col, threshold):
        self.size = size
        self.max_col = max_col
        self.threshold = threshold
        self.table = [None] * size
        self.count = 0
        self.history = []

    def print_table(self):
        for i in range(self.size):
            val = self.table[i] if self.table[i] is not None else "None"
            print(f"#{i+1}\t{val}")
        print("----------------------------------------")

    def hash_func(self, key):
        return key % self.size

    def insert_internal(self, key, show_collision=True):
        index = self.hash_func(key)
        for c in range(self.max_col):
            idx = (index + c**2) % self.size
            if self.table[idx] is None:
                self.table[idx] = key
                self.count += 1
                self.history.append(key)
                return True
            else:
                if show_collision:
                    print(f"collision number {c+1} at {idx}")
        return False

    def rehash(self, new_data=None, show_old_collision=True, show_new_collision=False):
        old_data = self.history.copy()
        new_size = next_prime(self.size * 2)
        self.size = new_size
        self.table = [None] * new_size
        self.count = 0
        self.history = []
        for k in old_data:
            self.insert_internal(k, show_collision=show_old_collision)
        if new_data is not None:
            self.insert_internal(new_data, show_collision=show_new_collision)
        self.print_table()

    def add(self, key):
        print(f"Add : {key}")
        if ((self.count + 1) / self.size) * 100 > self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash(new_data=key, show_old_collision=True, show_new_collision=True)
            return

        success = self.insert_internal(key, show_collision=True)
        if not success:
            print("****** Max collision - Rehash !!! ******")
            self.rehash(new_data=key, show_old_collision=True, show_new_collision=False)
            return

        self.print_table()

if __name__ == "__main__":
    print(" ***** Rehashing *****")
    inp = input("Enter Input : ").strip()
    left, right = inp.split('/')
    size, max_col, threshold = map(int, left.split())
    data = list(map(int, right.split()))

    h = HashTable(size, max_col, threshold)
    print("Initial Table :")
    h.print_table()
    for d in data:
        h.add(d)
