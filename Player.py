class Player():
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.trains = 45
        self.stations = 3
        self.__TrainCards = []
        self.__TicketCards = []

    def add_TrainCard(self, card):
        self.__TrainCards.append(card)

    def add_TicketCard(self, card):
        self.__TicketCards.append(card)

    # Tworzy słownik z kartami pociągów gracza
    def __gen_dict_TrainCard(self):
        colors = ['green', 'purple', 'red', 'locomotive', 'yellow']
        d = {c : 0 for c in colors}
        for card in self.__TrainCards:
            d.update({card.color : d[card.color] + 1})
        return d

    # Generuje listę możliwych tras do zajęcia przy aktualnym stanie kart
    def gen_possible_Routes(self, Board):
        d = self.__gen_dict_TrainCard()
        res = []
        for route in Board.Routes:
            if route.is_double():
                for el in route.data:
                    if not el[1] and d[el[0]] >= route.length and d['locomotive'] >= route.locomotives:
                        res.append(route)
            else:
                if not route.data[0][1] and d[route.data[0][0]] >= route.length and d['locomotive'] >= route.locomotives:
                        res.append(route)
        return res
        
    def to_str(self):
        return f'Gracz: {self.name}, punkty: {self.points}, wagoniki: {self.trains}, dworce: {self.stations}, karty pociągów: {len(self.__TrainCards)}, karty tras: {len(self.__TicketCards)}'