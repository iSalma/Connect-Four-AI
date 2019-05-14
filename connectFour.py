import copy

def main():
    columns = 7
    rows = 6
    connect4 = 4
    again = True
    while again:
        print("Choose level of difficulty(depth) from 1 to 10 ")
        depth = int(input())

        while (depth > 10):
            print("Enter difficulty level(depth) less than 10\nEnter new number")
            depth = int(input())

        board = [['0' for c in range(columns)] for r in range(rows)]
        print("Who plays first? Enter 1 for Computer or 2 for Player")
        Turn = int(input())

        while (Turn > 2 or Turn < 1):
            print("Enter 1 for Computer or 2 for Player\nEnter new number")
            Turn = int(input())

        if Turn==1:
            computerTurn = True
        else:
            computerTurn = False

        while winner(board, columns, rows, connect4) is False and isfull(board, columns, rows) is False:
            table = {}
            alphabeta(board, not computerTurn, columns, rows, connect4, table, depth)
            movesarray = []
            moves(board, not computerTurn, columns, rows, movesarray)
            maxmove = -100000000000
            for item in movesarray:
                x = str(item)
                if x in table:
                    if table[x] > maxmove:
                        maxmove = table[x]
                        bestmove = x
                        b = item

            if computerTurn == True:
                board = b
                printboard(board, columns, rows)

            else:
                addcoin(board, computerTurn, columns, rows)

            computerTurn = not computerTurn
            if winner(board, columns, rows, connect4) is True or isfull(board, columns, rows) is True:
                print("Play again? y/n" )
                playagain = input()
                if playagain =='y':
                    again = True
                else:
                    again = False
def moves(board, computerTurn, columns, rows, movesarray):
    if computerTurn == True:
        for columnchoice in range(columns):
            state = copy.deepcopy(board)

            if board[0][columnchoice - 1] == 'C' or board[0][columnchoice - 1] == 'P':
                continue
            else:
                i = rows - 1
                while (board[i][columnchoice - 1] == 'C' or board[i][columnchoice - 1] == 'P'):
                    i = i - 1
                state[i][columnchoice - 1] = 'P'
                movesarray.append(state)
    else:
        for columnchoice in range(columns):
            state = copy.deepcopy(board)

            if board[0][columnchoice - 1] == 'C' or board[0][columnchoice - 1] == 'P':
                continue
            else:
                i = rows - 1
                while (board[i][columnchoice - 1] == 'C' or board[i][columnchoice - 1] == 'P'):
                    i = i - 1
                state[i][columnchoice - 1] = 'C'
                movesarray.append(state)
    return movesarray


def printboard(board, columns, rows):
    print(" 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n")
    for r in range(rows):
        for c in range(columns):
            print(' %s |' % board[r][c], end='')
        print("\n")
    print(" 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n")

def isfull(board, columns, rows):
    for r in range(rows):
        for c in range(columns):
            if board[r][c] == '0':
                return False
    return True


def addcoin(board, computerTurn, columns, rows):
    if computerTurn == True:
        print("In which column would computer like to insert coin?")
        columnchoice = int(input())
        while board[0][columnchoice - 1] == 'C' or board[0][columnchoice - 1] == 'P':
            print("Can't put coin there. Enter new column: ")
            columnchoice = int(input())
        i = rows - 1
        while (board[i][columnchoice - 1] == 'C' or board[i][columnchoice - 1] == 'P'):
            i = i - 1
        board[i][columnchoice - 1] = 'C'
    else:
        print("In which column would player like to insert coin?")
        columnchoice = int(input())
        while (columnchoice < 1 or columnchoice > columns):
            print("Can't put coin there. Enter new column: ")
            columnchoice = int(input())

        while board[0][columnchoice - 1] == 'C' or board[0][columnchoice - 1] == 'P':
            print("Can't put coin there. Enter new column: ")
            columnchoice = int(input())
        i = rows - 1
        while (board[i][columnchoice - 1] == 'C' or board[i][columnchoice - 1] == 'P'):
            i = i - 1
        board[i][columnchoice - 1] = 'P'



def alphabeta(board, computerTurn, columns, rows, connect4, table, depth):
    if str(board) in table:
        return table[str(board)]
    score = maxvalue(board, computerTurn, columns, rows, connect4, table, -100000000, 100000000, depth)
    return score

def maxvalue(board, computerTurn, columns, rows, connect4, table, alpha, beta, depth):
    if str(board) in table:
        return table[str(board)]
    if winner(board, columns, rows, connect4) is True and computerTurn == True:
        table[str(board)] = 10000
        return 10000
    elif winner(board, columns, rows, connect4) is True and computerTurn == False:
        table[str(board)] = -10000
        return -10000
    elif isfull(board, columns, rows) is True:
        table[str(board)] = 0
        return 0
    elif depth == 0:
        table[str(board)] = cost(board, columns, rows)
        return cost(board, columns, rows)

    score = -100000000
    movesarray = []
    moves(board, computerTurn, columns, rows, movesarray)

    for item in movesarray:
        score = max(score, minvalue(item, not computerTurn, columns, rows, connect4, table, alpha, beta, depth - 1))
        if score >= beta:
            table[str(board)] = score
            return score
    a = max(alpha, score)
    table[str(board)] = score
    return score


