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
        return self.color == 'locomotive'

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
        return f'{self.city1} -> {self.city2} -- pkt: {self.points}'



class Deck():
    def __init__(self, pile):
        self.pile = pile
        self.discarded = []

    # Zwraca kartę z góry tali (dobranie karty)
    def draw(self, n):
        # Jeżeli jest za mało kart
        if len(self.pile) < n:
            self.__restock()
        return [self.pile.pop(0) for i in range(n)]

    # Dodaje kartę do listy kart odrzuconych (wykorzystanie karty)
    def add_discarded(self, cards):
        for card in cards:
            self.discarded.append(card)

    def shuffle(self):
        res = []
        for i in range(len(self.pile)):
            c = choice(self.pile)
            res.append(c)
            self.pile.remove(c)
        self.pile = res

    def special_cards(self):
        res = []
        for card in self.pile:
            if card.is_special():
                res.append(card)
        for card in res:
            self.pile.remove(card)
        return res
    
    # Tasuje wykorzystane karty i dokłada je pod talię
    def __restock(self):
        while self.discarded:
            temp = choice(self.discarded)
            self.pile.append(temp)
            self.discarded.remove(temp)