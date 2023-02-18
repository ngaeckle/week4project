"""
Python Blackjack
For this project you will make a Blackjack game using Python. Click here to familiarize yourself with the the rules of the game. You won't be implementing every rule "down to the letter" with the game, but we will doing a simpler version of the game. This assignment will be given to further test your knowledge on object-oriented programming concepts.

Rules:
1. The game will have two players: the Dealer and the Player. The game will start off with a deck of 52 cards. The 52 cards will consist of 4 different suits: Clubs, Diamonds, Hearts and Spades. For each suit, there will be cards numbered 1 through 13.



Note: No wildcards will be used in the program
2. When the game begins, the dealer will shuffle the deck of cards, making them randomized. After the dealer shuffles, it will deal the player 2 cards and will deal itself 2 cards from. The Player should be able to see both of their own cards, but should only be able to see one of the Dealer's cards.
3. The objective of the game is for the Player to count their cards after they're dealt. If they're not satisfied with the number, they have the ability to 'Hit'. A hit allows the dealer to deal the Player one additional card. The Player can hit as many times as they'd like as long as they don't 'Bust'. A bust is when the Player is dealt cards that total more than 21.
4. If the dealer deals the Player cards equal to 21 on the first deal, the Player wins. This is referred to as Blackjack. Blackjack is NOT the same as getting cards that equal up to 21 after the first deal. Blackjack can only be attained on the first deal.
5. The Player will never see the Dealer's hand until the Player chooses to 'stand'. A Stand is when the player tells the dealer to not deal it anymore cards. Once the player chooses to Stand, the Player and the Dealer will compare their hands. Whoever has the higher number wins. Keep in mind that the Dealer can also bust.


This will be an exercise of how well you understand OOP(Object Oriented Programming). In this project, you will be using "Pair-Programming" to complete the assignment.
"""

from random import shuffle

class Dealer():
    def __init__(self, deck, opponent) -> None:
        self.deck = deck
        self.opponent = opponent
        self.hand = []
        self.total = 0

    def deal(self, num, opponent = None):
        i = 0
        while i < num:
            i+=1
            if opponent:
                self.opponent.hand.append(self.deck.shuffled_list[0])
                self.deck.shuffled_list.pop(0)
            else:
                self.hand.append(self.deck.shuffled_list[0])
                self.deck.shuffled_list.pop(0)

    def print_hand(self):
        i = 0
        for value in self.hand:
            self.deck.deck[self.hand[i]].show()
            print(self.deck.deck[self.hand[i]])
            i+=1
        self.get_total()
        print(f" Total: {self.total}")
        print()
        print("Dealers Hand ^^^^^^^^^^^^^^")

    def get_total(self):
        has_an_ace = False
        self.total = 0
        for value in self.hand:
            for key in self.deck.deck:
                if value == key and value != 11:
                    self.total += self.deck.deck[key].value
                    if self.deck.deck[key].value == 11:
                        has_an_ace = True
        if self.total > 21 and has_an_ace:
            self.total -= 10


    def hit(self, opponent = None):
        if opponent:
            opponent.hand.append(self.deck.shuffled_list[0])
            self.deck.shuffled_list.pop(0)
        else:
            self.hand.append(self.deck.shuffled_list[0])
            self.deck.shuffled_list.pop(0)


class Player():
    def __init__(self, deck) -> None:
        self.deck = deck
        self.hand= []
        self.total = 0

    def show_cards(self):
        for value in self.hand:
            for key in self.deck.deck:
                if value == key:
                    self.deck.deck[key].show()
                    print(self.deck.deck[key])
        self.get_total()
        print(f" Total: {self.total}")
        print()
        print("Players Hand ^^^^^^^^^^^^^^")

    def get_total(self):
        has_an_ace = False
        self.total = 0
        for value in self.hand:
            for key in self.deck.deck:
                if value == key:
                    self.total += self.deck.deck[key].value
                    if self.deck.deck[key].value == 11:
                        has_an_ace = True
        if self.total > 21 and has_an_ace:
            self.total -= 10
        
