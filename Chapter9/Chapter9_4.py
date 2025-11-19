def get_weight(word):
    value = {
        'a':1, 'b':2, 'c':3, 'd':4, 'e':5,
        'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
        'k':11,'l':12,'m':13,'n':14,'o':15,
        'p':16,'q':17,'r':18,'s':19,'t':20,
        'u':21,'v':22,'w':23,'x':24,'y':25,
        'z':26
    }
    weight = 0
    for ch in word:
        weight += value[ch]
    return weight

def vowel_info(word):
    vowels = "aeiou"
    priority = {"a":5, "e":4, "i":3, "o":2, "u":1}
    count = 0
    max_priority = 0
    for ch in word:
        if ch in vowels:
            count += 1
            if priority[ch] > max_priority:
                max_priority = priority[ch]
    return count, max_priority

print("***Fun with Word***")
inp = input("Enter Input : ").strip()

words, mode = inp.split("/")
words = words.split()

n = len(words)
for i in range(n):
    for j in range(0, n-i-1):
        if mode == "W":
            w1 = get_weight(words[j])
            w2 = get_weight(words[j+1])
            if w1 > w2 or (w1 == w2 and words[j] > words[j+1]) or (w1 == w2): 
                words[j], words[j+1] = words[j+1], words[j]
        elif mode == "V":
            v1 = vowel_info(words[j])
            v2 = vowel_info(words[j+1])
            if v1[0] > v2[0] or (v1[0] == v2[0] and v1[1] < v2[1]):
                words[j], words[j+1] = words[j+1], words[j]

print(" ".join(words))
