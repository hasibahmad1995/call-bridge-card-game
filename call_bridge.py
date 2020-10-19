from random import shuffle

color = ["Club", "Heart", "Diamond", "Spade"]
card_names = ["A", "K", "Q", "J"]

player1_name=input("Name please: ")
player2_name=input("Name please: ")
player3_name=input("Name please: ")
player4_name=input("Name please: ")
def card_shuffle():
    for i in range(2, 11):
        card_names.append(str(i))

    Deck = []
    for i in card_names:
        for j in color:
            zip(i, j)
            combination_cards = [i, j]
            Deck.append(combination_cards)
    shuffle(Deck)
    return Deck

deck = card_shuffle()
def card_arrange():
    hand = []
    for _ in range(4):
        hand.append(deck[0:13])
        del deck[0:13]
    return hand

player_hand = card_arrange()

def cards_in_hand():
    print(f"Cards in {player1_name}'s hand:",player_hand[0])
    print(f"Cards in {player2_name}'s hand:",player_hand[1])
    print(f"Cards in {player3_name}'s hand:",player_hand[2])
    print(f"Cards in {player4_name} hand:",player_hand[3])
cards_in_hand()

player1_bid=int(input(f"{player1_name} bid call:  "))
player2_bid=int(input(f"{player2_name} bid call:  "))
player3_bid=int(input(f"{player3_name} bid call:  "))
player4_bid=int(input(f"{player4_name} bid call:  "))

# def cards_in_hand():
#     print(f"Cards in {player1_name}'s hand:",player_hand[0])
#     print(f"Cards in {player2_name}'s hand:",player_hand[1])
#     print(f"Cards in {player3_name}'s hand:",player_hand[2])
#     print(f"Cards in {player4_name} hand:",player_hand[3])
# cards_in_hand()

board = []
def player_1():
    pl1 = int(input(f"{player1_name}'s turn: "))
    if player_hand[0][pl1]:
        board.append(player_hand[0][pl1])
        pl1_store = player_hand[0][pl1]
        player_hand[0].remove(player_hand[0][pl1])

    print(board)
    return pl1_store
player1=player_1()

def player_2():
    pl2 = int(input(f"{player2_name} turn: "))
    if player_hand[1][pl2]:
        board.append(player_hand[1][pl2])
        pl2_store = player_hand[1][pl2]
        player_hand[1].remove(player_hand[1][pl2])

    print(board)
    return pl2_store
player2=player_2()

def player_3():
    pl3 = int(input(f"{player3_name}'s turn: "))
    if player_hand[2][pl3]:
        board.append(player_hand[2][pl3])
        pl3_store = player_hand[2][pl3]
        player_hand[2].remove(player_hand[2][pl3])


    print(board)
    return pl3_store
player3=player_3()

def player_4():
    pl4 = int(input(f"{player4_name}'s turn: "))
    if player_hand[3][pl4]:
        board.append(player_hand[3][pl4])
        pl4_store = player_hand[3][pl4]
        player_hand[3].remove(player_hand[3][pl4])

    print(board)
    return pl4_store
player4= player_4()
player1_call = []
player2_call = []
player3_call = []
player4_call = []
value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
card_name = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
z = dict(zip(card_name, value))

