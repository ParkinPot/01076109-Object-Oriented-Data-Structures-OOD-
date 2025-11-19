def card_sort(cards, mode):
    symbol_order = {"C":0,"D":1,"H":2,"S":3}
    num_order = {"2":0,"3":1,"4":2,"5":3,"6":4,"7":5,"8":6,"9":7,
                 "T":8,"J":9,"Q":10,"K":11,"A":12}

    seen = set()
    valid_cards = []

    for card in cards:
        if len(card) < 2 or len(card) > 3:  
            print(f"Error: {card} is an invalid card")
            continue

        sym, num = card[0], card[1:]
        if sym not in symbol_order or num not in num_order:
            print(f"Error: {card} is an invalid card")
            continue

        if card in seen:
            print(f"Error: Duplicate card found - {card}")
            continue
        seen.add(card)
        valid_cards.append((sym, num))

    if not valid_cards:
        print("No valid cards to sort.")
        return

    def get_key(card):
        sym, num = card
        if mode == "num":
            return (num_order[num], symbol_order[sym])
        else:
            return (symbol_order[sym], num_order[num])

    for i in range(1, len(valid_cards)):
        key = valid_cards[i]
        j = i - 1
        while j >= 0 and get_key(valid_cards[j]) > get_key(key):
            valid_cards[j+1] = valid_cards[j]
            j -= 1
        valid_cards[j+1] = key

    result = " ".join(sym+num for sym,num in valid_cards)
    print(f"Sorted cards : {result}")

print("Have fun with sort card")
n = input("Enter Input: ")
if ("/") not in n:
    print("No valid cards to sort.")
else:
    deck, mode = n.split("/")
    cards = deck.split(",") if deck else []
    card_sort(cards, mode)
