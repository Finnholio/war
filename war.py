import random

suits = ["♠", "♥", "♣", "♦"]
royals = ["J", "Q", "K", "A"]

def makeDeck(amount):
    deck = []
    for i in range(0, amount):
        for suit in suits:
            for i in range(2, 11 + len(royals)):
                if i <= 10:
                    deck.append(suit + str(i))

                else:
                    deck.append(suit + royals[i-11])


    return deck


def compare(card1, card2):
    value1 = getValue(card1)
    value2 = getValue(card2)

    if value1 > value2:
        return 1
    elif value2 > value1:
        return -1
    else:
        return 0

def getValue(value):
    if len(value) == 3:
        return 10

    trueValue = value[1]

    if trueValue == "J":
        return 11

    elif trueValue == "Q":
        return 12

    elif trueValue == "K":
        return 13

    elif trueValue == "A":
        return 14

    else:
        return int(trueValue)


def dealDecks(deck):
    deckLength = len(deck)

    return deck[0 : int(deckLength/2)], deck[int(deckLength/2) : deckLength]

deck = makeDeck(1)

random.shuffle(deck)
print(deck)

player1, player2 = dealDecks(deck)
print(player1)
print(player2)

while len(player1) > 0 and len(player2) > 0:
    roundResult = 0
    roundCards = []

    while (roundResult == 0):
        roundResult = compare(player1[0], player2[0])

        print(player1[0] + ", " + player2[0])
        print("player1 current cards : " + str(len(player1)))
        print("player2 current cards : " + str(len(player2)))
        print("\n")

        roundCards.append(player1[0])
        roundCards.append(player2[0])

        del player1[0]
        del player2[0]

        print(len(roundCards))

        if roundResult == 1:
            player1 += roundCards
            print("Player 1 Wins!")

        elif roundResult == -1:
            player2 += roundCards
            print("Player 2 Wins!")

        #uinput = input("")


        print("\n\n\n")


