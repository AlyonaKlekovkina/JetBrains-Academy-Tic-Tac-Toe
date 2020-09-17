def create_field():
    matrix = []
    for i in range(3):
        matrix.append([])
        for j in range(3):
            matrix[i].append(" ")
    return matrix


def get_coordinates():
    while True:
        row_column = input("Enter the coordinates: ")
        try:
            row, column = row_column.split()
            if (int(row) > 3) or (int(column) > 3):
                print("Coordinates should be from 1 to 3!")
            elif the_field[3 - int(column)][int(row) - 1] == "X" or the_field[3 - int(column)][int(row) - 1] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                return int(row), int(column)
        except ValueError:
            print("You should enter numbers!")
            continue


def get_row_column():
    column = coordinates[0] - 1
    row = 3 - coordinates[1]
    return row, column


def x_or_o():
    global variable
    if variable == 'O':
        variable = 'X'
        return 'X'
    else:
        variable = 'O'
        return 'O'


def check_combination_x():
    if the_field[0][0] == 'X' and the_field[0][1] == 'X' and the_field[0][2] == 'X':
        return "X wins"
    if the_field[1][0] == 'X' and the_field[1][1] == 'X' and the_field[1][2] == 'X':
        return "X wins"
    if the_field[2][0] == 'X' and the_field[2][1] == 'X' and the_field[2][2] == 'X':
        return "X wins"
    if the_field[0][0] == 'X' and the_field[1][0] == 'X' and the_field[2][0] == 'X':
        return "X wins"
    if the_field[0][1] == 'X' and the_field[1][1] == 'X' and the_field[2][1] == 'X':
        return "X wins"
    if the_field[0][2] == 'X' and the_field[1][2] == 'X' and the_field[2][2] == 'X':
        return "X wins"
    if the_field[0][0] == 'X' and the_field[1][1] == 'X' and the_field[2][2] == 'X':
        return "X wins"
    if the_field[0][2] == 'X' and the_field[1][1] == 'X' and the_field[2][0] == 'X':
        return "X wins"
    else:
        return False


def check_combination_o():
    if the_field[0][0] == 'O' and the_field[0][1] == 'O' and the_field[0][2] == 'O':
        return "O wins"
    if the_field[1][0] == 'O' and the_field[1][1] == 'O' and the_field[1][2] == 'O':
        return "O wins"
    if the_field[2][0] == 'O' and the_field[2][1] == 'O' and the_field[2][2] == 'O':
        return "O wins"
    if the_field[0][0] == 'O' and the_field[1][0] == 'O' and the_field[2][0] == 'O':
        return "O wins"
    if the_field[0][1] == 'O' and the_field[1][1] == 'O' and the_field[2][1] == 'O':
        return "O wins"
    if the_field[0][2] == 'O' and the_field[1][2] == 'O' and the_field[2][2] == 'O':
        return "O wins"
    if the_field[0][0] == 'O' and the_field[1][1] == 'O' and the_field[2][2] == 'O':
        return "O wins"
    if the_field[0][2] == 'O' and the_field[1][1] == 'O' and the_field[2][0] == 'O':
        return "O wins"
    else:
        return False


def draw():
    board = []
    for i in the_field:
        for j in i:
            if j == 'O' or j == "X":
                board.append(j)
    if len(board) == 9:
        print("Draw")
        return True


the_field = create_field()
variable = 'O'
while True:
    coordinates = get_coordinates()
    r, c = get_row_column()
    to_insert = x_or_o()
    the_field[r][c] = to_insert
    print("""---------\n| {} |\n| {} |\n| {} |\n---------""".format(" ".join(the_field[0]), " ".join(the_field[1]), " ".join(the_field[2])))
    if check_combination_x():
        print(check_combination_x())
        break
    elif check_combination_o():
        print(check_combination_o())
        break
    elif draw():
        break
