from abc import ABC, abstractmethod
from random import choice

class Card(ABC):
    @abstractmethod
    def is_special():
        pass

    @abstractmethod
    def to_str():
        pass

class TrainCard(Card):
    def __init__(self, color):
        self.color = color

    def is_special(self):
        return self.color == 'joker'

    def to_str(self):
        return self.color

class TicketCard(Card):
    def __init__(self, city1, city2, points):
        self.city1 = city1
        self.city2 = city2
        self.points = points

    def is_special(self):
        return self.points > 13

    def to_str(self):
        return f'From: {self.city1} To: {self.city2} - points: {self.points}'

class Deck():
    def __init__(self, pile):
        self.pile = pile
        self.discarded = []

    def draw(self):
        return self.pile.pop(0)

    def add_discarded(self, card):
        self.discarded = card
    
    def __restock(self):
        while self.discarded:
            temp = choice(self.discarded)
            self.pile.append(temp)
            self.pile.remove(temp)