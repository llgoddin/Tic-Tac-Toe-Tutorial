
def get_input():
    while True:
        user_input = input('Enter a square: ')

        match user_input:
            case '1':
                return (0, 0)
            case '2':
                return (0, 1)
            case '3':
                return (0, 2)
            case '4':
                return (1, 0)
            case '5':
                return (1, 1)
            case '6':
                return (1, 2)
            case '7':
                return (2, 0)
            case '8':
                return (2, 1)
            case '9':
                return (2, 2)
            case 'x':
                return None
            case _:
                print('Unknown Input') 

def place_symbol(board, coords, symbol):
    if board[coords[0]][coords[1]] == '':
        board[coords[0]][coords[1]] = symbol

        # Make symbol switch each time a turn is taken
        if symbol == 'X':
            symbol = 'O'
        else:
            symbol = 'X'
            
    else:
        print("That square is already taken!")

def print_board(board):
    for line in board:
        for square in line:
            print(f' {square} |', end='')

        print('\n' + '-' * 12)

def menu():
    while True:
        print('Welcome To Tic-Tac-Toe!')
        print('Enter a number to choose a game type.')
        print('1 - Single Player Game')
        print('2 - Two Player Game')
        user_input = input('Game Type: ')

        if user_input == '1':
            print('Starting Single Player Game...')
            return 1
        elif user_input == '2':
            print('Starting Two Player Game...')
            return 2
        else:
            print('Invalid Input!')

rows = 3
cols = 3

board = [['' for _ in range(cols)] for _ in range(rows)]

symbol = 'X'
running = True
in_menu = True
game_type = 0

while running:

    if in_menu:
        game_type = menu()
        in_menu = False

    print_board(board)
    coords = get_input()

    if coords == None:
        running = False
    else:
        place_symbol(board, coords, symbol)
        
        