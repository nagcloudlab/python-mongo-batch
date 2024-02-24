


# data structure vs iterator vs iterable

# data structure: list, tuple, set, dictionary
# iterator: __iter__ and __next__ methods ( a object who iterates data structure)
# iterable: data structure + iterator ( a object who can be iterated)

# -------------------------------------------------------------------------------------


# list is a data structure
# list is iterable
# list is not iterator


# list is a data structure

# list1 = [1, 2, 3, 4, 5]

# iterator = iter(list1)
# print(next(iterator)) # 1
# print(next(iterator)) # 2
# print(next(iterator)) # 3
# print(next(iterator)) # 4   
# print(next(iterator)) # 5
# # print(next(iterator)) # StopIteration

# # list is iterable

# for i in list1:
#     print(i)



# custom iterable


# class MyRange:
#     def __init__(self, start, end):
#         self.value = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.value >= self.end:
#             raise StopIteration
#         current = self.value
#         self.value += 1
#         return current
    

# for i in MyRange(0, 10):
#     print(i)





from random import shuffle

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    def __iter__(self):
        return iter(self.cards)
    
    def reset(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        return self

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        """
        Return a list of cards dealt
        """
        count = self.count()
        actual = min([num, count])  # make sure we don't try to over-deal

        if count == 0:
            raise ValueError("All cards have been dealt")

        if actual == 1:
            return [self.cards.pop()]

        cards = self.cards[-actual:]  # slice off the end
        self.cards = self.cards[:-actual]  # adjust cards

        return cards

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)
        return self

    def deal_card(self):
        """
        Returns a single Card
        """
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        """
        Returns a list of Cards
        """
        return self._deal(hand_size)




my_deck = Deck()
my_deck.shuffle()



for card in my_deck:
    print(card)

