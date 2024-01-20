import random
import pdb

# war, the card game of chance where 26 battles take place between rival armies.
# the higher card wins each battle. ties accumulate a bonus to be won at the next battle.
# for each battle, outputs the number of cards left, the two cards drawn, and the win totals.
# if a battle is a tie, its value is accrued towards the next one that is won.

# build deck list, containing tuples of the names and values of each card
# the order of the names list determines the cards' values
# the deck is 52 tuples like this:  ('Jack of Diamonds', 11)
names = [ 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace' ]
suits = [ 'Hearts', 'Diamonds', 'Spades', 'Clubs' ]

# ***** FIXED ****** deck was not shuffled and I shuffled it with using random module
random.shuffle((deck:= [ (name + ' of ' + suit, suits.index(suit) ) for name in names for suit in suits ]))


bonus, scoreA, scoreB = 0, 0, 0

# as long as there are cards left in the deck, draw pairs for each battle
# while loop is safe as long as the only thing that happens to deck is .pop()



while deck:

 # compare a pair of cards' values, tally scores and adjust bonus
 # there are three possible cases; in case of a win the bonus is paid out, otherwise it rises
 cards = cardA, cardB = deck.pop(), deck.pop()  # **** ADDED **** stored pair of cards in a tuple for mapping
 valueA, valueB =  (map(lambda x: names.index(x[0].split(" ")[0]), cards))  # **** IMPLEMENTED **** to get actual values for each card of pairs


# ****** FIXED ***** before compration was between suits,
# now between values of numbers of two cards
 if valueA == valueB:
  bonus += 1      # **** FIXED **** Before it was " bouns += scoreA " -Team A was cheating- 
  outcome = 'ties'

 elif valueA > valueB:
  scoreA += 1 + bonus
  bonus = 0
  outcome = 'beats'
 else:
  scoreB += 1 + bonus
  bonus = 0
  outcome = 'is beaten by' # ****** FIXED ****** Indendation is fixed. It was not under else statement

 # display the outcome of each battle, current winnings, and how much left to be won
 event = "The {} {} the {}!".format ( cardA[0], outcome, cardB[0])

# ***** FIXED ***** first curly braces were "{:55.55}"  '.55' for decimal places and it was unnecessary
# ':55' was not perfectly enough for space holding for the event string variable, I changed it to 60
 print ( '{:60}  ${} to ${}, ${} left.'.format ( event, scoreA, scoreB, int(len(deck)/2)))




