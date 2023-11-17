import random

suits = "♥♦♣♠"

stdCardsSet = {
    1 : 'A',     
    6 : '6',
    7 : '7',
    8 : '8',
    9 : '9',
    10 : '10',
    11 : 'J',
    12 : 'Q',
    13 : 'K',
}

extCardsSet = {
    1 : 'A',
    2 : '2',
    3 : '3',
    4 : '4',
    5 : '5',     
    6 : '6',
    7 : '7',
    8 : '8',
    9 : '9',
    10 : '10',
    11 : 'J',
    12 : 'Q',
    13 : 'K',
}

class Dek:
    block = []
    refDek : dict

    def __init__(self, size : int = 1) -> None:
        '''
            size:
            1 - 36 cards
            2 - 52 cards
        '''

        if size not in (1, 2):
            size = 1

        refDek = (stdCardsSet, extCardsSet)[size - 1]

        for suit in suits:
            for card in refDek:
                self.block.append((card, suit + refDek[card]))

        pass

    def shuffle(self):
        '''
        shuffles the dek
        '''
        random.shuffle(self.block)

    def pullCard(self) -> (int, str):
        '''
        works like a pop function in stack.
        If there is no cards in block - returns (0, '')
        Otherwise return (pts, cardSuit + cardVal)
        '''
        if len(self.block):
            card = self.block[0]
            del self.block[0]
            return card
        return (0, '')