def player1_hand_check():
    if player1[1]==color[3] and player2[1]==color[3] and player3[1]==color[3] and player4[1]==color[3]:
        max_check = max([z[player1[0]], z[player2[0]], z[player3[0]],z[player4[0]]])
        print(max_check)
        if max_check == z[player1[0]]:
            player1_call.append(board[:])
        elif max_check == z[player2[0]]:
            player2_call.append(board[:])
        elif max_check == z[player3[0]]:
            player3_call.append(board[:])
        else:
            player4_call.append(board[:])

    elif player1[1]==color[3] and player2[1]==color[3] and player3[1]==color[3]:
        max_check= max([z[player1[0]], z[player2[0]], z[player3[0]]])
        print(max_check)
        if max_check== z[player1[0]]:
            player1_call.append(board[:])
        elif max_check== z[player2[0]]:
            player2_call.append(board[:])
        elif max_check== z[player3[0]]:
            player3_call.append(board[:])

    elif player1[1]==color[3] and player2[1]==color[3] and player4[1]==color[3] and player3[1]!=color[3]:
        max_check = max([z[player1[0]], z[player2[0]], z[player4[0]]])
        print(max_check)
        if max_check == z[player1[0]]:
            player1_call.append(board[:])
        elif max_check == z[player2[0]]:
            player2_call.append(board[:])
        elif max_check == z[player4[0]]:
            player4_call.append(board[:])

    elif player1[1]==color[3] and player3[1]==color[3] and player4[1]==color[3] and player2[1]!=color[3]:
        max_check = max([z[player1[0]], z[player3[0]], z[player4[0]]])
        print(max_check)
        if max_check == z[player1[0]]:
            player1_call.append(board[:])
        elif max_check == z[player3[0]]:
            player3_call.append(board[:])
        elif max_check == z[player4[0]]:
            player4_call.append(board[:])

    elif player2[1]==color[3] and player3[1]==color[3] and player4[1]==color[3] and player1[1]!=color[3]:
        max_check = max([z[player2[0]], z[player3[0]], z[player4[0]]])
        print(max_check)
        if max_check == z[player2[0]]:
            player2_call.append(board[:])
        elif max_check == z[player3[0]]:
            player3_call.append(board[:])
        elif max_check == z[player4[0]]:
            player4_call.append(board[:])

    elif player1[1] == color[3] and player2[1] == color[3]:
        if z[player1[0]] > z[player2[0]]:
            player1_call.append(board[:])
        else:
            player2_call.append(board[:])

    elif player1[1] == color[3] and player3[1] == color[3]:
        if z[player1[0]] > z[player3[0]]:
            player1_call.append(board[:])
        else:
            player3_call.append(board[:])

    elif player1[1] == color[3] and player4[1] == color[3]:
        if z[player1[0]] > z[player4[0]]:
            player1_call.append(board[:])
        else:
            player4_call.append(board[:])

    elif player2[1] == color[3] and player3[1] == color[3]:
        if z[player2[0]] > z[player3[0]]:
            player2_call.append(board[:])
        elif z[player2[0]] < z[player3[0]]:
            player3_call.append(board[:])

    elif player2[1] == color[3] and player4[1] == color[3]:
        if z[player2[0]] > z[player4[0]]:
            player2_call.append(board[:])
        else:
            player4_call.append(board[:])

    elif player3[1] == color[3] and player4[1] == color[3]:
        if z[player3[0]] > z[player4[0]]:
            player3_call.append(board[:])
        else:
            player4_call.append(board[:])

    elif player1[1] == color[3] or player2[1] == color[3] or player3[1] == color[3] or player4[1] == color[3]:
        if color[3] == player1[1]:
            player1_call.append(board[:])
        elif color[3] == player2[1]:
            player2_call.append(board[:])
        elif color[3] == player3[1]:
            player3_call.append(board[:])
        elif color[3] == player4[1]:
            player4_call.append(board[:])
        else:
            pass

    elif  player1[1]==player2[1]==player3[1] ==player4[1]:
        max_check = max([z[player1[0]], z[player2[0]], z[player3[0]], z[player4[0]]])
        print(max_check)
        if max_check == z[player1[0]]:
            player1_call.append(board[:])
        elif max_check == z[player2[0]]:
            player2_call.append(board[:])
        elif max_check == z[player3[0]]:
            player3_call.append(board[:])
        else:
            player4_call.append(board[:])

    elif player1[1]==player2[1]==player3[1]:
        max_check = max([z[player1[0]], z[player2[0]], z[player3[0]]])
        print(max_check)
        if max_check == z[player1[0]]:
            player1_call.append(board[:])
        elif max_check == z[player2[0]]:
            player2_call.append(board[:])
        else:
            player3_call.append(board[:])

    elif player1[1]==player2[1]==player4[1]:
        max_check = max([z[player1[0]], z[player2[0]], z[player4[0]]])
        print(max_check)
        if max_check == z[player1[0]]:
            player1_call.append(board[:])
        elif max_check == z[player2[0]]:
            player2_call.append(board[:])
        else:
            player4_call.append(board[:])

    elif player1[1]==player3[1]==player4[1]:
        max_check = max([z[player1[0]], z[player3[0]], z[player4[0]]])
        print(max_check)
        if max_check == z[player1[0]]:
            player1_call.append(board[:])
        elif max_check == z[player3[0]]:
            player3_call.append(board[:])
        else:
            player4_call.append(board[:])

    elif player1[1]==player2[1]:
        max_check = max([z[player1[0]], z[player2[0]]])
        print(max_check)
        if max_check == z[player1[0]]:
            player1_call.append(board[:])
        else:
            player2_call.append(board[:])

    elif player1[1]==player3[1]:
        max_check = max([z[player1[0]], z[player3[0]]])
        print(max_check)
        if max_check == z[player1[0]]:
            player1_call.append(board[:])
        else:
            player3_call.append(board[:])

    elif player1[1]==player4[1]:
        max_check = max([z[player1[0]], z[player4[0]]])
        print(max_check)
        if max_check == z[player1[0]]:
            player1_call.append(board[:])
        else:
            player4_call.append(board[:])

    elif player1[1]!=player2[1] and player1[1]!=player3[1] and player1[1]!=player4[1]:
        if player2[1]==color[3]:
            player2_call.append(board[:])
        elif player3[1]==color[3]:
            player3_call.append(board[:])
        elif player4[1] == color[3]:
            player4_call.append(board[:])
        else:
            player1_call.append(board[:])

