import cards
import hand


def Game(dek: cards.Dek, players: dict[int, hand.Hand]) -> None:
    stopList = []
    gameEnded = False
    while len(dek.block) and len(stopList) < len(players) and not(gameEnded):
        for i in players:
            if i in stopList:
                continue
            ans = input(
                f'\nИгрок {i + 1}, нажмите "Enter", чтобы взять карту или введите 0, если не хотите брать карту ')
            if ans == '0':
                stopList.append(i)
                continue
            card = dek.pullCard()
            players[i].takeCard(card)
            print(f'Игрок {i + 1} берёт карту {card[1]}')

        print("\nТекущий счёт:")

        for i in players:
            if i in stopList:
                continue
            print(f'Игрок {i + 1} имеет руку: {players[i].showHand()}\n')
            if players[i].totalSum > 21:
                print(f'Игрок {i + 1} проиграл(\n')
                stopList.append(i)
            elif players[i].totalSum == 21:
                print(f'Игрок {i + 1} выиграл!\n')
                # print(f'Игра окончена!\n Очки всех игроков:')
                # for player in players.items():
                #     print(f'Игрок {player[0] + 1} - {player[1].totalSum}')
                gameEnded = True
    else:
        gameEnded = True
        # print("Итоговый счёт:")
        # for playerId in players:
        #     print(f'Игрок {playerId + 1} - {players[playerId].totalSum}')

    if gameEnded:
        print("Таблица лидеров:")
        leaderBoard = sorted(players.items(), key=lambda x: abs(21 - x[1].totalSum))
        leaderBoard = sorted(players.items(), key=lambda x: x[1].totalSum <= 21, reverse=True)
        for i in range(len(leaderBoard)):
            print(f'{i + 1} : Игрок {leaderBoard[i][0] + 1} - {leaderBoard[i][1].totalSum}')
    
    pass


if __name__ == '__main__':
    dek = cards.Dek()
    dek.shuffle()

    nPlayers = int(input("Укажите кол-вол игроков: "))
    players = {i: hand.Hand() for i in range(nPlayers)}

    while True:
        print('Игра начата!')
        Game(dek, players)
        ans = input("Начать новую игру? [y/n] ")
        if ans != 'y':
            exit()
