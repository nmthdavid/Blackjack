import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
print()
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    card = random.choice(cards)
    return card

def cards_sum(list):
    sum_of = 0
    for card in list:
        sum_of += card
    
    if sum_of == 21:
        return 0
    else:
        return sum_of

def check_winner():
    if cards_sum(staff_cards)>21:
        print(f"You won: staff:{staff_cards} user:{user_cards}")
    elif cards_sum(staff_cards)>17 and cards_sum(staff_cards)>cards_sum(user_cards):
        print(f"You lost: staff:{staff_cards} user:{user_cards}")
    elif cards_sum(staff_cards)>17 and cards_sum(staff_cards)<cards_sum(user_cards):
        print(f"You won: staff:{staff_cards} user:{user_cards}")
    elif cards_sum(staff_cards)==cards_sum(user_cards):
        print(f"It's a draw: staff:{staff_cards} user:{user_cards}")
    else:
        while cards_sum(staff_cards) <= 17:
            x=deal_card()
            staff_cards.append(x)
        if cards_sum(staff_cards)==0 and cards_sum(staff_cards)!=0:
            print(f"You lost: staff:{staff_cards} user:{user_cards}")
        if cards_sum(staff_cards) > 21:
            print(f"You won: staff:{staff_cards} user:{user_cards}")
        elif cards_sum(staff_cards)>cards_sum(user_cards) and cards_sum(staff_cards)<=21 and cards_sum(user_cards)<=21:
            print(f"You lost: staff:{staff_cards} user:{user_cards}")
        elif cards_sum(staff_cards)<cards_sum(user_cards):
            print(f"You won: staff:{staff_cards} user:{user_cards}")
        elif cards_sum(staff_cards)==cards_sum(user_cards):
            print(f"It's a draw: staff:{staff_cards} user:{user_cards}")
        
print("Welcome to the Blackjack Game!")
ison = input("Press S to start the game: ")
on = False
if ison == "S":
    on = True
    
user_cards = []
staff_cards = []
user_sum = 0
staff_sum = 0

user_cards.append(deal_card()) 
user_cards.append(deal_card())
staff_cards.append(deal_card())
staff_cards.append(deal_card())
    
print(f"Your cards are : {user_cards} and the sum of your hand is {cards_sum(user_cards)}")
print(f"Staff cards are : {staff_cards[0]} and X")
on2 = True

if cards_sum(user_cards) == 0 and cards_sum(staff_cards)==0:
    print("It's a draw")
    on2 = False
    
while on2:
    choice = input("Would you like to continue?(Y/N): ")
    if choice == "N":
        check_winner()
        break
    else:
        new = deal_card()    
        user_cards.append(new)
        if cards_sum(user_cards) > 21:
            print(f"You lost, you got: {new}")
            break
        elif cards_sum(user_cards) == 0:
            print("You won")
            break
        print(f"Your cards are : {user_cards} and the sum of your hand is {cards_sum(user_cards)}")