def player2_hand_check():
    if player2[1]==color[3] and player3[1]==color[3] and player4[1]==color[3] and player1[1]==color[3]:
        max_check = max([z[player2[0]], z[player3[0]], z[player4[0]],z[player1[0]]])
        print(max_check)
        if max_check == z[player2[0]]:
            player2_call.append(board[:])
        elif max_check == z[player3[0]]:
            player3_call.append(board[:])
        elif max_check == z[player4[0]]:
            player4_call.append(board[:])
        else:
            player1_call.append(board[:])

    elif player2[1]==color[3] and player3[1]==color[3] and player4[1]==color[3]:
        max_check= max([z[player2[0]], z[player3[0]], z[player4[0]]])
        print(max_check)
        if max_check== z[player2[0]]:
            player2_call.append(board[:])
        elif max_check== z[player3[0]]:
            player3_call.append(board[:])
        elif max_check== z[player4[0]]:
            player4_call.append(board[:])

    elif player2[1]==color[3] and player3[1]==color[3] and player1[1]==color[3] and player4[1]!=color[3]:
        max_check = max([z[player2[0]], z[player3[0]], z[player1[0]]])
        print(max_check)
        if max_check == z[player2[0]]:
            player2_call.append(board[:])
        elif max_check == z[player3[0]]:
            player3_call.append(board[:])
        elif max_check == z[player1[0]]:
            player1_call.append(board[:])

    elif player2[1]==color[3] and player4[1]==color[3] and player1[1]==color[3] and player3[1]!=color[3]:
        max_check = max([z[player2[0]], z[player4[0]], z[player1[0]]])
        print(max_check)
        if max_check == z[player2[0]]:
            player2_call.append(board[:])
        elif max_check == z[player4[0]]:
            player4_call.append(board[:])
        elif max_check == z[player1[0]]:
            player1_call.append(board[:])

    elif player2[1]==color[3] and player3[1]==color[3] and player4[1]==color[3] and player1[1]!=color[3]:
        max_check = max([z[player2[0]], z[player3[0]], z[player4[0]]])
        print(max_check)
        if max_check == z[player2[0]]:
            player2_call.append(board[:])
        elif max_check == z[player3[0]]:
            player3_call.append(board[:])
        elif max_check == z[player4[0]]:
            player4_call.append(board[:])

    elif player2[1] == color[3] and player3[1] == color[3]:
        if z[player2[0]] > z[player3[0]]:
            player2_call.append(board[:])
        else:
            player3_call.append(board[:])

    elif player2[1] == color[3] and player4[1] == color[3]:
        if z[player2[0]] > z[player4[0]]:
            player2_call.append(board[:])
        else:
            player4_call.append(board[:])

    elif player2[1] == color[3] and player1[1] == color[3]:
        if z[player2[0]] > z[player1[0]]:
            player2_call.append(board[:])
        else:
            player1_call.append(board[:])

    elif player3[1] == color[3] and player4[1] == color[3]:
        if z[player3[0]] > z[player4[0]]:
            player3_call.append(board[:])
        elif z[player3[0]] < z[player4[0]]:
            player4_call.append(board[:])

    elif player3[1] == color[3] and player1[1] == color[3]:
        if z[player3[0]] > z[player1[0]]:
            player3_call.append(board[:])
        else:
            player1_call.append(board[:])

    elif player4[1] == color[3] and player1[1] == color[3]:
        if z[player4[0]] > z[player1[0]]:
            player4_call.append(board[:])
        else:
            player1_call.append(board[:])

    elif player2[1] == color[3] or player3[1] == color[3] or player4[1] == color[3] or player1[1] == color[3]:
        if color[3] == player2[1]:
            player2_call.append(board[:])
        elif color[3] == player3[1]:
            player3_call.append(board[:])
        elif color[3] == player4[1]:
            player4_call.append(board[:])
        elif color[3] == player1[1]:
            player1_call.append(board[:])
        else:
            pass

    elif  player2[1]==player3[1]==player4[1] ==player1[1]:
        max_check = max([z[player2[0]], z[player3[0]], z[player4[0]], z[player1[0]]])
        print(max_check)
        if max_check == z[player2[0]]:
            player2_call.append(board[:])
        elif max_check == z[player3[0]]:
            player3_call.append(board[:])
        elif max_check == z[player4[0]]:
            player4_call.append(board[:])
        else:
            player1_call.append(board[:])

    elif player2[1]==player3[1]==player4[1]:
        max_check = max([z[player2[0]], z[player3[0]], z[player4[0]]])
        print(max_check)
        if max_check == z[player2[0]]:
            player2_call.append(board[:])
        elif max_check == z[player3[0]]:
            player3_call.append(board[:])
        else:
            player4_call.append(board[:])

    elif player2[1]==player3[1]==player1[1]:
        max_check = max([z[player2[0]], z[player3[0]], z[player1[0]]])
        print(max_check)
        if max_check == z[player2[0]]:
            player2_call.append(board[:])
        elif max_check == z[player3[0]]:
            player3_call.append(board[:])
        else:
            player1_call.append(board[:])

    elif player2[1]==player4[1]==player1[1]:
        max_check = max([z[player2[0]], z[player4[0]], z[player1[0]]])
        print(max_check)
        if max_check == z[player2[0]]:
            player2_call.append(board[:])
        elif max_check == z[player4[0]]:
            player4_call.append(board[:])
        else:
            player1_call.append(board[:])

    elif player2[1]==player3[1]:
        max_check = max([z[player2[0]], z[player3[0]]])
        print(max_check)
        if max_check == z[player2[0]]:
            player2_call.append(board[:])
        else:
            player3_call.append(board[:])

    elif player2[1]==player4[1]:
        max_check = max([z[player2[0]], z[player4[0]]])
        print(max_check)
        if max_check == z[player2[0]]:
            player2_call.append(board[:])
        else:
            player4_call.append(board[:])

    elif player2[1]==player1[1]:
        max_check = max([z[player2[0]], z[player1[0]]])
        print(max_check)
        if max_check == z[player2[0]]:
            player2_call.append(board[:])
        else:
            player1_call.append(board[:])

    elif player2[1]!=player3[1] and player2[1]!=player4[1] and player2[1]!=player1[1]:
        if player3[1]==color[3]:
            player3_call.append(board[:])
        elif player4[1]==color[3]:
            player4_call.append(board[:])
        elif player1[1] == color[3]:
            player1_call.append(board[:])
        else:
            player2_call.append(board[:])

