import cards
import hand

def Game(dek : cards.Dek, players : list[hand.Hand]) -> None:
    while len(dek.block):
        for i in range(len(players)):
            input(f'\nИгрок {i + 1}, нажмите "Enter", чтобы взять карту')
            card = dek.pullCard()
            print(f'Игрок {i + 1} берёт карту {card[1]}')
        
        print("\nТекущий счёт:")

        for i in range(len(players)):
            print(f'Игрок {i + 1} имеет руку: {players[i].showHand()}')
            if players[i].totalSum > 21:
                print(f'Игрок {i + 1} проиграл(')
            elif players[i].totalSum == 21:
                print(f'Игрок {i + 1} выиграл!')
                print(f'Игра окончена!\n Очки всех игроков:')
                print(''.join(player.totalSum for player in players))
                pass

    pass

if __name__ == '__main__':
    dek = cards.Dek()
    dek.shuffle()

    nPlayers = int(input("Укажите кол-вол игроков: "))
    players = [hand.Hand() for i in range(nPlayers)]

    while True:
        print('Игра начата!')
        Game(dek, players)
        ans = input("Начать новую игру? [y/n] ")
        if ans != 'y':
            exit()
