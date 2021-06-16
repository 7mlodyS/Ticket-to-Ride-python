class Route():
    def __init__(self, length, locomotives, data, is_tunnel):
        self.lenght = length
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
                res += f'color: {el[0]}, length: {self.lenght}'
        return res

class City():
    def __init__(self, Routes, name):
        self.Routes = Routes
        self.name = name
        self.station = None

    # Sprawdza czy w mieście już znajduje się stacja
    def is_occupied(self):
        return self.Station != None

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
                res += f'{route.to_str()}, '