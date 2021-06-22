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

    # Sprawdza czy karta jest specjalna (joker)
    def is_special(self):
        return self.color == 'joker'

    def to_str(self):
        return self.color



class TicketCard(Card):
    def __init__(self, city1, city2, points):
        self.city1 = city1
        self.city2 = city2
        self.points = points

    # Sprawdza czy karta jest specjalna (długa trasa)
    def is_special(self):
        return self.points > 13

    def to_str(self):
        return f'From: {self.city1} To: {self.city2} - points: {self.points}'



class Deck():
    def __init__(self, pile):
        self.pile = pile
        self.discarded = []

    # Zwraca kartę z góry tali (dobranie karty)
    def draw(self, n):
        return [self.pile.pop(0) for i in range(n)]

    # Dodaje kartę do listy kart odrzuconych (wykorzystanie karty)
    def add_discarded(self, card):
        self.discarded = card
    
    # Tasuje wykorzystane kart i dokłada je pod talię
    def __restock(self):
        while self.discarded:
            temp = choice(self.discarded)
            self.pile.append(temp)
            self.discarded.remove(temp)