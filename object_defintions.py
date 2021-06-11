import random

# object of Card
import config


class Card:
    # defining the cards and its characteristics
    def __init__(self, suit, number):
        self.is_ace = False
        self.suit = suit
        self.number = number
        # adding the value of the card to the card
        if self.number in [11, 12, 13]:
            self.value = 10
        elif self.number == 1:
            self.value = 11
            self.is_ace = True
        else:
            self.value = self.number

    # function to easily print off the info about a card
    def print_info(self):
        print(f'Suit: {self.suit} \n number: {self.number} \n value: {self.value}')


class Deck:
    # initializing a deck (creating the list randomizing and defining stuff)
    def __init__(self):
        self.max_cards = ()
        self.number_of_aces = 0
        self.value = ()
        self.cards = []
        self.counter = 0
        self.suits = ['♣', '♦', '♥', '♠']
        self.numbers = ['▒', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        for i in range(1, 14):
            for j in range(0, 4):
                self.cards.append(Card(j, i))
        random.shuffle(self.cards)

    # displaying the deck
    def deck_print(self, header=str(), display_info=bool):
        line_top_bottom = []
        emblem_____line = []
        number_line_t = []
        number_line_b = []

        if self.counter > 52:
            self.counter = 52

        if self.max_cards == ():
            self.max_cards = 99999999

        if self.counter > self.max_cards:
            self.counter = self.max_cards

        if display_info:
            for i in range(0, self.counter):
                line_top_bottom.append(f'*******')
                emblem_____line.append(f'*  {self.suits[self.cards[i].suit]}  *')
                if self.numbers[self.cards[i].number] == 10:
                    number_line_t.append(f'*{self.numbers[self.cards[i].number]}   *')
                    number_line_b.append(f'*   {self.numbers[self.cards[i].number]}*')
                else:
                    number_line_t.append(f'*{self.numbers[self.cards[i].number]}    *')
                    number_line_b.append(f'*    {self.numbers[self.cards[i].number]}*')
        else:
            for i in range(0, self.counter):
                line_top_bottom.append(f'*******')
                emblem_____line.append(f'*|||||*')
                number_line_b.append(f'*|||||*')
                number_line_t.append('*|||||*')

        print(header)
        print(*line_top_bottom, sep='  ')
        print(*number_line_t, sep='  ')
        print(*emblem_____line, sep='  ')
        print(*number_line_b, sep='  ')
        print(*line_top_bottom, sep='  ')

    # draw card
    def draw(self, header=str(), display_info=bool):
        self.counter += 1
        self.deck_print(header=header, display_info=display_info)

    def cal_score(self):
        self.score = []
        for i in range(0, self.counter):
            self.score.append(self.cards[i].value)
            # print(self.cards[i].print_info())
        self.score = sum(self.score)

    def result(self, display_score=bool):
        self.cal_score()
        if self.score > 21:
            for i in range(0, self.counter):
                if self.cards[i].is_ace:
                    self.cards[i].value = 1
                self.cal_score()
                if self.score <= 21:
                    break
        print(f'Score = {self.score}')


class Player:
    def __init__(self, ai_on=bool):
        self.ai_on = ai_on
        self.deck = Deck()
        self.current_bet = 0
        self.balance = config.default_balance
        self.max_cards = int()
        if ai_on:
            self.deck.cal_score()
            while 1:
                self.deck.cal_score()
                if self.deck.score <= 17:
                    self.deck.cal_score()
                    self.deck.counter += 1
                else:
                    self.deck.cal_score()
                    break
            self.deck.max_cards = self.deck.counter
    def reset_deck(self):
        self.current_bet = 0
        self.deck = Deck()
        if self.ai_on:
            self.deck.cal_score()
            while 1:
                self.deck.cal_score()
                if self.deck.score <= 17:
                    self.deck.cal_score()
                    self.deck.counter += 1
                else:
                    self.deck.cal_score()
                    break
            self.deck.max_cards = self.deck.counter


def credits():
    print("░█████╗░██████╗░███████╗░█████╗░████████╗███████╗██████╗░  ██████╗░██╗░░░██╗")
    print("██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗  ██╔══██╗╚██╗░██╔╝")
    print("██║░░╚═╝██████╔╝█████╗░░███████║░░░██║░░░█████╗░░██║░░██║  ██████╦╝░╚████╔╝░")
    print("██║░░██╗██╔══██╗██╔══╝░░██╔══██║░░░██║░░░██╔══╝░░██║░░██║  ██╔══██╗░░╚██╔╝░░")
    print("╚█████╔╝██║░░██║███████╗██║░░██║░░░██║░░░███████╗██████╔╝  ██████╦╝░░░██║░░░")
    print("░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░  ╚═════╝░░░░╚═╝░░░")
    print('')
    print("████████╗██╗░░██╗░█████╗░███╗░░░███╗░█████╗░░██████╗  ██╗░░██╗░█████╗░██████╗░░█████╗░░█████╗"
          "░░██████╗██╗")
    print("╚══██╔══╝██║░░██║██╔══██╗████╗░████║██╔══██╗██╔════╝  ██║░██╔╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗"
          "██╔════╝██║")
    print("░░░██║░░░███████║██║░░██║██╔████╔██║███████║╚█████╗░  █████═╝░███████║██████╔╝██║░░██║██║░░╚═╝"
          "╚█████╗░██║")
    print("░░░██║░░░██╔══██║██║░░██║██║╚██╔╝██║██╔══██║░╚═══██╗  ██╔═██╗░██╔══██║██╔═══╝░██║░░██║██║░░██╗"
          "░╚═══██╗██║")
    print("░░░██║░░░██║░░██║╚█████╔╝██║░╚═╝░██║██║░░██║██████╔╝  ██║░╚██╗██║░░██║██║░░░░░╚█████╔╝╚█████╔╝"
          "██████╔╝██║")
    print("░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░╚════╝░░╚════╝░"
          "╚═════╝░╚═╝")
    print('Thomas Kapocsi')
