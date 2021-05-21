import random
import time

start_time = time.time()

emblems = ['▒', '♣', '♦', '♥', '♠']
types = ['▒', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
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
bet = 0
balance = 100
firstrun = True
cards_to_play_d = 0
d_final_value = 0
hold = False


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
    cards_dealer = []
    # setting up variables
    # number of how many cards to genrate this set by varible at the begining of the code call max_card_count
    number_cards = 52
    # cards is the order of the deck this expresed as integer bettwen 0,51 for each card
    cards = []
    # this varible that makes the cards easier work in code mostly for the display module
    chosen_emblems = []
    # this varible that makes the cards easier work in code mostly for the display module and getting the value of
    # each cards
    chosen_types = []
    # the for is used to have set number repitions
    for i in range(0, 52):
        # if its the first card we simply generate no checks needed
        if i == 1:
            cards_dealer.append(random.randint(0, 52))
        else:
            # here if the i is non 1 we go and make a new card check if already on the list if its we go again until
            # the code finds a apporite that then appended
            new_card = random.randint(0, 52)
            while new_card in cards_dealer:
                new_card = random.randint(0, 52)
            cards_dealer.append(new_card)

    # there still some sets with repetitions in them here we check if the deck is on them and if so we throw it out and
    # try again
    if len(cards_dealer) != len(set(cards_dealer)):
        get_random_deck_dealer()
    else:
        if len(set(cards_dealer)) <= 50:
            print('here')
            get_random_deck()

    # the for command is used to run the code the approate number of times
    for i in range(0, number_cards):
        # get emblems and append to chossen emblems list
        if cards_dealer[i] in range(0, 13):
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
    card_num = []
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
            if chosen_types_dealer[i] != 10:
                card_num.append(f'| {cards_dealer[i]} |')
                rtline.append(f'* {types[chosen_types_dealer[i]]}   *')
                ltline.append(f'*   {types[chosen_types_dealer[i]]} *')
            elif chosen_types_dealer[i] == 10:
                rtline.append(f'* {types[chosen_types_dealer[i]]}  *')
                ltline.append(f'*  {types[chosen_types_dealer[i]]} *')
            emline.append(f'*  {emblems[chosen_emblems_dealer[i]]}  *')
    elif revealed == bool(0):
        for i in range(0, number_cards_to_display):
            tpline.append("*******")
            rtline.append("*▒▒▒▒▒*")
            emline.append("*-----*")
            ltline.append("*▒▒▒▒▒*")
    # printing the list without any of list sybols and adding spacing
    print('Dealer\'s hand===========')
    print(*tpline, sep='  ')
    print(*rtline, sep='  ')
    print(*emline, sep='  ')
    print(*ltline, sep='  ')
    print(*tpline, sep='  ')
    return


def display_cards(number_cards_to_display):
    global cards, chosen_emblems, chosen_types
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
    print('Your Hand ===============')
    print(*tpline, sep='  ')
    print(*rtline, sep='  ')
    print(*emline, sep='  ')
    print(*ltline, sep='  ')
    print(*tpline, sep='  ')
    return


# this code serves to reveal a card to the player
def draw(*cte):
    global card_exposed
    # adds one to cards exposed
    if cte == ():
        card_exposed = card_exposed + 1
    else:
        card_exposed = int(str(*cte))
    # gets display cards to display said number of cards
    display_cards(card_exposed)
    print()
    return


# the front end code for the game
def cal_number_card_to_play():
    global cards_to_play_d, d_final_value
    value_to_play = []
    f2 = ((int(values_dealer[0]) + int(values_dealer[1])))
    if f2 == 21:
        draw(2)
    for i in range(0, 52):
        x = sum(values[0:i])
        if x <= 21:
            value_to_play.append(i)
        if x >= 21:
            cards_to_play_d = (len(value_to_play))
            break

    gl = random.randint(0, 3)
    gl = 100
    if sum(values_dealer[0:cards_to_play_d-1]) > 18:
        d_final_value = sum(values_dealer[0:cards_to_play_d])
    elif gl == 1:
        d_final_value = sum(values_dealer[0:cards_to_play_d])
    elif gl == 2:
        d_final_value = sum(values_dealer[0:cards_to_play_d]) - 1
        cards_to_play_d =- 1
    elif gl == 3:
        d_final_value = sum(values_dealer[0:cards_to_play_d]) + 1
        cards_to_play_d = + 1

def get_card_vals():
    global values, chosen_types
    for i in range(0, len(chosen_types)):
        if chosen_types[i] == 0:
            values.append(9999999999)
        elif chosen_types[i] in [11, 12, 13]:
            values.append(10)
        elif chosen_types[i] in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            values.append(chosen_types[i])
        elif chosen_types[i] == 1:
            values.append(10)
        else:
            values.append(000000)


def get_card_vals_d():
    global values_dealer, chosen_types_dealer
    for i in range(0, len(chosen_types_dealer)):
        if chosen_types_dealer[i] == 0:
            values_dealer.append(9999999999)
        elif chosen_types_dealer[i] in [11, 12, 13]:
            values_dealer.append(10)
        elif chosen_types_dealer[i] in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            values_dealer.append(chosen_types_dealer[i])
        elif chosen_types_dealer[i] == 1:
            values_dealer.append(10)
        else:
            values_dealer.append(000000)


def lose_bet():
    global balance, bet
    balance = balance - bet


def win_bet():
    global balance, bet
    balance = balance + bet


def set_bet(new_bet):
    global balance, bet
    if new_bet > balance:
        print('You cant bet more then you have!')
    elif new_bet < balance:
        bet = new_bet


def check_draw():
    i = input('Would you like to draw?(y,n) ?_')
    try:
        if i[0] == 'y':
            draw()
            return True
        if i[0] == 'n':
            pass
            return False
    except:
        pass


def play():
    global card_exposed, values, d_final_value, d_t_s, cards_to_play_d, hold
    card_exposed = 0
    bust = False
    playing = True
    new_bet = input('How much are you betting?_')
    if new_bet.isnumeric():
        if int(new_bet) < int(0):
            print('Cant be negative')
            play()
        else:
            set_bet(int(new_bet))
    else:
        play()
    while playing:
        if check_draw():
            if cards_to_play_d > card_exposed:
                d_t_s = card_exposed
            else:
                d_t_s = cards_to_play_d
            display_cards_dealer(d_t_s, 0)
        elif not check_draw():
            check_result()
            hold = True
        if sum(values[0:card_exposed]) <= 21:
            pass
        else:
            check_result()


def check_result():
    global card_exposed, values, d_final_value, d_t_s, cards_to_play_d, hold
    print('\n\n\n\n\n')
    display_cards(card_exposed)
    print(sum(values[0:card_exposed]))
    display_cards_dealer(cards_to_play_d, 1)
    print(sum(values_dealer[0:cards_to_play_d]))
    if d_final_value > 21:
        print('You win!')
        win_bet()
    elif sum(values[0:card_exposed]) > 21:
        lose_bet()
    elif hold:
        if sum(values[0:card_exposed]) > sum(values_dealer[0:card_exposed]):
            print('You win!')
            win_bet()
    elif sum(values[0:card_exposed]) == d_final_value:
        print('Tie!')
        reset()
    elif sum(values[0:card_exposed]) < d_final_value:
        print('You lose')
        lose_bet()
        reset()
    elif sum(values[0:card_exposed]) > d_final_value:
        print('You win!')
        win_bet()

    else:
        print('Well this unexpected the codes fucked sorry please restart me!')
    reset()
    print(f'balance : {balance}')
    input('Shall we begin..(press enter to start)')
    time.sleep(1)
    for i in range(0, 40):
        print('\n')
    reset()
    play()


def reset():
    global cards, cards_dealer, chosen_emblems, chosen_types, chosen_types_dealer, chosen_emblems_dealer, values_dealer \
        , values, max_card_count, bet, card_exposed, card_exposed_dealer, cards_to_play_d, d_final_value
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
    bet = 0
    cards_to_play_d = 0
    d_final_value = 0
    get_random_deck()
    get_random_deck_dealer()
    get_card_vals()
    get_card_vals_d()
    cal_number_card_to_play()



# default runs
get_random_deck()
get_random_deck_dealer()
get_card_vals()
get_card_vals_d()
cal_number_card_to_play()

while 1:
    # Check to do welcome
    if firstrun == True:
        print('Welcome to blackjack!')
        print('Please note for the sake of sanity of the coder Aces will treated as being worth 10 thanks!')
        print('Would like to know the rules? (y,n)')
        get_instuct = input('?_')
        if str(get_instuct[0]).lower() == 'y':
            print('http://www.hitorstand.net/strategy.php')
        else:
            pass
        firstrun = False
    print('Shall we begin..')
    time.sleep(1)
    print(f'Your balance is {balance}')
    play()
