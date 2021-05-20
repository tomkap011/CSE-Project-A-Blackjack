import random

emblems = ['▒', '♣', '♦', '♥', '♠']
types = ['▒', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cards = []
chosen_emblems = []
chosen_types = []
values = []
max_card_count = 52
card_exposed = 0

def get_random_deck():
    global cards, chosen_emblems, chosen_types, max_card_count,values
    number_cards = max_card_count
    cards = []
    chosen_emblems = []
    chosen_types = []
    for i in range(0, number_cards):
        if i == 1:
            cards.append(random.randint(0, 52))
        else:
            new_card = random.randint(0, 52)
            while new_card in cards:
                new_card = random.randint(0, 52)
            cards.append(new_card)
    for i in range(0, number_cards):
        # get emblems
        if cards[i] in range(0, 12):
            chosen_emblems.append(1)
        elif cards[i] in range(14, 26):
            chosen_emblems.append(2)
        elif cards[i] in range(27, 39):
            chosen_emblems.append(3)
        elif cards[i] in range(40, 52):
            chosen_emblems.append(4)
        # get types
        if cards[i] in [1, 14, 27, 40]:
            chosen_types.append(1)
        elif cards[i] in [2, 15, 28, 41]:
            chosen_types.append(2)
        elif cards[i] in [3, 16, 29, 42]:
            chosen_types.append(3)
        elif cards[i] in [4, 17, 30, 43]:
            chosen_types.append(4)
        elif cards[i] in [5, 18, 31, 44]:
            chosen_types.append(5)
        elif cards[i] in [6, 19, 32, 45]:
            chosen_types.append(6)
        elif cards[i] in [7, 20, 33, 46]:
            chosen_types.append(7)
        elif cards[i] in [8, 21, 34, 47]:
            chosen_types.append(8)
        elif cards[i] in [9, 22, 35, 48]:
            chosen_types.append(9)
        elif cards[i] in [10, 23, 36, 49]:
            chosen_types.append(10)
        elif cards[i] in [11, 24, 37, 50]:
            chosen_types.append(11)
        elif cards[i] in [12, 25, 38, 51]:
            chosen_types.append(12)
        elif cards[i] in [13, 26, 39, 52]:
            chosen_types.append(13)
    return


def display_cards(number_cards_to_display):
    global cards, chosen_emblems, chosen_types
    card_sep = ''
    tpline = []
    rtline = []
    emline = []
    ltline = []
    # ensure card set is generated
    if [] ==  cards:
        get_random_deck()
    else:
        pass
    # card design template
    """ *********
        * T     *
        *   E   *
        *     T *
        *********"""
    for i in range(0, number_cards_to_display):
        tpline.append(f'*******')
        if chosen_types[i] != 10:
            rtline.append(f'* {types[chosen_types[i]]}   *')
            ltline.append(f'*   {types[chosen_types[i]]} *')
        elif chosen_types[i] == 10:
            rtline.append(f'* {types[chosen_types[i]]}  *')
            ltline.append(f'*  {types[chosen_types[i]]} *')
        emline.append(f'*  {emblems[chosen_emblems[i]]}  *')

    print(*tpline,sep='  ')
    print(*rtline,sep='  ')
    print(*emline,sep='  ')
    print(*ltline,sep='  ')
    print(*tpline,sep='  ')
    return

def draw():
    global card_exposed
    card_exposed = card_exposed + 1
    display_cards(card_exposed)
    return

def logic():
    user_choice = input('Would you like to draw or new deck?(y,n)')
    if user_choice == 'y':
        draw()
    elif user_choice == 'n':
        get_random_deck()
        print('new deck availabe')
        logic()
    logic()

dup = 0
reps= 10000
for i in range(0,reps):
    get_random_deck()
    if len(cards) != len(set(cards)):
        dup = dup + 1
        print(f'dupfound that the {dup} duplicate!')
    else:
        pass
print(f'duplicates found : {dup} that is {(round(((dup/reps)*100),5))} % ')