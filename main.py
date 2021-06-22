from Game import Game
from Player import Player
from Board import Route, City, Board
from Cards import Deck, TrainCard, TicketCard
from data import GameData

# Dane gry
colors = GameData().colors
data_routes = GameData().routes
data_cities = GameData().cities
data_ticekts = GameData().tickets

def gen_cities():
    cities = [City(name) for name in data_cities]
    for city in cities:
        for route in gen_routes():
            if route.City1 == city.name or route.City2 == city.name:
                city.add_Route(route)
    return cities        

def gen_routes():
    return [Route(route['city1'], route['city2'], route['length'], route['locomotives'], route['data'], route['is_tunnel']) for route in data_routes]

def gen_board():
    return Board(gen_cities(), gen_routes())

def gen_players(n):
    # zapytac o imie gracza
    players = [Player(f'bot-{i}') for i in range(n-1)]
    name = input('Podaj nazwę gracza: ')
    players.append(Player(name))
    return players

def gen_traincards():
    # sprawdzić ilość kart !!!
    res = []
    for color in colors:
        for i in range(8):
            res.append(TrainCard(color))
    return res

def gen_ticketcards():
    return [TicketCard(ticket['city1'], ticket['city2'], ticket['points']) for ticket in data_ticekts]

def gen_traindeck():
    return Deck(gen_traincards())

def gen_ticketdeck():
    return Deck(gen_ticketcards())


def menu():
    m = '''
=======================
    Ticket to Ride
=======================
'''
    print(m)

    players_num = input()
    return int(players_num)

if __name__ == '__main__':
    players_num = menu()
    gen_players(players_num)

    new_game = Game(gen_board(), gen_players(players_num), gen_traindeck(), gen_ticketdeck())

    new_game.start()