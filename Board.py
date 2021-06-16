class Route():
    def __init__(self, City1, City2, length, locomotives, data, is_tunnel):
        self.City1 = City1
        self.City2 = City2
        self.length = length
        self.locomotives = locomotives
        self.data = data
        self.is_tunnel = is_tunnel

    # Sprawdza czy trasa jest podwójna
    def is_double(self):
        return len(self.data) > 1

    # Sprawdza czy cała trasa jest zajęta
    def is_claimed(self):
        if self.is_double():
            return self.data[0][1] and self.data[1][1]
        return self.data[0][1]

    # Zwraca string z niezajętymi częściami trasy
    def to_str(self):
        res = ''
        for el in self.data:
            if not el[1]:
                res += f'city1: {self.City1.name}, city2: {self.City2.name}, color: {el[0]}, length: {self.length}, locomotives: {self.locomotives}, tunnel: {self.is_tunnel}'
        return res



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
        for route in self.Routes:
            res += f'    {route.to_str()}\n'
        return res



class Board():
    def __init__(self, Cities, Routes, faceupCards):
        self.Cities = Cities
        self.Routes = Routes
        self.faceupCards = faceupCards

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
            if not route.is_claimed():
                res += f'{route.to_str()}, \n'
        return res