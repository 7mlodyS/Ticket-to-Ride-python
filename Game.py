import random

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
        numbers = input()

        for number in numbers.split():
           res.append(cards[int(number) - 1])
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
                    elif length == 2 and (self.Board.faceupCards[int(d[0]) - 1].is_special() or self.Board.faceupCards[int(d[1])].is_special()):
                        s += 'Wybierz dwie zwykłe karty lub jedną specjalną!'
                    else:
                        if length == 1:
                            drawed = self.TrainDeck.draw(1)
                            return self.Board.pick_faceup([d[0]], drawed)
                        elif length == 2:
                            drawed = self.TrainDeck.draw(2)
                            return self.Board.pick_faceup([d[0], d[1]], drawed)

    def claim_route():
        return False

    def build_station():
        return False

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
            pass
        elif n == 4:
            pass
        elif n == 5:
            self.on_move.add_TicketCards(data)

    def play(self):
        self.on_move = random.choice(self.Players)
        while not self.is_end:
            if not self.on_move.is_bot:
                move = self.choose_move()
                self.do_move(move)
            else:
                print('on move: ', self.on_move.to_str())
                move = self.draw_from_pile()
                self.do_move((1, move))

            self.on_move = self.next_player()
        print('game ended')

    # Przygotowanie do rozgrywki
    def start(self):
        print('started')

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
        # TODO: 3 jokery
        self.Board.add_faceup_cards(self.TrainDeck.draw(5))

        # Wylosowanie gracza zaczynającego
        num = random.randint(0, len(self.Players) - 1)

        # # Testowe wypisanie danych
        # for p in self.Players:
        #     print(p.to_str())

        # Rozpoczęcie rozgrywki
        self.play()