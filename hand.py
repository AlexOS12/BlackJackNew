class Hand:
    cards = []
    totalSum = 0

    def __init__(self) -> None:
        pass

    def showHand(self) -> str:
        '''
        returns str with a pretty designed hand-display
        '''

        handDisplay = '\n'.join(f'{card[1]} - {card[0]} pts' for card in self.cards)
        handDisplay += f'\n total: {self.totalSum} pts'

        return handDisplay
    
    def takeCard(self, card : tuple[int, str]) -> None:
        self.cards.append(card)
        self.totalSum += card[0]