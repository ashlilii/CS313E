#  File: Poker.py

#  Description: Program plays a game of poker with 2-6 players and determines
#  hand types and winner of the hands

import sys, random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank

class Deck (object):
  # constructor
  def __init__ (self, num_decks = 1):
    self.deck = []
    for i in range (num_decks):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  # constructor
  def __init__ (self, num_players = 2, num_cards = 5):
    self.deck = Deck()
    self.deck.shuffle()
    self.all_hands = []
    self.numCards_in_Hand = num_cards

    # deal the cards to the players one at a time (round robin)
    for i in range (num_players):
      hand = []
      self.all_hands.append(hand)

    card_counter = 0
    while card_counter < (num_players * self.numCards_in_Hand):
      # game deals one card to each player
      for k in range(0, len(self.all_hands)):
        self.all_hands[k].append(self.deck.deal())
        card_counter += 1

    
  # simulate the play of poker
  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.all_hands)):
      sorted_hand = sorted (self.all_hands[i], reverse = True)
      self.all_hands[i] = sorted_hand
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str (card) + ' '
      print ('Player ' + str(i + 1) + ' : ' + hand_str)

    hand_type = []
    hand_points = {}
    print('')

    # goes through all the types of hands
    for i in range (len(self.all_hands)):
      sorted_hand = sorted (self.all_hands[i], reverse = True)
      self.all_hands[i] = sorted_hand
      test_hand = []
      for card in sorted_hand:
        test_hand.append(card)
      hand_type = self.is_royal(test_hand)
      if hand_type[0] == 0:
        hand_type = self.is_straight_flush(test_hand)
        if hand_type[0] == 0:
          hand_type = self.is_four_kind(test_hand)
          if hand_type[0] == 0:
            hand_type = self.is_full_house(test_hand)
            if hand_type[0] == 0:
              hand_type = self.is_flush(test_hand)
              if hand_type[0] == 0:
                hand_type = self.is_straight(test_hand)
                if hand_type[0] == 0:
                  hand_type = self.is_three_kind(test_hand)
                  if hand_type[0] == 0:
                    hand_type = self.is_two_pair(test_hand)
                    if hand_type[0] == 0:
                      hand_type = self.is_one_pair(test_hand)
                      if hand_type[0] == 0:
                        hand_type = self.is_high_card(test_hand)
      # puts all player number and hand points into a dictionary
      hand_points[str(i+1)] = str(hand_type[0])
      print ('Player ' + str(i + 1) + ': ' + str(hand_type[1]))

    # calculates who is the winner
    winner_points = 0
    winner = ''
    possible_ties = []
    # utilizes dictionary above ^
    for i in range(1, len(hand_points)):
      entry = str(i)
      hand_points_adjusted = int(hand_points[entry])
      if hand_points_adjusted > winner_points:
        # if player's hand is bigger than the previous winner, it will see
        # if there are other same values to see if there is a tie
        for j in range(i, len(hand_points)):
          if hand_points_adjusted == int(hand_points[str(j+1)]):
            possible_ties.append(str(j))
        winner_points = hand_points_adjusted
        winner = entry
    # tie output
    if len(possible_ties) > 1:
      for i in range(0, len(possible_ties)):
        position = possible_ties[i]
        print('Player ' + str(position) + ' ties.')
    # normal winner output
    else:
      print('\n' + 'Player ' + winner + ' wins.')

  def is_royal(self, hand):
    royal_flush = False
    same_suit = hand[0].suit
    royal_flush_count = 0
    # if first card is not A, there's no point in continuing
    if hand[0].rank != 14:
      return 0, ''

    # checks suits
    for i in range (len(hand) - 1):
      if hand[i].suit != hand[0].suit:
        return 0, ''
    
    # checks if consecutive
    for i in range (len(hand) - 1):
      if hand[i + 1].rank == hand[i].rank - 1:
        royal_flush_count += 1
        
      if royal_flush_count == 4:
        royal_flush = True
    
    if (not royal_flush):
      return 0, ''

    points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Royal Flush'

  def is_straight_flush (self, hand):
    straight_flush = False
    same_suit = hand[0].suit
    straight_flush_count = 0

    # checks suit
    for i in range (len(hand) - 1):
      if hand[i].suit != hand[0].suit:
        return 0, ''
    
    # checks if consecutive
    for i in range (len(hand) - 1):
      if hand[i + 1].rank == hand[i].rank - 1:
        straight_flush_count += 1
      if straight_flush_count == 4:
        straight_flush = True
    
    if (not straight_flush):
      return 0, ''

    points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Straight Flush'


  def is_four_kind (self, hand):
    four_kind = False
    # sees if there are four same cards in a row
    for i in range(0, len(hand)-3):
      if hand[i].rank == hand[i+3].rank:
        # places four of a kind at beginning of hand
        hand.insert(0, hand.pop(i))
        hand.insert(1, hand.pop(i+1))
        hand.insert(2, hand.pop(i+2))
        hand.insert(3, hand.pop(i+3))
        four_kind = True
          
    if (not four_kind):
      return 0, ''
          
    if (not four_kind):
      return 0, ''

    points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Four of a Kind'

  def is_full_house (self, hand):
    full_house = False
    # sees if first half or second half has a pair
    if (hand[0].rank == hand[1].rank) and (hand[3].rank == hand[4].rank):
      # sees if pair can be three of a kind
      if (hand[2].rank == hand[0].rank):
        full_house = True
      # if three of kind in second half, place at the beginning of hand
      elif (hand[2].rank == hand[4].rank):
        hand.insert(0, hand.pop(2))
        hand.insert(1, hand.pop(3))
        hand.insert(2, hand.pop(4))
        full_house = True
          
    if (not full_house):
      return 0, ''

    points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Full House'

  def is_flush (self, hand):
    flush = True
    same_suit = hand[0].suit
    # checks suit
    for i in range (len(hand) - 1):
      if hand[i].suit != hand[0].suit:
        flush = False
        break
    
    if (not flush):
      return 0, ''

    points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Flush'


  def is_straight (self, hand):
    straight = False
    straight_count = 0
    # checks if consecutive
    for i in range (len(hand) - 1):
      if hand[i + 1].rank == hand[i].rank - 1:
        straight_count += 1
    if straight_count == 4:
      straight = True
          
    if (not straight):
      return 0, ''

    points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Straight'


  def is_three_kind (self, hand):
    three_kind = False
    # sees if there are three same cards in a row
    for i in range(0, len(hand)-2):
      if hand[i].rank == hand[i+2].rank:
        # places three of a kind at beginning of hand
        hand.insert(0, hand.pop(i))
        hand.insert(1, hand.pop(i+1))
        hand.insert(2, hand.pop(i+2))
        three_kind = True
          
    if (not three_kind):
      return 0, ''

    points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Three of a Kind'

      
  def is_two_pair (self, hand):
    hand.reverse()
    two_pair = False
    pair_count = 0
    pair_hand = []
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        pair_count += 1
        hand.insert(0, hand.pop(i))
        hand.insert(1, hand.pop(i+1))
    
    if pair_count == 2:
      two_pair = True
    
    if (not two_pair):
      return 0, ''

    points = 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Two Pair'

  def is_one_pair (self, hand):
    one_pair = False
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        hand.insert(0, hand.pop(i))
        hand.insert(1, hand.pop(i+1))
        one_pair = True
        break
    if (not one_pair):
      return 0, ''

    points = 2 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'One Pair'

  def is_high_card (self,hand):
      
    points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'High Card'


def main():
  # read number of players from stdin
  line = sys.stdin.readline()
  line = line.strip()
  num_players = int (line)
  if (num_players < 2) or (num_players > 6):
    return

  # create the Poker object
  game = Poker (num_players)

  # play the game
  game.play()

if __name__ == "__main__":
  main()
