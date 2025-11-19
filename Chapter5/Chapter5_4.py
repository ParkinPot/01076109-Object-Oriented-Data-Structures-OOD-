class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def __str__(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node.data))
            node = node.next
        return ' '.join(ans)
    
    def food(self, amount):
        ant_used = []
        itr = self.head
        Success = False
        while itr:
            if 'W' in itr.data: 
                amount -= 2
                ant_used.append(itr.data)
            if 'A' in itr.data:
                amount -= 5
                ant_used.append(itr.data)
            
            if amount <= 0:
                Success = True
                break

            itr = itr.next

        itr = self.head
        while itr:
            if itr.data not in ant_used:
                self.head = itr
                break
            elif itr.next == None:
                self.head = None
            itr = itr.next

        ant_used = ' '.join(ant_used)

        if ant_used == "":
            ant_used = "Empty"

        return Success,ant_used
        
    def fight(self, amount):
        ant_used = []
        itr = self.head
        Success = False
        while itr:
            if 'W' in itr.data: 
                amount -= 5
                ant_used.append(itr.data)
            if 'A' in itr.data:
                amount -= 10
                ant_used.append(itr.data)
            
            if amount <= 0:
                Success = True
                break

            itr = itr.next

        itr = self.head
        while itr:
            if itr.data not in ant_used:
                self.head = itr
                break
            elif itr.next == None:
                self.head = None
            itr = itr.next

        ant_used = ' '.join(ant_used)

        if ant_used == "":
            ant_used = "Empty"

        return Success,ant_used
    
    def get_ant(self):
        worker = []
        soldier = []
        itr = self.head
        while itr:
            if 'W' in itr.data:
                worker.append(itr.data)
            if 'A' in itr.data:
                soldier.append(itr.data)
            itr = itr.next   

        if worker == []:
            worker = "Empty"
        else:
            worker = ' '.join(worker)
        if soldier == []:
            soldier = "Empty"
        else:
            soldier = ' '.join(soldier)
        
        return worker,soldier
    
    def add_worker(self, current_worker_id, amount, length):
        itr = self.head
        if not itr:
            self.head = Node(f"W{current_worker_id + 1}")
            last = self.head
            for i in range(1, amount):
                last.next = Node(f"W{current_worker_id + i + 1}")
                last = last.next
            return

        while itr.next:
            itr = itr.next 

        for i in range(amount):
            itr.next = Node(f"W{current_worker_id + i + 1}")
            itr = itr.next

    def add_soldier(self, current_soldier_id, amount, length):
        itr = self.head
        if not itr:
            self.head = Node(f"A{current_soldier_id + 1}")
            last = self.head
            for i in range(1, amount):
                last.next = Node(f"A{current_soldier_id + i + 1}")
                last = last.next
            return

        while itr.next:
            itr = itr.next 

        for i in range(amount):
            itr.next = Node(f"A{current_soldier_id + i + 1}")
            itr = itr.next

print("***This colony is our home***")
n = input("Enter input : ").split("/")
add_ant = n[0].split(" ")
command = n[1].split(",")

colony = LinkedList()
for i in range(int(add_ant[0])):
    colony.append(f"W{i+1}")
for i in range(int(add_ant[1])):
    colony.append(f"A{i+1}")

w_length,s_length = colony.get_ant()
w_length = len(w_length)
s_length = len(s_length)

if colony.head is None:
    print(f"Current Ant List: Empty\n")
else:
    print(f"Current Ant List: {colony}\n")

count = 0
for com in command:
    if 'C' in com:
        result,ant_used = colony.food(int(com[2:]))
        print(f"Food carrying mission : {ant_used}")
        if result == True:
            pass
        else:
            print("The food load is incomplete!")
            print("Queen is angry! ! !")
            count += 1
        if count == 3:
            print("**The queen is furious! The ant colony has been destroyed**")
            break
    if 'F' in com:
        result,ant_used = colony.fight(int(com[2:]))
        print(f"Attack mission : {ant_used}")
        if result == False:
            print("Ant nest has fallen!")
            break
    if 'S' in com:
        worker,solider = colony.get_ant()
        print(f"-> Remaining worker ants: {worker}")
        print(f"-> Remaining soldier ants: {solider}")
    if 'W' in com:
        worker,solider = colony.get_ant()
        if worker == "Empty":
            current_worker_id = 0
        else:
            last_worker = worker.split()[-1]
            current_worker_id = int(last_worker[1:])

        amount = int(com[2:])   
        colony.add_worker(current_worker_id,amount,w_length)
    if 'A' in com:
        worker,solider = colony.get_ant()
        if solider == "Empty":
            current_soldier_id = 0
        else:
            last_soldier = worker.split()[-1]
            current_soldier_id = int(last_soldier[1:])

        amount = int(com[2:])   
        colony.add_soldier(current_soldier_id,amount,s_length)

