class Route():
    def __init__(self, city1, city2, length, locomotives, color, is_tunnel, is_claimed):
        self.city1 = city1
        self.city2 = city2
        self.length = length
        self.locomotives = locomotives
        self.color = color
        self.is_tunnel = is_tunnel
        self.is_claimed = is_claimed

    def to_str(self):
        # res = f'city1: {self.city1}, city2: {self.city2}, color: {self.color}, length: {self.length}, locomotives: {self.locomotives}, tunnel: {self.is_tunnel}, claimed?: {self.is_claimed}'
        if self.is_tunnel:
            return f'{self.city1} -> {self.city2} -- tunel'
        else:
            return f'{self.city1} -> {self.city2}'

    def claim(self, player):
        self.is_claimed = player.name


class City():
    def __init__(self, name):
        self.Routes = []
        self.name = name
        self.station = None

    # Dodaje trasę do listy tras wychodzących z tego miasta
    def add_Route(self, Route):
        self.Routes.append(Route)

    # Sprawdza czy w mieście już znajduje się stacja
    def is_occupied(self):
        return self.station != None

    def to_str(self):
        res = f'name: {self.name}, list of routes:\n'
        return res



class Board():
    def __init__(self, Cities, Routes):
        self.Cities = Cities
        self.Routes = Routes
        self.faceupCards = []

    # Zwraca string z wolymi miastami
    def to_str_freeCities(self):
        res = ''
        for city in self.Cities:
            if not city.is_occupied():
                res += f'{city.name}, '
        return res

    # Zwraca string z wolnymi drogami
    def to_str_freeRoutes(self):
        res = ''
        for route in self.Routes:
            if not route.is_claimed:
                res += f'{route.to_str()}, \n'
        return res

    # Dokłada karty na stół
    def add_faceup_cards(self, cards):
        for card in cards:
            self.faceupCards.append(card)

    # Wypisuje karty na stole
    def to_str_faceup(self):
        res = ''
        i = 1
        for card in self.faceupCards:
            res += f'{i}.  '
            res += card.to_str()
            res += '\n'
            i += 1
        return res

    # Zwraca wybrane karty z planszy i podmienia na nowe
    def pick_faceup(self, numbers, cards):
        res = []
        temp = []
        print(numbers)
        for number in numbers:
            res.append(self.faceupCards[number])
        for number in numbers:
            temp.append(self.faceupCards[number])
        for el in temp:
            self.faceupCards.remove(el)
        self.add_faceup_cards(cards)
        return res
