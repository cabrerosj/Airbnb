from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Returns a random card"""
    card = choice(list(cards))
    return card


def calculate_score(cards):
    """Totals the values of each player's hand"""
    hand = cards
    total_value = sum(cards)
    if total_value == 21 and len(hand) == 2:
        return 0
    if 11 in hand and total_value > 21:
        hand.remove(11)
        hand.append(1)
        calculate_score(hand)
    return total_value


def compare_totals(user_total, dealer_total):
    """Compares the totals of the hands and declares wins/losses"""
    if user_total == 0:
        return "You got BlackJack! You win!"
    elif dealer_total == 0:
        return "The dealer got BlackJack. You lose."
    elif user_total > 21:
        return "You went over 21. You lose."
    elif dealer_total > 21:
        return "The dealer went over 21! You win!"

    # *** If you and the dealer go over 21, you still lose ***

    if user_total == dealer_total and user_total > 21:
        return "You went over 21. You lose."
    elif user_total == dealer_total:
        return "It's a draw!"
    elif user_total > dealer_total:
        return "You win!"
    else:
        return "You lose."


user_cards = []
dealer_cards = []
game_over = False

# *** Deals 2 cards for each person at the start of the game ***

for _ in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

# *** Keeps game going as long as game_over == False ***

while not game_over:
    user_total = calculate_score(user_cards)
    dealer_total = calculate_score(dealer_cards)

    print(f"Your cards: {user_cards}\nDealer's first card: {dealer_cards[0]}")
    if user_total == 0 or dealer_total == 0 or user_total > 21:
        game_over = True
    else:
        another_card = input("Do you want another card? (Y/N)\n")
        if another_card.lower() == "y":
            user_cards.append(deal_card())
        else:
            game_over = True

# *** Casino rules state that dealer keeps drawing a card if their total is less than 17 ***
while 17 > dealer_total != 0:
    dealer_cards.append(deal_card())
    dealer_total = calculate_score(dealer_cards)

compare_totals(user_total, dealer_total)

# *** Shows each person's hands and totals ***

# *** Shows the user or dealer's total as 21 as the function compare_totals returns 0 ***
if user_total == 0:
    print(f"Your cards: {user_cards}\nYour total: 21\nDealer's cards: {dealer_cards}\nDealer's total: {dealer_total}")
elif dealer_total == 0:
    print(f"Your cards: {user_cards}\nYour total: {user_total}\nDealer's cards: {dealer_cards}\nDealer's total: 21")
else:
    print(f"Your cards: {user_cards}\nYour total: {user_total}\nDealer's cards: {dealer_cards}\nDealer's total: {dealer_total}")

print(compare_totals(user_total, dealer_total))