def player3_hand_check():
    if player3[1]==color[3] and player4[1]==color[3] and player1[1]==color[3] and player2[1]==color[3]:
        max_check = max([z[player3[0]], z[player4[0]], z[player1[0]],z[player2[0]]])
        print(max_check)
        if max_check == z[player3[0]]:
            player3_call.append(board[:])
        elif max_check == z[player4[0]]:
            player4_call.append(board[:])
        elif max_check == z[player1[0]]:
            player1_call.append(board[:])
        else:
            player2_call.append(board[:])

    elif player3[1]==color[3] and player4[1]==color[3] and player1[1]==color[3]:
        max_check= max([z[player3[0]], z[player4[0]], z[player1[0]]])
        print(max_check)
        if max_check== z[player3[0]]:
            player3_call.append(board[:])
        elif max_check== z[player4[0]]:
            player4_call.append(board[:])
        elif max_check== z[player1[0]]:
            player1_call.append(board[:])

    elif player3[1]==color[3] and player4[1]==color[3] and player2[1]==color[3] and player1[1]!=color[3]:
        max_check = max([z[player3[0]], z[player4[0]], z[player2[0]]])
        print(max_check)
        if max_check == z[player3[0]]:
            player2_call.append(board[:])
        elif max_check == z[player4[0]]:
            player4_call.append(board[:])
        elif max_check == z[player2[0]]:
            player2_call.append(board[:])

    elif player3[1]==color[3] and player1[1]==color[3] and player2[1]==color[3] and player4[1]!=color[3]:
        max_check = max([z[player3[0]], z[player1[0]], z[player2[0]]])
        print(max_check)
        if max_check == z[player3[0]]:
            player3_call.append(board[:])
        elif max_check == z[player1[0]]:
            player1_call.append(board[:])
        elif max_check == z[player2[0]]:
            player2_call.append(board[:])

    elif player2[1]==color[3] and player3[1]==color[3] and player4[1]==color[3] and player1[1]!=color[3]:
        max_check = max([z[player2[0]], z[player3[0]], z[player4[0]]])
        print(max_check)
        if max_check == z[player2[0]]:
            player2_call.append(board[:])
        elif max_check == z[player3[0]]:
            player3_call.append(board[:])
        elif max_check == z[player4[0]]:
            player4_call.append(board[:])

    elif player3[1] == color[3] and player4[1] == color[3]:
        if z[player3[0]] > z[player4[0]]:
            player3_call.append(board[:])
        else:
            player4_call.append(board[:])

    elif player3[1] == color[3] and player1[1] == color[3]:
        if z[player3[0]] > z[player1[0]]:
            player3_call.append(board[:])
        else:
            player1_call.append(board[:])

    elif player3[1] == color[3] and player2[1] == color[3]:
        if z[player3[0]] > z[player2[0]]:
            player3_call.append(board[:])
        else:
            player2_call.append(board[:])

    elif player4[1] == color[3] and player1[1] == color[3]:
        if z[player4[0]] > z[player1[0]]:
            player4_call.append(board[:])
        elif z[player4[0]] < z[player1[0]]:
            player1_call.append(board[:])

    elif player4[1] == color[3] and player2[1] == color[3]:
        if z[player4[0]] > z[player2[0]]:
            player4_call.append(board[:])
        else:
            player2_call.append(board[:])

    elif player1[1] == color[3] and player2[1] == color[3]:
        if z[player1[0]] > z[player2[0]]:
            player1_call.append(board[:])
        else:
            player2_call.append(board[:])

    elif player3[1] == color[3] or player4[1] == color[3] or player1[1] == color[3] or player2[1] == color[3]:
        if color[3] == player3[1]:
            player3_call.append(board[:])
        elif color[3] == player4[1]:
            player4_call.append(board[:])
        elif color[3] == player1[1]:
            player1_call.append(board[:])
        elif color[3] == player2[1]:
            player2_call.append(board[:])
        else:
            pass

    elif  player3[1]==player4[1]==player1[1] ==player2[1]:
        max_check = max([z[player3[0]], z[player4[0]], z[player1[0]], z[player2[0]]])
        print(max_check)
        if max_check == z[player3[0]]:
            player3_call.append(board[:])
        elif max_check == z[player4[0]]:
            player4_call.append(board[:])
        elif max_check == z[player1[0]]:
            player1_call.append(board[:])
        else:
            player2_call.append(board[:])

    elif player3[1]==player4[1]==player1[1]:
        max_check = max([z[player3[0]], z[player4[0]], z[player1[0]]])
        print(max_check)
        if max_check == z[player3[0]]:
            player3_call.append(board[:])
        elif max_check == z[player4[0]]:
            player4_call.append(board[:])
        else:
            player1_call.append(board[:])

    elif player3[1]==player4[1]==player2[1]:
        max_check = max([z[player3[0]], z[player4[0]], z[player2[0]]])
        print(max_check)
        if max_check == z[player3[0]]:
            player3_call.append(board[:])
        elif max_check == z[player4[0]]:
            player4_call.append(board[:])
        else:
            player2_call.append(board[:])

    elif player3[1]==player1[1]==player2[1]:
        max_check = max([z[player3[0]], z[player1[0]], z[player2[0]]])
        print(max_check)
        if max_check == z[player3[0]]:
            player3_call.append(board[:])
        elif max_check == z[player1[0]]:
            player1_call.append(board[:])
        else:
            player2_call.append(board[:])

    elif player3[1]==player4[1]:
        max_check = max([z[player3[0]], z[player4[0]]])
        print(max_check)
        if max_check == z[player3[0]]:
            player3_call.append(board[:])
        else:
            player4_call.append(board[:])

    elif player3[1]==player1[1]:
        max_check = max([z[player3[0]], z[player1[0]]])
        print(max_check)
        if max_check == z[player3[0]]:
            player3_call.append(board[:])
        else:
            player1_call.append(board[:])

    elif player3[1]==player2[1]:
        max_check = max([z[player3[0]], z[player2[0]]])
        print(max_check)
        if max_check == z[player3[0]]:
            player3_call.append(board[:])
        else:
            player2_call.append(board[:])

    elif player3[1]!=player4[1] and player3[1]!=player1[1] and player3[1]!=player2[1]:
        if player4[1]==color[3]:
            player4_call.append(board[:])
        elif player1[1]==color[3]:
            player1_call.append(board[:])
        elif player2[1] == color[3]:
            player2_call.append(board[:])
        else:
            player3_call.append(board[:])

