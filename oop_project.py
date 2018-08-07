
# For this project will use OOP to crate a card game.
# Card game 'War' for two player, here are basic rules： 

from random import shuffle

# two useful variables for creating cards
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split() 

class Deck:
  """
    This is Deck clas, will create a deck of cards to initiate play. You can then use Deck list of cards to split in half and give to the players. 
    It will use suite and ranks to create the decj. Ir should also have a method for splitting/cutting the deck in half and shuffling the deck.
  """
  def __init__(self):

    print("Creating New Ordered Deck!")
    mycards=[]
    for r in RANKS:
      for s in SUITE:
        mycards.append((s,r))
    self.allcards = mycards
  def shuffle(self):
    print("Shuffling deck")
    shuffle(self.allcards)
  
  def split_in_half(self):
    return(self.allcards[:26], self.allcards[26:])

class Hand:
  """
    This is the hand class. Player use hand to add or remove cards. There should have add and remove cards method
  """
  def __init__(self, cards):
    self.cards = cards

  def __str__(self):
    return "Contains {} cards".format(len(self.cards))
  def add(self, added_cards):
    self.cards.extend(added_cards)
  def remove_cards(self):
    return self.cards.pop()

class Player:
  """
    This is the Player class, which takes in a name and an instance of a Hand class object. The Player can play cards and check if they still have cards.
  """
  def __init__(self, name, hand):
    self.name = name
    self.hand = hand
  def play_card(self):
    drawn_card = self.hand.remove_cards()
    print("{} has placed: {}".format(self.name, drawn_card))
    print("\n")
    return drawn_card

  def remove_war_cards(self):
    war_cards = []
    if len(self.hand.cards)<3:
      return self.hand.cards
    else:
      for x in range(3):
      # war_cards.append(self.hand.cards.pop()) 
        war_cards.append(self.hand.remove_cards)  #same result if use above line code
      return war_cards
  def still_has_cards(self):
    """
      return True if player still has cards left
    """
    return len(self.hand.cards) != 0

#### GAME PLAY

print("Welcome to War, let's begin...")

# Create new deck and split it in half:
d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

# Create two players
computer_player = Player("Computer", Hand(half1))
name = input("What is your name?")
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0
while user.still_has_cards() and computer_player.still_has_cards():
  total_rounds += 1
  print("Time for new round")
  print("Here are the current standings")
  print(user.name+"has the count: "+str(len(user.hand.cards)))
  print(user.name+"has the count: "+str(len(computer_player.hand.cards)))
  print("play a card")
  print("\n")

  table_cards=[]

  computer_card = computer_player.play_card()
  user_card = user.play_card()

  table_cards.append(computer_card)
  table_cards.append(user_card)

  if computer_card[1] == user_card[1]:
    war_count += 1
    print("War")

    table_cards.extend(user.remove_war_cards())
    table_cards.extend(computer_player.remove_war_cards())

    if RANKS.index(computer_card[1])< RANKS.index(user_card[1]):
      user.hand.add(table_cards)
    else:
      computer_player.hand.add(table_cards)
  else:
    if RANKS.index(computer_card[1])< RANKS.index(user_card[1]):
      user.hand.add(table_cards)
    else:
      computer_player.hand.add(table_cards)

print("game over, number of rounds: "+str(total_rounds))
print("a war hanppend "+str(war_count)+" times")
print("Does computer_player still have cards?")
print(str(computer_player.still_has_cards()))
print("Does user still have cards?")
print(str(user.still_has_cards()))