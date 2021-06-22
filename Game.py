class Game():
    def __init__(self, Board, Players, TrainDeck, RouteDeck):
        self.Board = Board
        self.Players = Players
        self.TrainDeck = TrainDeck
        self.RouteDeck = RouteDeck
        self.on_move = None
        self.is_end = False
        self.moves = 0

    # Rozpoczęcie rozgrywki
    def start(self):
        print('started')