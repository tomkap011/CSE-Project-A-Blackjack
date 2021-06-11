import u_input as u_i
from object_defintions import *
<<<<<<< HEAD
def run():
    player = Player(ai_on=False)
    dealer = Player(ai_on=True)

    print('Welcome to BlackJack!')
    if u_i.boolean(question='Do you want to know the rules?'):
        print('https://bicyclecards.com/how-to-play/blackjack/')

    while 1:
        print(f'current balance = {player.balance} $')
        while 1:
            j = u_i.postive_int_only('What do you want to bet')
            if j > player.balance:
                print('That is higher then you balance ')
                pass
            else:
                player.current_bet = j
                break

        print(f'Your bet has been set to {player.current_bet} $')

        while u_i.boolean(question='do you want to draw?'):
            player.deck.draw(header='Player ###################')
            dealer.deck.draw(display_info=False, header='Dealer ###################')

        player.deck.deck_print(header='Player ###################')
        player.deck.result()
        dealer.deck.draw(display_info=True, header='Dealer ###################')
        dealer.deck.result()

        player.deck.cal_score()

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

        if u_i.boolean(question='Do you want play another round?'):
            player.reset_deck()
            dealer.reset_deck()

        else:
            print(f' Final Balance = {player.balance}')
            credits()
            break
    quit()
    print('Achievement get "How did we get her" \n no seriously there quit command above me!')
=======

player = Player(ai_on=False)
dealer = Player(ai_on=True)
player.deck.cards[0] = Card(1, 1)
player.deck.cards[0].is_ace = True
player.deck.cards[1] = Card(1, 10)
player.deck.cards[2] = Card(1, 10)

print('Welcome to BlackJack!')
if u_i.boolean(question='Do you want to know the rules?'):
    print('https://bicyclecards.com/how-to-play/blackjack/')

while 1:
    print(f'current balance = {player.balance} $')
    while 1:
        j = u_i.postive_int_only('What do you want to bet')
        if j > player.balance:
            print('That is higher then you balance ')
            pass
        else:
            player.current_bet = j
            break

    print(f'Your bet has been set to {player.current_bet} $')

    while u_i.boolean(question='do you want to draw?'):
        player.deck.draw(header='Player ###################')
        dealer.deck.draw(display_info=False, header='Dealer ###################')

    player.deck.deck_print(header='Player ###################')
    player.deck.result()
    dealer.deck.draw(display_info=True, header='Dealer ###################')
    dealer.deck.result()

    player.deck.cal_score()

    if player.deck.score == 21:
        player.balance = player.balance + player.current_bet
        print('you win!')
    elif dealer.deck.score < player.deck.score <= 21:
        player.balance = player.balance + player.current_bet
        print('you win!')
    elif player.deck.score > 21:
        player.balance = player.balance - player.current_bet
        print('you lose')

    if u_i.boolean(question='Do you want play another round?'):
        player.reset_deck()
        dealer.reset_deck()

    else:
        print(f' Final Balance = {player.balance}')
        break
>>>>>>> origin/master