def minvalue(board, computerTurn, columns, rows, connect4, table, alpha, beta, depth):
    if str(board) in table:
        return table[str(board)]
    if winner(board, columns, rows, connect4) is True and computerTurn == True:
        table[str(board)] = 10000
        return 10000
    elif winner(board, columns, rows, connect4) is True and computerTurn == False:
        table[str(board)] = -10000
        return -10000
    elif isfull(board, columns, rows) is True:
        table[str(board)] = 0
        return 0
    elif depth == 0:
        table[str(board)] = cost(board, columns, rows)
        return cost(board, columns, rows)
    score = 100000000
    movesarray = []
    moves(board, computerTurn, columns, rows, movesarray)

    for item in movesarray:
        score = min(score, maxvalue(item, not computerTurn, columns, rows, connect4, table, alpha, beta, depth - 1))
        if score <= alpha:

            return score

        beta = min(beta, score)
    table[str(board)] = score
    return score


def winner(board, columns, rows, connect4):
    for r in range(rows):
        for c in range(columns):
            if c + 3 < columns:
                if board[r][c] == 'C' and board[r][c + 1] == 'C' and board[r][c + 2] == 'C' and board[r][c + 3] == 'C':

                    return True
                if board[r][c] == 'P' and board[r][c + 1] == 'P' and board[r][c + 2] == 'P' and board[r][c + 3] == 'P':

                    return True

    for r in range(rows):
        for c in range(columns):
            if r + 3 < rows:
                if board[r][c] == 'C' and board[r + 1][c] == 'C' and board[r + 2][c] == 'C' and board[r + 3][c] == 'C':

                    return True
                if board[r][c] == 'P' and board[r + 1][c] == 'P' and board[r + 2][c] == 'P' and board[r + 3][c] == 'P':

                    return True

    for r in range(rows):
        for c in range(columns):
            if r + 3 < rows and c - 3 >= 0:
                if board[r][c] == 'C' and board[r + 1][c - 1] == 'C' and board[r + 2][c - 2] == 'C' and board[r + 3][c - 3] == 'C':

                    return True
                if board[r][c] == 'P' and board[r + 1][c - 1] == 'P' and board[r + 2][c - 2] == 'P' and board[r + 3][c - 3] == 'P':

                    return True

    for r in range(rows):
        for c in range(columns):
            if c + 3 < columns and r + 3 < rows:
                if board[r][c] == 'C' and board[r + 1][c + 1] == 'C' and board[r + 2][c + 2] == 'C' and board[r + 3][c + 3] == 'C':

                    return True
                if board[r][c] == 'P' and board[r + 1][c + 1] == 'P' and board[r + 2][c + 2] == 'P' and  board[r + 3][c + 3] == 'P':

                    return True
    return False


def cost(board, columns, rows):
    num= 0
    for r in range(rows):
        for c in range(columns):
            if c + 1 < columns:
                if board[r][c] == 'C' and board[r][c + 1] == 'C':
                    num= num+ 3
                if board[r][c] == 'P' and board[r][c + 1] == 'P':
                    num= num- 3

    for r in range(rows):
        for c in range(columns):
            if r + 1 < rows:
                if board[r][c] == 'C' and board[r + 1][c] == 'C':
                    num= num+ 3
                if board[r][c] == 'P' and board[r + 1][c] == 'P':
                    num= num- 3

    for r in range(rows):
        for c in range(columns):
            if r + 1 < rows and c - 1 >= 0:
                if board[r][c] == 'C' and board[r + 1][c - 1] == 'C':
                    num= num+ 3
                if board[r][c] == 'P' and board[r + 1][c - 1] == 'P':
                    num= num- 3
    for r in range(rows):
        for c in range(columns):
            if c + 1 < columns and r + 1 < rows:

                if board[r][c] == 'C' and board[r + 1][c + 1] == 'C':
                    num= num+ 3
                if board[r][c] == 'P' and board[r + 1][c + 1] == 'P':
                    num= num- 3
    for r in range(rows):
        for c in range(columns):
            if c + 2 < columns:
                if board[r][c] == 'C' and board[r][c + 1] == 'C' and board[r][c + 2] == 'C':
                    num= num+ 10
                if board[r][c] == 'P' and board[r][c + 1] == 'P' and board[r][c + 2] == 'P':
                    num= num- 10

    for r in range(rows):
        for c in range(columns):
            if r + 2 < rows:
                if board[r][c] == 'C' and board[r + 1][c] == 'C' and board[r + 2][c] == 'C':
                    num= num+ 10
                if board[r][c] == 'P' and board[r + 1][c] == 'P' and board[r + 2][c] == 'P':
                    num= num- 10

    for r in range(rows):
        for c in range(columns):
            if r + 2 < rows and c - 2 >= 0:
                if board[r][c] == 'C' and board[r + 1][c - 1] == 'C' and board[r + 2][c - 2] == 'C':
                    num= num+ 10
                if board[r][c] == 'P' and board[r + 1][c - 1] == 'P' and board[r + 2][c - 2] == 'P':
                    num= num- 10
    for r in range(rows):
        for c in range(columns):
            if c + 2 < columns and r + 2 < rows:
                if board[r][c] == 'C' and board[r + 1][c + 1] == 'C' and board[r + 2][c + 2] == 'C':
                    num= num+ 10
                if board[r][c] == 'P' and board[r + 1][c + 1] == 'P' and board[r + 2][c + 2] == 'P':
                    num= num- 10

    return num


main()







