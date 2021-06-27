import random
from Board import Board, Route
import turtle


class Game():
    def __init__(self, Board, Players, TrainDeck, RouteDeck):
        self.Board = Board
        self.Players = Players
        self.TrainDeck = TrainDeck
        self.RouteDeck = RouteDeck
        self.on_move = None
        self.is_end = False
        self.moves = 0

    def next_player(self):
        id = self.Players.index(self.on_move)
        return self.Players[(id + 1)%len(self.Players)]


    def choose_ticket_cards(self, cards):
        res = []
        i = 0
        for card in cards:
            print(f'{i+1}.  ', card.to_str())
            i += 1
        print('Wybierz numery kart, które chcesz zostawić (oddzielone spacją)')
        while True:
            numbers = input()
            # TODO: handle errors
            numbers = numbers.split()
            if len(numbers) <= 3:
                is_good = True
                for number in numbers:
                    if number < '1' or number > '3':
                        is_good = False
                        print('Podaj poprawne numery kart!')
                if is_good:
                    for number in numbers:
                        res.append(cards[int(number) - 1])
                    break
            else:
                print('Podaj poprawne numery kart!')
        return res

    def draw_from_pile(self):
        if not self.on_move.is_bot:
            print('Czy na pewno chcesz dobrać karty ze stosu? [y/n]' )
            d = input()
            if d == 'y' or d == 'Y':
                return self.TrainDeck.draw(2)
            else:
                return False
        else:
            return self.TrainDeck.draw(2)

    def draw_faceup(self):
        def check():
            n = 0
            for card in self.Board.faceupCards:
                if card.is_special():
                    n += 1
            return n < 3

        s = 'Wybierz karty, które chcesz dobrać lub "q" żeby wyjść'
        while True:
            print(s)
            print(self.Board.to_str_faceup())
            d = input()
            if d == 'q' or d == 'Q':
                return False
            else:
                d = d.split()
                length = len(d)
                for el in d:
                    if el < '1' or el > '5':
                        s += 'Wybierz poprawne numery kart!'
                    elif length > 2:
                        s += 'Wybierz poprawną ilość kart!'
                    elif length == 1 and not self.Board.faceupCards[int(d[0]) - 1].is_special():
                        s += 'Wybierz dwie zwykłe karty lub jedną specjalną!'
                    elif length == 2 and (self.Board.faceupCards[int(d[0]) - 1].is_special() or self.Board.faceupCards[int(d[1])-1].is_special()):
                        s += 'Wybierz dwie zwykłe karty lub jedną specjalną!'
                    else:
                        if length == 1:
                            drawed = self.TrainDeck.draw(1)
                            r = self.Board.pick_faceup([int(d[0])-1], drawed)
                            while not check():
                                print('Na planszy były 3 jokery - zmiana kart')
                                drawed = self.TrainDeck.draw(5)
                                self.Board.pick_faceup([0,1,2,3,4])
                                self.Board.add_faceup_cards(drawed)

                            return r
                        elif length == 2:
                            drawed = self.TrainDeck.draw(2)
                            r = self.Board.pick_faceup([int(d[0])-1, int(d[1])-1], drawed)
                            while not check():
                                print('Na planszy były 3 jokery - zmiana kart')
                                drawed = self.TrainDeck.draw(5)
                                self.Board.pick_faceup([0,1,2,3,4])
                                self.Board.add_faceup_cards(drawed)
                            return r

    def claim_route(self):
        s = '''
Wybierz drogę do zajęcia lub "q" żeby wyjść'''
        print(s)
        routes = self.on_move.gen_possible_Routes(self.Board)
        if len(routes) == 0:
            print('Obecnie nie możesz zbudować żadnej trasy.')
            return False
        else:
            i = 1
            for route in routes:
                print(route)
                print(f'{i}. - {route.to_str()}')
                i += 1
            
            while True:
                d = input()
                if d >= '1' and d <= str(i):
                    d = int(d) - 1
                    if routes[d].color == 'any':
                        print('Wybierz kolor którym chcesz zająć trasę')
                        poss = self.on_move.gen_possible_colors(routes[d].length)
                        print(poss)
                        j = 1
                        for color in poss:
                            print(f'{j}. - {color}')                   
                            j += 1
                        while True:
                            d2 = input()
                            if d2 >= '1' and d2 <= str(len(poss)):
                                cards = self.on_move.give_cards(routes[d].length, poss[int(d2)-1])
                                break
                            else:
                                if d2 == 'q' or d2 == 'Q':
                                    return False
                                print('Podaj poprawny kolor')
                    elif d == 'q' or d == 'Q':
                        return False
                    else:
                        cards = self.on_move.give_cards(routes[d].length, routes[d].color)
                    
                    routes[d].claim(self.on_move)
                    return cards
                # TODO: Drawing
                else:
                    print('Wybierz poprawny numer!')
        
    def build_station(self):
        s = '''
Wybierz miasto do zajęcia lub "q" żeby wyjść'''
        print(s)
        cities = self.on_move.gen_possible_Cities(self.Board)
        if len(cities) == 0:
            print('Obecnie nie możesz postawić żadnego dworca.')
            return False
        else:
            i = 1
            for city in cities:
                print(f'{i}. - {city.to_str()}')
                i += 1
            while True:
                d = input()
                if d >= '1' and d <= str(i):
                    d = int(d) - 1
                    cities[d].station = self.on_move
                    return True
                else:
                    print('Podaj poprawną liczbę!')


    def draw_tickets(self):
        return self.choose_ticket_cards(self.RouteDeck.draw(3))

    def choose_move(self):
        s = '''
Wybierz ruch:
1 - Dobierz 2 karty ze stosu
2 - Dobierz 2 karty lub jokera z planszy
3 - Zajmij trasę
4 - Postaw dworzec
5 - Dobierz 3 karty tras
        '''
        while True:
            print('on move: ', self.on_move.to_str())
            print(s)
            move = input()
            if move == '1':
                chosen = self.draw_from_pile()
                if chosen:
                    return (1, chosen)
            elif move == '2':
                chosen = self.draw_faceup()
                if chosen:
                    return (2, chosen) 
            elif move == '3':
                chosen = self.claim_route()
                if chosen:
                    return (3, chosen)
            elif move == '4':
                chosen = self.build_station()
                if chosen:
                    return (4, chosen)
            elif move == '5':
                chosen = self.draw_tickets()
                if chosen:
                    return (5, chosen)
            else:
                s += 'Podaj poprawny numer!'


    def do_move(self, move):
        n, data = move[0], move[1]
        if n == 1:
            self.on_move.add_TrainCards(data)
        elif n == 2:
           self.on_move.add_TrainCards(data)
        elif n == 3:
            self.TrainDeck.add_discarded(data)
        elif n == 5:
            self.on_move.add_TicketCards(data)

    def count_points(self, player):
        pass

    def play(self):
        self.on_move = random.choice(self.Players)
        while not self.is_end:
            for route in self.Board.Routes:
                print(route.to_str())

            for city in self.Board.Cities:
                print(city.to_str())
            if not self.on_move.is_bot:
                move = self.choose_move()
                self.do_move(move)
            else:
                print('on move: ', self.on_move.to_str())
                move = self.draw_from_pile()
                self.do_move((1, move))

            self.on_move = self.next_player()
        for player in self.Players:
            print(player.name, 'points: ', self.count_points(player))
        print('game ended')

    # Przygotowanie do rozgrywki
    def start(self):
        print('game started')
        tr = turtle.Turtle()
        wn = turtle.Screen()
        wn.setup(width=1280, height=1080, startx=640, starty=0)
        wn.bgpic('./img/board-photo.gif')

        # Tasowanie kart
        self.TrainDeck.shuffle()
        self.RouteDeck.shuffle()

        # Rozdawanie kart tras graczom
        p = self.Players[len(self.Players) - 1]
        p.add_TicketCards(self.choose_ticket_cards(self.RouteDeck.draw(2)))

        for player in self.Players:
            if player.no_tickets() == 0:
                player.add_TicketCards(self.RouteDeck.draw(2))

        # Rozdanie kart pociągów graczom
        for player in self.Players:
            player.add_TrainCards(self.TrainDeck.draw(4))

        # Wyłożenie kart na planszę
        self.Board.add_faceup_cards(self.TrainDeck.draw(5))

        # Rozpoczęcie rozgrywki
        self.play()