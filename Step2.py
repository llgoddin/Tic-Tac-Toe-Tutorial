rows = 3
cols = 3

board = [['' for _ in range(cols)] for _ in range(rows)]

user_input = input('Enter a square: ')

match user_input:
    case '1':
        print('Square 1')
    case '2':
        print('Square 2')
    case '3':
        print('Square 3')
    case '4':
        print('Square 4')
    case '5':
        print('Square 5')
    case '6':
        print('Square 6')
    case '7':
        print('Square 7')
    case '8':
        print('Square 8')
    case '9':
        print('Square 9')
    case _:
        print('Unknown Input')