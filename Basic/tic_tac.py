import pprint

board = {'T-L':'x','T-M':'x','T-R':'x',
        'M-L':'o','M-M':'o','M-R':'o',
        'L-L':'o ','L-M':'o','L-R':'o',
}

pprint.pprint(board)

def print_board(board):
    print(board['T-L'] +"|"+ board['T-M']  +"|"+ board['T-R'])
    print("-----")
    print(board['M-L'] +"|"+ board['M-M']  +"|"+ board['M-R'])
    print("-----")
    print(board['L-L'] +"|"+ board['L-M']  +"|"+ board['L-R'])

print_board(board) 