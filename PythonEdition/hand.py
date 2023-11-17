class Hand:
    cards : list
    totalSum : int

    def __init__(self) -> None:
        self.cards = []
        self.totalSum = 0

    def showHand(self) -> str:
        '''
        returns str with a pretty designed hand-display
        '''

        handDisplay = '\n'.join(f'{card[1]} - {card[0]} pts' for card in self.cards)
        handDisplay += f'\n total: {self.totalSum} pts'

        return handDisplay
    
    def takeCard(self, card : tuple[int, str]) -> None:
        '''
        adds a card to the hand
        '''

        self.cards.append(card)
        self.totalSum += card[0]