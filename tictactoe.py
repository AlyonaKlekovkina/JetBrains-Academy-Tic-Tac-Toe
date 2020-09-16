def create_field():
    the_list = [n for n in input("Enter cells: ")]
    matrix = []
    ap = 0
    for i in range(3):
        matrix.append([])
        for j in range(3):
            if the_list[ap] == "_":
                matrix[i].append(" ")
            else:
                matrix[i].append(the_list[ap])
            ap += 1
    print("""---------\n| {} |\n| {} |\n| {} |\n---------""".format(" ".join(matrix[0]), " ".join(matrix[1]), " ".join(matrix[2])))
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
            elif (int(row) and int(column) == 1) or (int(row) and int(column) == 2) or (int(row) and int(column) == 3):
                return int(row), int(column)
        except ValueError:
            print("You should enter numbers!")
            continue


def get_row_column():
    column = coordinates[0] - 1
    row = 3 - coordinates[1]
    return row, column


the_field = create_field()
coordinates = get_coordinates()
r, c = get_row_column()
cell = the_field[r][c]
the_field[r][c] = "X"
print("""---------\n| {} |\n| {} |\n| {} |\n---------""".format(" ".join(the_field[0]), " ".join(the_field[1]), " ".join(the_field[2])))

