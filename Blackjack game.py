import random

values = {"Two": 2, 'Three': 3, 'Four': 4, "Five": 5, "Six": 6, 'Seven': 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', "Queen", "King", 'Ace')
random_names = ["Mark", "Bob", "Wade", "Sean", "Amy", "Mandy", "Molly", "Gab"]


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.allcards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.allcards.append(new_card)
        print("\nThe Dealer has brought a new deck!\n")

    def shuffle(self):
        random.shuffle(self.allcards)
        print("\nThe Dealer has shuffled the deck!\n")


class Player:

    def __init__(self, name, score=0, ace_count=0, bank=200):
        self.name = name
        self.score = score
        self.hand = []
        self.score_list = []
        self.ace_count = ace_count
        self.bank = bank

    def __str__(self):
        return self.name

    def deal(self):
        self.hand.append(deck.allcards.pop(0))
        self.hand.append(deck.allcards.pop(0))
        self.score_list.append(values[self.hand[0].rank])
        self.score_list.append(values[self.hand[1].rank])
        self.score = sum(self.score_list)

    def draw(self):
        self.hand.append(deck.allcards.pop(0))
        self.score_list.append(values[self.hand[-1].rank])
        self.score = sum(self.score_list)
        print("You draw a card from the deck")

    def check_ace(self):
        ace_count = 0
        for card_on_hand in self.hand:
            if "Ace" in card_on_hand.rank:
                ace_count += 1
        while self.score > 21 and ace_count != 0:
            self.score = self.score - 10
            ace_count -= 1
        else:
            pass


class Dealer:

    def __init__(self, name, score=0, ace_count=0):
        self.name = name
        self.score = score
        self.hand = []
        self.score_list = []
        self.ace_count = ace_count

    def __str__(self):
        return self.name

    def deal(self):
        self.hand.append(deck.allcards.pop(0))
        self.hand.append(deck.allcards.pop(0))
        self.score_list.append(values[self.hand[0].rank])
        self.score_list.append(values[self.hand[1].rank])
        self.score = sum(self.score_list)

    def draw(self):
        self.hand.append(deck.allcards.pop(0))
        self.score_list.append(values[self.hand[-1].rank])
        self.score = sum(self.score_list)
        print("\nDealer " + self.name + " draws a card from the deck.\n")

    def check_ace(self):
        ace_count = 0
        for card_on_hand in self.hand:
            if "Ace" in card_on_hand.rank:
                ace_count += 1
        while self.score > 21 and ace_count != 0:
            self.score = self.score - 10
            ace_count -= 1
        else:
            pass


# Game Logic


gamerunning = True

while gamerunning == True:

    current_game = True
    p1 = Player(input("Enter your name:\n "))
    print(
        "************************************************\nWelcome to the game, " + p1.name + "!\n************************************************")
    print("You start with " + str(p1.bank) + " credits in your bank.")

    dealer_name = random.choice(random_names)
    p2 = Dealer(dealer_name)
    print("\nThe Dealer's name is " + p2.name + ". Say hi!\n")

    while current_game == True:

        p1_win = 0
        p2_win = 0

        deck = Deck()
        deck.shuffle()

        #
        bet = 0
        while bet not in range(1, 51) and bet < p1.bank:
            try:
                bet = int(input("\nChoose your bet! (minimum of 1 credit and maximum of 50 credits) \n"))
            except:
                print("\nNumbers only please!")
            else:
                if bet > p1.bank:
                    print("\nYou have less than what you're trying to bet. You only have {}.".format(p1.bank))
                    bet = 0
                    continue
                else:
                    pass
                if bet not in range(1, 51):
                    print("\nYou can't bet that! (minimum of 1 credit and maximum of 50 credits)\n")
                    bet = 0
                else:
                    pass

                    #

        p1.bank = p1.bank - bet

        p1.deal()
        print("\nYour cards are:\n")
        for card in p1.hand:
            print(card)
        p1.check_ace()
        p2.deal()
        p2.check_ace()
        print("\nOne of the dealer's card is ")
        print(p2.hand[0])

        if p1.score == 21:
            print("\nBlackJack!\n")

        else:
            p1choice_made = False
            p1bust = False
            while p1choice_made == False and p1bust == False:

                while p1.score < 21 and len(p1.hand) != 5:

                    choice = input("\nWhat would you like to do?\nA) Hit\nB) Stay\nC) View Score\n\n").upper()

                    if choice == "C":
                        print("\nYour Score is: ")
                        print(p1.score)

                    elif choice == "A":
                        p1.draw()
                        print("\nYour cards are now:\n")
                        for card in p1.hand:
                            print(card)
                        p1.check_ace()
                        if p1.score == 21:
                            print("\nYou have 21. You stay.\n")
                            p1choice_made = True
                            break
                        elif p1.score > 21:
                            print("\nYou bust!")
                            p1bust = True
                            break
                        else:
                            pass


                    elif choice == "B":
                        print("\nYou are satisfied with your cards.\n")
                        p1choice_made = True
                        break
                    else:
                        print("\nChoose between A, B or C only!\n")

                p1choice_made = True
                if p1bust == True or len(p1.hand) != 5:
                    pass
                else:
                    print("\nYou already have five cards.\n")

        print("\nYour Score is:\n" + str(p1.score))

        if p1bust == True:
            print("\nDealer " + p2.name + " wins!")
            p2bust = False
            p2_win = 1

        else:

            print(
                "*********************************\nIt's the dealer's turn now! Dealer hits until 17.\n*********************************")
            print("\nDealer " + p2.name + "'s cards are:\n")
            for card in p2.hand:
                print(card)
            p2.check_ace()

            if p2.score == 21:
                print("BlackJack!")

            else:
                p2choice_made = False
                p2bust = False
                while p2choice_made == False and p2bust == False:
                    while p2.score < 17 and len(p2.hand) != 5:
                        p2.draw()
                        print("\nDealer " + p2.name + "'s cards are:\n")
                        for card in p2.hand:
                            print(card)
                        p2.check_ace()
                        if p2.score > 21:
                            print("\nDealer " + p2.name + " busts!")
                            p2bust = True
                            break
                        else:
                            pass

                    p2choice_made = True
                    if p2bust == True:
                        pass
                    else:
                        print("\nDealer " + p2.name + " stays.")

            print("\nDealer " + p2.name + " score is:\n" + str(p2.score))

        if p1.score > p2.score and p1bust == False:
            print("\n" + p1.name + " wins and doubles the bet!")
            p1_win = 1
        elif p2.score > p1.score and p2bust == False:
            print("\nDealer " + p2.name + " wins!")
            p2_win = 1
        elif p2bust == True:
            print("\n" + p1.name + " wins!")
            p1_win = 1
        elif p1.score == p2.score:
            print("It's a draw!\n ")

        if p1_win == 1 and p2_win == 0:
            p1.bank = p1.bank + (bet * 2)
        elif p2_win == 1 and p1_win == 0:
            print("\n" + p1.name + " loses the bet!")
        else:
            print("\n" + p1.name + " gets back the bet!")
            p1.bank = p1.bank + bet

        print("\n" + p1.name + "'s bank is now worth " + str(p1.bank) + " credits!")

        if p1.bank <= 0:
            print("\nYou're bankrupt! You can't deal anymore, " + p1.name + "!")
            current_game = False
            break

        else:

            deal_again = ""
            while deal_again not in ["Y", "N"]:
                deal_again = (input("Deal again? y or n")).upper()
                if deal_again == "Y":
                    current_game = True
                    p1.hand = []
                    p2.hand = []
                    p1.score_list = []
                    p2.score_list = []
                    p1.score = 0
                    p2.score = 0
                elif deal_again == "N":
                    current_game = False
                    print("\nYou have cashed out " + str(p1.bank) + " credits. Thanks for playing, " + p1.name + "!")
                    break
                else:
                    print("please choose between y or n only!")

    play_again = ""
    while play_again not in ["Y", "N"]:
        play_again = (input("Would you like a new game? Y or N")).upper()
        if play_again == "Y":
            gamerunning = True
        elif play_again == "N":
            gamerunning = False
            print("Thanks for trying out blackjack!")
            break
        else:
            print("please choose between y or n only!")

# In[ ]:




