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

    def play(self):
        while not self.is_end:
            pass
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

        # Testowe wypisanie danych
        for p in self.Players:
            print(p.to_str())

        # Rozpoczęcie rozgrywki
        self.play()