def player4_hand_check():
    if player4[1]==color[3] and player1[1]==color[3] and player2[1]==color[3] and player3[1]==color[3]:
        max_check = max([z[player4[0]], z[player1[0]], z[player2[0]],z[player3[0]]])
        print(max_check)
        if max_check == z[player4[0]]:
            player4_call.append(board[:])
        elif max_check == z[player1[0]]:
            player1_call.append(board[:])
        elif max_check == z[player2[0]]:
            player2_call.append(board[:])
        else:
            player3_call.append(board[:])

    elif player4[1]==color[3] and player1[1]==color[3] and player2[1]==color[3]:
        max_check= max([z[player4[0]], z[player1[0]], z[player2[0]]])
        print(max_check)
        if max_check== z[player4[0]]:
            player4_call.append(board[:])
        elif max_check== z[player1[0]]:
            player1_call.append(board[:])
        elif max_check== z[player2[0]]:
            player2_call.append(board[:])

    elif player4[1]==color[3] and player1[1]==color[3] and player3[1]==color[3] and player2[1]!=color[3]:
        max_check = max([z[player4[0]], z[player1[0]], z[player3[0]]])
        print(max_check)
        if max_check == z[player4[0]]:
            player4_call.append(board[:])
        elif max_check == z[player1[0]]:
            player1_call.append(board[:])
        elif max_check == z[player3[0]]:
            player3_call.append(board[:])

    elif player4[1]==color[3] and player2[1]==color[3] and player3[1]==color[3] and player1[1]!=color[3]:
        max_check = max([z[player4[0]], z[player2[0]], z[player3[0]]])
        print(max_check)
        if max_check == z[player4[0]]:
            player4_call.append(board[:])
        elif max_check == z[player2[0]]:
            player2_call.append(board[:])
        elif max_check == z[player3[0]]:
            player3_call.append(board[:])

    elif player2[1]==color[3] and player3[1]==color[3] and player4[1]==color[3] and player1[1]!=color[3]:
        max_check = max([z[player2[0]], z[player3[0]], z[player4[0]]])
        print(max_check)
        if max_check == z[player2[0]]:
            player2_call.append(board[:])
        elif max_check == z[player3[0]]:
            player3_call.append(board[:])
        elif max_check == z[player4[0]]:
            player4_call.append(board[:])

    elif player4[1] == color[3] and player1[1] == color[3]:
        if z[player4[0]] > z[player1[0]]:
            player4_call.append(board[:])
        else:
            player1_call.append(board[:])
    elif player4[1] == color[3] and player2[1] == color[3]:
        if z[player4[0]] > z[player2[0]]:
            player4_call.append(board[:])
        else:
            player2_call.append(board[:])

    elif player4[1] == color[3] and player3[1] == color[3]:
        if z[player4[0]] > z[player3[0]]:
            player4_call.append(board[:])
        else:
            player3_call.append(board[:])

    elif player1[1] == color[3] and player2[1] == color[3]:
        if z[player1[0]] > z[player2[0]]:
            player1_call.append(board[:])
        elif z[player1[0]] < z[player2[0]]:
            player2_call.append(board[:])

    elif player1[1] == color[3] and player3[1] == color[3]:
        if z[player1[0]] > z[player3[0]]:
            player1_call.append(board[:])
        else:
            player3_call.append(board[:])

    elif player2[1] == color[3] and player3[1] == color[3]:
        if z[player2[0]] > z[player3[0]]:
            player2_call.append(board[:])
        else:
            player3_call.append(board[:])

    elif player4[1] == color[3] or player3[1] == color[3] or player2[1] == color[3] or player1[1] == color[3]:
        if color[3] == player4[1]:
            player4_call.append(board[:])
        elif color[3] == player3[1]:
            player3_call.append(board[:])
        elif color[3] == player2[1]:
            player2_call.append(board[:])
        elif color[3] == player1[1]:
            player1_call.append(board[:])
        else:
            pass

    elif  player4[1]==player1[1]==player2[1] ==player3[1]:
        max_check = max([z[player4[0]], z[player1[0]], z[player2[0]], z[player3[0]]])
        print(max_check)
        if max_check == z[player4[0]]:
            player4_call.append(board[:])
        elif max_check == z[player1[0]]:
            player1_call.append(board[:])
        elif max_check == z[player2[0]]:
            player2_call.append(board[:])
        else:
            player3_call.append(board[:])

    elif player4[1]==player1[1]==player2[1]:
        max_check = max([z[player4[0]], z[player1[0]], z[player2[0]]])
        print(max_check)
        if max_check == z[player4[0]]:
            player4_call.append(board[:])
        elif max_check == z[player1[0]]:
            player1_call.append(board[:])
        else:
            player2_call.append(board[:])

    elif player4[1]==player1[1]==player3[1]:
        max_check = max([z[player4[0]], z[player1[0]], z[player3[0]]])
        print(max_check)
        if max_check == z[player4[0]]:
            player4_call.append(board[:])
        elif max_check == z[player1[0]]:
            player1_call.append(board[:])
        else:
            player3_call.append(board[:])

    elif player4[1]==player2[1]==player3[1]:
        max_check = max([z[player4[0]], z[player2[0]], z[player3[0]]])
        print(max_check)
        if max_check == z[player4[0]]:
            player4_call.append(board[:])
        elif max_check == z[player2[0]]:
            player2_call.append(board[:])
        else:
            player3_call.append(board[:])

    elif player4[1]==player1[1]:
        max_check = max([z[player4[0]], z[player1[0]]])
        print(max_check)
        if max_check == z[player4[0]]:
            player4_call.append(board[:])
        else:
            player1_call.append(board[:])

    elif player4[1]==player2[1]:
        max_check = max([z[player4[0]], z[player2[0]]])
        print(max_check)
        if max_check == z[player4[0]]:
            player4_call.append(board[:])
        else:
            player2_call.append(board[:])

    elif player4[1]==player3[1]:
        max_check = max([z[player4[0]], z[player3[0]]])
        print(max_check)
        if max_check == z[player4[0]]:
            player4_call.append(board[:])
        else:
            player3_call.append(board[:])

    elif player4[1]!=player1[1] and player4[1]!=player2[1] and player4[1]!=player3[1]:
        if player1[1]==color[3]:
            player1_call.append(board[:])
        elif player2[1]==color[3]:
            player2_call.append(board[:])
        elif player3[1] == color[3]:
            player3_call.append(board[:])
        else:
            player4_call.append(board[:])

