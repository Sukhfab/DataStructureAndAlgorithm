import random
# board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def print_board():
    for x in range(3):
        print('| ' + ' | '.join(board[x*3: (x+1)*3]) + ' |')

# print_board()
def print_number():
    array = []
    index = 0
    for x in board:
        array.append(str(index))
        index = index+1
    for y in range(3):
        print('| '+' | '.join(array[y*3:(y+1)*3]) + ' |')


def available_moves():
    availableMove = []
    index = 0
    for x in board:
        if x == ' ':
            availableMove.append(index)
        index = index +1
    return availableMove

# print(available_moves())

def is_won(player, index):
    #check row, column and diagonal
    row_ind = index//3
    row = board[row_ind *3: (row_ind+1) *3]
    if all(spot == player for spot in row):
        return True

    #check Column
    col_ind = index%3
    col = [board[col_ind + x * 3] for x in range(3)]
    if all(spot == player for spot in col):
        return True

    #check diagonal 0,4,8 or 2,4,6    so 0,2,4,6,8

    if index %2 ==0:
        d_one = [board[x] for x in [0,4,8]]
        if all(spot == player for spot in d_one):
            return True
        d_two = [board[x] for x in [2, 4, 6]]
        if all(spot == player for spot in d_two):
            return True

# Game starts here

exit = False
while exit != True:
    won = False
    tie = False
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    user_value = int(input("1 to play and 0 to exit: "))
    if user_value == 0:
        exit = True
    if user_value ==1:
        print_number()
        print("")
        while won != True and tie != True:
            print_board()
            user_input = int(input("Enter your Value: "))
            if user_input not in range(0,9):
                print("Invalid input! Enter between 0-8")
                continue
            if user_input in range(0,9) and user_input not in available_moves():
                print("It is already used. Check your input.")
                continue
            board[user_input] = 'X'
            if is_won('X', user_input):
                print_board()
                print(f"x won")
                won = True

            if len(available_moves()) > 0:
                computer_input = random.choice(available_moves())
                        # if computer_input not in range(1, 9):
                        #     print("Invalid input! Enter between 0-8")
                        # if computer_input not in available_moves():
                        #     print("It is already used. Check your input.")

                board[computer_input] = 'o'
                if is_won('o', computer_input):
                    print_board()
                    print(f"o won")
                    won = True

            if len(available_moves()) < 1 and won == False:
                print("Tie")
                tie = True

