class Queue:
    def __init__(self, init_list=[]):
        self.items = list(init_list)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

input_str = input("Enter input: ")
commands = input_str.split(", ")

schedule = {}
for cmd in commands:
    action, rest = cmd.split(":")
    time_str, *data = rest.strip().split(" ", 1)
    time = int(time_str)
    data = data[0] if data else None
    schedule.setdefault(time, []).append((action.strip(), data))

printer_queue = Queue()
tray = []
paper = 3
printing = None
print_buffer = []
current_time = 0
output = {}
max_time = max(schedule.keys()) if schedule else 0

def printer_status():
    if printing:
        return f'Status: Printing... "{printing}" and Pending {printer_queue.size()} file(s) in queue.'
    return f"Status: Idle. Pending {printer_queue.size()} file(s) in queue."

while True:
    if printing and print_buffer:
        print_buffer.pop(0)
        if not print_buffer:
            tray.append(printing)
            printing = None

    if not printing and not printer_queue.is_empty():
        if paper > 0:
            printing = printer_queue.dequeue()
            print_buffer = [printing[i:i+5] for i in range(0, len(printing), 5)]
            paper -= 1

    should_error = not printing and not printer_queue.is_empty() and paper <= 0
    if should_error:
        output.setdefault(current_time, []).append("Error: Printer is out of paper. Please refill.")

    if current_time in schedule:
        for command, data in schedule[current_time]:
            if command == "P":
                if printer_queue.size() >= 3:
                    output.setdefault(current_time, []).append("Error: Printer buffer is full. Please try again later.")
                else:
                    printer_queue.enqueue(data)
                    if not printing and paper > 0:
                        printing = printer_queue.dequeue()
                        print_buffer = [printing[i:i+5] for i in range(0, len(printing), 5)]
                        paper -= 1
                    elif not printing and paper <= 0:
                        output.setdefault(current_time, []).append("Error: Printer is out of paper. Please refill.")
            elif command == "R":
                try:
                    paper += int(data)
                    if not printing and not printer_queue.is_empty() and paper > 0:
                        printing = printer_queue.dequeue()
                        print_buffer = [printing[i:i+5] for i in range(0, len(printing), 5)]
                        paper -= 1
                except:
                    pass
            elif command == "S":
                output.setdefault(current_time, []).append(printer_status())
            elif command == "T":
                if tray:
                    docs = [f'"{doc}"' for doc in tray[::-1]]
                    output.setdefault(current_time, []).append(f"You got: {', '.join(docs)}")
                    tray.clear()
                else:
                    output.setdefault(current_time, []).append("You got: Nothing in tray.")

    if current_time >= max_time and not printing and (printer_queue.is_empty() or paper <= 0):
        break

    current_time += 1

for t in sorted(output.keys()):
    for line in output[t]:
        print(f"[Time {t}] {line}")