player1_hand_check()

def player_board():
    print(f"{player1_name}:{player1_call}, {player2_name}: {player2_call}, {player3_name}: {player3_call}, {player4_name}: {player4_call}")
    print(f"""              {player1_name} has: {len(player1_call)}
              {player2_name} has: {len(player2_call)}
              {player3_name} has: {len(player3_call)}
              {player4_name} has: {len(player4_call)}""")
    print(f"Cards left in {player1_name}'s hand:",player_hand[0])
    print(f"Cards left in {player2_name}'s hand:",player_hand[1])
    print(f"Cards left in {player3_name}'s hand:",player_hand[2])
    print(f"Cards left in {player4_name}'s hand:",player_hand[3])
player_board()

player1_score=0
player2_score=0
player3_score=0
player4_score=0

player01_call=1
player02_call=1
player03_call=1
player04_call=1

while(True):
    while len(player_hand[0])!=0:
        if len(player1_call)==player01_call:
            board=[]
            player1=player_1()
            player2=player_2()
            player3=player_3()
            player4=player_4()
            player1_hand_check()
            player_board()
            grab_player1_call_length=len(player1_call)
            player01_call+=1

        elif len(player2_call)==player02_call:
            board=[]
            player2=player_2()
            player3=player_3()
            player4=player_4()
            player1=player_1()
            player2_hand_check()
            player_board()
            grab_player2_call_length = len(player2_call)
            player02_call+=1

        elif len(player3_call)==player03_call:
            board=[]
            player3=player_3()
            player4=player_4()
            player1=player_1()
            player2=player_2()
            player3_hand_check()
            player_board()
            grab_player3_call_length = len(player3_call)
            player03_call+=1

        elif len(player4_call) == player04_call:
            board = []
            player4=player_4()
            player1=player_1()
            player2=player_2()
            player3=player_3()
            player3_hand_check()
            player_board()
            grab_player4_call_length = len(player4_call)
            player04_call += 1

    difference_player1_1 = grab_player1_call_length-player1_bid
    difference_player1_2 = player1_bid - grab_player1_call_length
    if len(player1_call) == player1_bid:
        player1_score += player1_bid
        print(f"{player1_name}'s score is: ", player1_score)
    elif len(player1_call) > player1_bid:
        player1_score -= difference_player1_1
        print(f"{player1_name}'s score is: ", player1_score)
    else:
        player1_score -= difference_player1_2
        print(f"{player1_name}'s is: ", player1_score)

    difference_player2_1 = grab_player2_call_length- player2_bid
    difference_player2_2 = player2_bid - grab_player2_call_length
    if len(player2_call) == player2_bid:
        player2_score += player2_bid
        print(f"{player2_name}'s score is: ", player2_score)
    elif len(player2_call) > player2_bid:
        player2_score -= difference_player2_1
        print(f"{player2_name}'s score is: ", player2_score)
    else:
        player2_score -= difference_player2_2
        print(f"{player2_name}'s score is: ", player2_score)

    difference_player3_1 = grab_player3_call_length- player3_bid
    difference_player3_2 = player3_bid - grab_player3_call_length
    if len(player3_call) == player3_bid:
        player3_score += player3_bid
        print(f"{player3_name}'s score is: ", player3_score)
    elif len(player3_call) > player3_bid:
        player3_score -= difference_player3_1
        print(f"{player3_name}'s score is: ", player3_score)
    else:
        player3_score -= difference_player3_2
        print(f"{player3_name}'s is: ", player3_score)

    difference_player4_1 = grab_player4_call_length - player4_bid
    difference_player4_2 = player4_bid - grab_player4_call_length
    if len(player4_call) == player4_bid:
        player4_score += player4_bid
        print(f"{player4_name}'s score is: ", player4_score)
    elif len(player4_call) > player4_bid:
        player4_score -= difference_player4_1
        print(f"{player4_name}'s score is: ", player4_score)
    else:
        player4_score -= difference_player4_2
        print(f"{player4_name}'s score is: ", player4_score)

    deck = card_shuffle()
    player_hand = card_arrange()
    cards_in_hand()
    board = []
    player1_bid=int(input(f"{player1_name}'s call:  "))
    player2_bid=int(input(f"{player3_name}'s call:  "))
    player3_bid=int(input(f"{player4_name}'s call:  "))
    player4_bid=int(input(f"{player4_name}'s bid call:  "))

    player1=player_1()
    player2=player_2()
    player3=player_3()
    player4=player_4()
