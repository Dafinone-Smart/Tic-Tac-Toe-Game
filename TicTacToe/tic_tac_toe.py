currentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def playingBoard(field):
    for row in range(5):
        if row % 2 == 0:
            practicalRow = row / 2
            newPracticalRow = int(practicalRow)
            for column in range(5):
                if column % 2 == 0:
                    practicalColumn = column / 2
                    newPracticalColumn = int(practicalColumn)
                    if column != 4:
                        print(field[newPracticalColumn]
                              [newPracticalRow], end="")
                    else:
                        print(field[newPracticalColumn][newPracticalRow])
                else:
                    print("|", end="")
        else:
            print("-" * 5)


checkList = [" ", " ", " "]


def checkPlayerWin():
    Player = 1
    column = -1
    for rows in range(3):
        row = rows
        column += 1
        checkList[row] = currentField[column][row]
        if checkList == ["X", "X", "X"]:
            print(f"Player {Player} has won!")
            return True
        elif checkList == ["O", "O", "O"]:
            Player += 1
            print(f"Player {Player} has won!")
            return True
        else:
            pass
    column = -1
    for rows in range(2, -1, -1):
        row = rows
        column += 1
        checkList[row] = currentField[column][row]
        if checkList == ["X", "X", "X"]:
            print(f"Player {Player} has won!")
            return True
        elif checkList == ["O", "O", "O"]:
            Player += 1
            print(f"Player {Player} has won!")
            return True
        else:
            pass
    for rows in range(3):
        row = rows
        column = 0
        checkList[row] = currentField[column][row]
        if checkList == ["X", "X", "X"]:
            print(f"Player {Player} has won!")
            return True
        elif checkList == ["O", "O", "O"]:
            Player += 1
            print(f"Player {Player} has won!")
            return True
        else:
            pass
    for rows in range(3):
        row = rows
        column = 1
        checkList[row] = currentField[column][row]
        if checkList == ["X", "X", "X"]:
            print(f"Player {Player} has won!")
            return True
        elif checkList == ["O", "O", "O"]:
            Player += 1
            print(f"Player {Player} has won!")
            return True
        else:
            pass
    for rows in range(3):
        row = rows
        column = 2
        checkList[row] = currentField[column][row]
        if checkList == ["X", "X", "X"]:
            print(f"Player {Player} has won!")
            return True
        elif checkList == ["O", "O", "O"]:
            Player += 1
            print(f"Player {Player} has won!")
            return True
        else:
            pass
    for columns in range(3):
        column = columns
        row = 0
        checkList[column] = currentField[column][row]
        if checkList == ["X", "X", "X"]:
            print(f"Player {Player} has won!")
            return True
        elif checkList == ["O", "O", "O"]:
            Player += 1
            print(f"Player {Player} has won!")
            return True
        else:
            pass
    for columns in range(3):
        column = columns
        row = 1
        checkList[column] = currentField[column][row]
        if checkList == ["X", "X", "X"]:
            print(f"Player {Player} has won!")
            return True
        elif checkList == ["O", "O", "O"]:
            Player += 1
            print(f"Player {Player} has won!")
            return True
        else:
            pass
    for columns in range(3):
        column = columns
        row = 2
        checkList[column] = currentField[column][row]
        if checkList == ["X", "X", "X"]:
            print(f"Player {Player} has won!")
            return True
        elif checkList == ["O", "O", "O"]:
            Player += 1
            print(f"Player {Player} has won!")
            return True
        else:
            pass


Player = 1


while (True):
    print("Players turn: ", Player)
    moveRow = int(input(f"Player {Player}: please select row: "))
    moveColumn = int(input(f"Player {Player}: please select column: "))
    if Player == 1:
        if currentField[moveColumn][moveRow] == " ":
            currentField[moveColumn][moveRow] = "X"
            if checkPlayerWin() is True:
                playingBoard(currentField)
                exit()
            else:
                pass
            Player = 2
    else:
        if currentField[moveColumn][moveRow] == " ":
            currentField[moveColumn][moveRow] = "O"
            if checkPlayerWin() is True:
                playingBoard(currentField)
                exit()
            else:
                pass
            Player = 1
    print(currentField)
    playingBoard(currentField)
