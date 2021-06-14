# imports the user_input module user_input to easier mange the user inputs
import u_input as u_i
# import the object definition for cards,decks and players
from object_defintions import *


# running the game
def run():
    # setting up the players
    player = Player(ai_on=False)
    dealer = Player(ai_on=True)

    # Welcome Message
    print('Welcome to BlackJack!')
    # asks user if they want to know the rules and if yes print out a link for blackjack rules
    if u_i.boolean(question='Do you want to know the rules?'):
        print('https://bicyclecards.com/how-to-play/blackjack/')

    # Game-loop
    while 1:
        # print the player balance
        print(f'current balance = {player.balance} $')
        # getting the bet of player and make sure that it is possible
        while 1:
            j = u_i.postive_int_only('What do you want to bet')
            # checks if the player balance is is larger then the bet
            if j > player.balance:
                print('That is higher then you balance ')
                pass
            # if the player bet is good break the loop
            else:
                player.current_bet = j
                break

        # print the current bet
        print(f'Your bet has been set to {player.current_bet} $')

        # starts the draw loop I.E (the player loop continues until the player specifies not to draw)
        while u_i.boolean(question='do you want to draw?'):
            player.deck.draw(header='Player ###################')
            dealer.deck.draw(display_info=False, header='Dealer ###################')

        # print the final result and value of the decks
        player.deck.deck_print(header='Player ###################')
        player.deck.result()
        dealer.deck.draw(display_info=True, header='Dealer ###################')
        dealer.deck.result()

        # calculate winner
        player.deck.calulate_drawn_deck_values()

        if dealer.deck.score > 21:
            player.balance = player.balance + player.current_bet
            print('you win!')
        elif player.deck.score == 21:
            player.balance = player.balance + player.current_bet
            print('you win!')
        elif dealer.deck.score < player.deck.score <= 21:
            player.balance = player.balance + player.current_bet
            print('you win!')
        elif player.deck.score > 21:
            player.balance = player.balance - player.current_bet
            print('you lose')

        # asks if player want to play a other round
        if u_i.boolean(question='Do you want play another round?'):
            player.reset_deck()
            dealer.reset_deck()
        # quits loop if  play does not want to play a other round
        else:
            print(f' Final Balance = {player.balance}')
            credits()
            quit()
            print('Achievement get "How did we get her" \n no seriously there quit command above me!')
