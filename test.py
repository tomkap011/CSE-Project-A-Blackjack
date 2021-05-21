import random
import time

start_time = time.time()

emblems = ['▒', '♣', '♦', '♥', '♠']
types = ['▒', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cards = []
cards_dealer = []
chosen_emblems = []
chosen_types = []
chosen_emblems_dealer = []
chosen_types_dealer = []
values = []
values_dealer = []
max_card_count = 52
card_exposed = 0
card_exposed_dealer = 0


def get_random_deck():
    global cards, chosen_emblems, chosen_types, max_card_count, values, card_values
    # setting up variables
    # number of how many cards to genrate this set by varible at the begining of the code call max_card_count
    number_cards = max_card_count
    # cards is the order of the deck this expresed as integer bettwen 0,51 for each card
    cards = []
    # this varible that makes the cards easier work in code mostly for the display module
    chosen_emblems = []
    # this varible that makes the cards easier work in code mostly for the display module and getting the value of
    # each cards
    chosen_types = []
    # the for is used to have set number repitions
    for i in range(0, number_cards):
        # if its the first card we simply generate no checks needed
        if i == 1:
            cards.append(random.randint(0, 52))
        else:
            # here if the i is non 1 we go and make a new card check if already on the list if its we go again until
            # the code finds a apporite that then appended
            new_card = random.randint(0, 52)
            while new_card in cards:
                new_card = random.randint(0, 52)
            cards.append(new_card)
    # there still some sets with repetitions in them here we check if the deck is on them and if so we throw it out and
    # try again
    if len(cards) == len(set(cards)):
        pass
    else:
        get_random_deck()
    # the for command is used to run the code the approate number of times
    for i in range(0, number_cards):
        # get emblems and append to chossen emblems list
        if cards[i] in range(0, 12):
            chosen_emblems.append(1)
        elif cards[i] in range(14, 26):
            chosen_emblems.append(2)
        elif cards[i] in range(27, 39):
            chosen_emblems.append(3)
        elif cards[i] in range(40, 52):
            chosen_emblems.append(4)
        # get types and append them to the chosen types list
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
    # we then return,
    # the variables being globals there is not need to return them
    return


def get_random_deck_dealer():
    global cards_dealer, chosen_emblems_dealer, chosen_types_dealer, max_card_count, values_dealer
    # setting up variables
    # number of how many cards to genrate this set by varible at the begining of the code call max_card_count
    number_cards = max_card_count
    # cards is the order of the deck this expresed as integer bettwen 0,51 for each card
    cards = []
    # this varible that makes the cards easier work in code mostly for the display module
    chosen_emblems = []
    # this varible that makes the cards easier work in code mostly for the display module and getting the value of
    # each cards
    chosen_types = []
    # the for is used to have set number repitions
    for i in range(0, number_cards):
        # if its the first card we simply generate no checks needed
        if i == 1:
            cards_dealer.append(random.randint(0, 52))
        else:
            # here if the i is non 1 we go and make a new card check if already on the list if its we go again until
            # the code finds a apporite that then appended
            new_card = random.randint(0, 52)
            while new_card in cards:
                new_card = random.randint(0, 52)
            cards_dealer.append(new_card)
    # there still some sets with repetitions in them here we check if the deck is on them and if so we throw it out and
    # try again
    if len(cards) == len(set(cards_dealer)):
        pass
    else:
        get_random_deck()
    # the for command is used to run the code the approate number of times
    for i in range(0, number_cards):
        # get emblems and append to chossen emblems list
        if cards_dealer[i] in range(0, 12):
            chosen_emblems_dealer.append(1)
        elif cards_dealer[i] in range(14, 26):
            chosen_emblems_dealer.append(2)
        elif cards_dealer[i] in range(27, 39):
            chosen_emblems_dealer.append(3)
        elif cards_dealer[i] in range(40, 52):
            chosen_emblems_dealer.append(4)
        # get types and append them to the chosen types list
        if cards_dealer[i] in [1, 14, 27, 40]:
            chosen_types_dealer.append(1)
        elif cards_dealer[i] in [2, 15, 28, 41]:
            chosen_types_dealer.append(2)
        elif cards_dealer[i] in [3, 16, 29, 42]:
            chosen_types_dealer.append(3)
        elif cards_dealer[i] in [4, 17, 30, 43]:
            chosen_types_dealer.append(4)
        elif cards_dealer[i] in [5, 18, 31, 44]:
            chosen_types_dealer.append(5)
        elif cards_dealer[i] in [6, 19, 32, 45]:
            chosen_types_dealer.append(6)
        elif cards_dealer[i] in [7, 20, 33, 46]:
            chosen_types_dealer.append(7)
        elif cards_dealer[i] in [8, 21, 34, 47]:
            chosen_types_dealer.append(8)
        elif cards_dealer[i] in [9, 22, 35, 48]:
            chosen_types_dealer.append(9)
        elif cards_dealer[i] in [10, 23, 36, 49]:
            chosen_types_dealer.append(10)
        elif cards_dealer[i] in [11, 24, 37, 50]:
            chosen_types_dealer.append(11)
        elif cards_dealer[i] in [12, 25, 38, 51]:
            chosen_types_dealer.append(12)
        elif cards_dealer[i] in [13, 26, 39, 52]:
            chosen_types_dealer.append(13)
    # we then return,
    # the variables being globals there is not need to return them
    return


def display_cards_dealer(number_cards_to_display, revealed):
    global cards_dealer, chosen_emblems_dealer, chosen_types_dealer
    card_sep = ''
    tpline = []
    rtline = []
    emline = []
    ltline = []
    # ensure card set is generated
    # card design template
    # creating the display line by line as list
    if revealed == bool(1):
        for i in range(0, number_cards_to_display):
            tpline.append(f'*******')
            if chosen_types[i] != 10:
                rtline.append(f'* {types[chosen_types_dealer[i]]}   *')
                ltline.append(f'*   {types[chosen_types_dealer[i]]} *')
            elif chosen_types[i] == 10:
                rtline.append(f'* {types[chosen_types[chosen_types_dealer[i]]]}  *')
                ltline.append(f'*  {types[chosen_types_dealer[i]]} *')
            emline.append(f'*  {emblems[chosen_emblems_dealer[i]]}  *')
    elif revealed == bool(0):
        for i in range(0, number_cards_to_display):
            tpline.append("*******")
            rtline.append("*▒▒▒▒▒*")
            emline.append("*-----*")
            ltline.append("*▒▒▒▒▒*")
    # printing the list without any of list sybols and adding spacing
    print(*tpline, sep='  ')
    print(*rtline, sep='  ')
    print(*emline, sep='  ')
    print(*ltline, sep='  ')
    print(*tpline, sep='  ')
    return


def display_cards(number_cards_to_display):
    global cards, chosen_emblems, chosen_types
    card_sep = ''
    tpline = []
    rtline = []
    emline = []
    ltline = []
    # ensure card set is generated
    # card design template
    """ *********
        * T     *
        *   E   *
        *     T *
        *********"""
    # creating the display line by line as list
    for i in range(0, number_cards_to_display):
        tpline.append(f'*******')
        if chosen_types[i] != 10:
            rtline.append(f'* {types[chosen_types[i]]}   *')
            ltline.append(f'*   {types[chosen_types[i]]} *')
        elif chosen_types[i] == 10:
            rtline.append(f'* {types[chosen_types[i]]}  *')
            ltline.append(f'*  {types[chosen_types[i]]} *')
        emline.append(f'*  {emblems[chosen_emblems[i]]}  *')
    # printing the list without any of list sybols and adding spacing
    print(*tpline, sep='  ')
    print(*rtline, sep='  ')
    print(*emline, sep='  ')
    print(*ltline, sep='  ')
    print(*tpline, sep='  ')
    return


# this code serves to reveal a card to the player
def draw():
    global card_exposed
    # adds one to cards exposed
    card_exposed = card_exposed + 1
    # gets display cards to display said number of cards
    display_cards(card_exposed)
    print()
    return


# the front end code for the game
def dealer():
    pass


# a diagnosis tool for the efficiency of the code with the random being the bottle neck in the system that is what
# we check it outputs time taken to run if there are any repeating cards and some usefull information
def rand_check():
    # start of the code time
    global cards, max_card_count
    # the number of sets with duplicats
    dup = 0
    # the number of times the code reapets
    reps = 10000
    # the list where all the
    times = []
    # once again using a for command for reapeting
    for i in range(0, reps):
        # storing the time when the rep started
        start_time = time.time()
        # genrating a deck
        get_random_deck_dealer()
        # storing the end time
        end_time = time.time()
        # checking for duplicate and adding it to the count if found
        if len(cards) != len(set(cards)):
            print(f'found {len(cards) - len(set(cards))} that the {dup} duplicate!')
            dup = dup + (len(cards) - len(set(cards)))
        else:
            pass
        # storing the end time
        end_time = time.time()
        # adding the time taken to the list
        times.append((end_time - start_time))
    # calculating the average time
    av_time = sum(times) / len(times)
    # calculating the total time
    totaltimetaken = sum(times)
    # printing all the usefull information
    print(f'duplicates found : {dup} that is {(round(((dup / reps) * 100), 5))} % the average run time per set was'
          f' {(round(av_time, 7))} \n there where {max_card_count} cards in each set, the full run time was {round(totaltimetaken, 5)} seconds '
          f'there where a total of {reps} deck\'s generated')


get_random_deck_dealer()
display_cards_dealer(10,0)