class TorKham:
    def __init__(self):
        self.words = []

    def restart(self):
        self.words = []
        return "game restarted"

    def play(self, word):
        word_lower = word.lower()
        used_words = [w.lower() for w in self.words]

        if word_lower in used_words:
            return f"'{word}' -> game over"

        if self.words:
            last_word = self.words[-1].lower()
            if last_word[-2:] != word_lower[:2]:
                return f"'{word}' -> game over"

        self.words.append(word)
        return f"'{word}' -> {self.words}"


torkham = TorKham()
print("*** TorKham HanSaa ***")
S = input("Enter Input : ").split(',')

for command in S:
    command = command.strip()

    if command == 'X':
        break
    elif command == 'R':
        print(torkham.restart())
    elif command.startswith('P '):
        parts = command.split(' ', 1)
        if len(parts) != 2 or not parts[1].strip():
            print(f"'{command}' is Invalid Input !!!")
            break
        word = parts[1].strip()
        result = torkham.play(word)
        print(result)
        if "game over" in result:
            break
    else:
        print(f"'{command}' is Invalid Input !!!")
        break

# Same as Chapter2_3.py