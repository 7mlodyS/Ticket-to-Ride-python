from typing import Reversible


class Player():
    def __init__(self, name, is_bot):
        self.name = name
        self.points = 0
        self.trains = 45
        self.stations = 3
        self.__TrainCards = []
        self.__TicketCards = []
        self.is_bot = is_bot

    def add_TrainCards(self, cards):
        for card in cards:
            self.__TrainCards.append(card)

    def add_TicketCards(self, cards):
        for card in cards:
            self.__TicketCards.append(card)
    
    def no_tickets(self):
        return len(self.__TicketCards)

    def give_cards(self, n, color):
        res = []
        for card in self.__TrainCards:
            if card.color == color:
                res.append(card)
                n -= 1
            if n == 0:
                break
        for card in res:
            self.__TrainCards.remove(card)
        return res

    # Tworzy słownik z kartami pociągów gracza
    def __gen_dict_TrainCard(self):
        colors = ['white', 'black', 'red', 'blue', 'pink', 'green', 'orange', 'yellow', 'locomotive']
        d = {c : 0 for c in colors}
        for card in self.__TrainCards:
            d.update({card.color : d[card.color] + 1})
        return d

    # Generuje listę możliwych tras do zajęcia przy aktualnym stanie kart
    def gen_possible_Routes(self, Board):
        d = self.__gen_dict_TrainCard()
        res = []
        for route in Board.Routes:
            if not route.is_claimed:
                if route.locomotives > 0:
                    if d['locomotive'] >= route.locomotives:
                        if route.color == 'any':
                            for key in d:
                                if d[key] >= route.length:
                                    res.append(route)
                                    break
                        elif d[route.color] >= route.length:
                            res.append(route)
                else:
                    if route.color == 'any':
                        for key in d:
                            if d[key] >= route.length:
                                res.append(route)
                                break
                    elif d[route.color] >= route.length:
                        res.append(route)

        return res
    
    def does_have(self, n, color):
        d = self.__gen_dict_TrainCard()
        return d[color] >= n

    def gen_possible_Cities(self, Board):
        res = []
        for city in Board.Cities:
            if not city.is_occupied():
                is_reachable = False
                for route in city.Routes:
                    if route.is_claimed == self.name:
                        is_reachable = True
                        break
                if is_reachable:
                    res.append(city)
        return res

    # Generuje nazwy kolorów, których jest więcej niż n
    def gen_possible_colors(self, n):
        res = []
        d = self.__gen_dict_TrainCard()
        for key in d:
            if d[key] >= n:
                res.append(key)
        return res

    def info(self):
        res = f'Informacje o graczu\nIlość wagoników: {self.trains}\nKarty tras:\n'
        for card in self.__TicketCards:
            res += f'  {card.to_str()}\n'

        d = self.__gen_dict_TrainCard()
        for key in d:
            res += f'  {key} : {d[key]}\n'
        return res

    def to_str(self):
        return f'Gracz: {self.name}, punkty: {self.points}, wagoniki: {self.trains}, dworce: {self.stations}, karty pociągów: {len(self.__TrainCards)}, karty tras: {len(self.__TicketCards)}'