class Deck():
    def __init__(self) -> None:
        self.suits = {
            0: 'Clubs',
            1: 'Diamonds',
            2: 'Hearts',
            3: 'Spades'
            }
        self.cards = {
            0: 'Ace',
            1: '2',
            2: '3',
            3: '4',
            4: '5',
            5: '6',
            6: '7',
            7: '8',
            8: '9',
            9: '10',
            10: 'Jack',
            11: 'Queen',
            12: 'King'
            }
        self.deck = {}
        self.shuffled_list = []
        self.used_cards = {}


    def create_deck(self):
        i = 0
        for suit in self.suits:
            for card in self.cards:
                self.deck[i] = Card(self.suits[suit], self.cards[card])
                i+=1

    def shuffle_deck(self):
        if self.deck and not self.shuffled_list:
            # ready to shuffle deck
            for key in self.deck:
                self.shuffled_list.append(key)
            #print(self.shuffled_list)
            shuffle(self.shuffled_list)
            #print(self.shuffled_list)


        elif self.deck:
            print("You already shuffled the deck")
        
        else:
            print("Create a deck first")

class Card():
    def __init__(self, suit, card):
        self.suit = suit
        self.card = card
        self.shown = False
        try:
            self.value = int(self.card)
        except:
            if self.card == "Ace":
                self.value = 11
            else:
                self.value = 10

    def __repr__(self):
        if self.card == "10":
            self.card = "X"
        if self.shown:
            if self.suit == 'Spades':
                return f"  _____ \n |{self.card[0]} .  | \n | /.\ | \n |(_._)| \n |  |  | \n |____{self.card[0]}|"
            elif self.suit == "Diamonds":
                return f"  _____ \n |{self.card[0]} ^  | \n | / \ | \n | \ / | \n |  .  | \n |____{self.card[0]}|"
            elif self.suit == "Clubs":
                return f"  _____ \n |{self.card[0]} _  | \n | ( ) | \n |(_'_)| \n |  |  | \n |____{self.card[0]}|"
            elif self.suit == "Hearts":
                return f"  _____ \n |{self.card[0]}_ _ | \n |( v )| \n | \ / | \n |  .  | \n |____{self.card[0]}|"
        else:
            return f"  _____ \n |\ ~ /| \n |)):((| \n |)):((| \n |)):((| \n |/_~_\|"

    
    def show(self):
        self.shown = True
    
    def hide(self):
        self.shown = False


def game():
    #set up game
    winner = ""
    stand = False
    game_deck = Deck()
    game_deck.create_deck()
    game_deck.shuffle_deck()
    player = Player(game_deck)
    dealer = Dealer(game_deck, player)
    #Start game
    dealer.deal(2,player)
    dealer.deal(2)
    dealer.deck.deck[dealer.hand[0]].show()
    print(dealer.deck.deck[dealer.hand[0]])
    print(dealer.deck.deck[dealer.hand[1]])
    print()
    print("Dealers Hand ^^^^^^^^^^^^^^")
    player.show_cards()
    if player.total == 21:
        winner = "Player"
        print("BLACKJACK!")
    #Ready to begin making moves
    while not winner:
        if not stand:
            choice = input("What would you like to do? stand/hit? ").lower()
            if choice == "hit":
                dealer.hit(player)
                player.show_cards()
                if player.total > 21:
                    print("Bust!")
                    winner = "Dealer"
                    break
            elif choice == "stand":
                stand = True
                dealer.print_hand()
                input("Ready for next move? ")
        else:
            dealer.hit()
            dealer.print_hand()
            if dealer.total > 21:
                print("Bust!")
                winner = "Player"
                break
            input("Ready for next move? ")

        if player.total == 21:
            stand = True

        if dealer.total > player.total:
                winner = "Dealer"
                break

        if dealer.total == player.total:
            print("Tie!")
            winner = "Nobody"

    print(f"{winner} wins!")
    print(f"Final score: Player: {player.total} | Dealer: {dealer.total}")

game()   


