# write your code here
the_list = [n for n in input("Enter cells: ")]
line_1 = the_list[0] + " " + the_list[1] + " " + the_list[2]
line_2 = the_list[3] + " " + the_list[4] + " " + the_list[5]
line_3 = the_list[6] + " " + the_list[7] + " " + the_list[8]
print("""---------
| {} |
| {} |
| {} |
---------""".format(line_1, line_2, line_3))

list_of_x = []
list_of_o = []
for i in the_list:
    if i == 'X':
        list_of_x.append(i)
    if i == 'O':
        list_of_o.append(i)
num_of_x = len(list_of_x)
num_of_o = len(list_of_o)
difference = abs(len(list_of_o) - len(list_of_x))


def check_combination_x():
    if the_list[0] == 'X' and the_list[1] == 'X' and the_list[2] == 'X':
        return "X wins"
    if the_list[3] == 'X' and the_list[4] == 'X' and the_list[5] == 'X':
        return "X wins"
    if the_list[6] == 'X' and the_list[7] == 'X' and the_list[8] == 'X':
        return "X wins"
    if the_list[0] == 'X' and the_list[3] == 'X' and the_list[6] == 'X':
        return "X wins"
    if the_list[1] == 'X' and the_list[4] == 'X' and the_list[7] == 'X':
        return "X wins"
    if the_list[2] == 'X' and the_list[5] == 'X' and the_list[8] == 'X':
        return "X wins"
    if the_list[0] == 'X' and the_list[4] == 'X' and the_list[8] == 'X':
        return "X wins"
    if the_list[2] == 'X' and the_list[4] == 'X' and the_list[6] == 'X':
        return "X wins"
    else:
        return False


def check_combination_o():
    if the_list[0] == 'O' and the_list[1] == 'O' and the_list[2] == 'O':
        return "O wins"
    if the_list[3] == 'O' and the_list[4] == 'O' and the_list[5] == 'O':
        return "O wins"
    if the_list[6] == 'O' and the_list[7] == 'O' and the_list[8] == 'O':
        return "O wins"
    if the_list[0] == 'O' and the_list[3] == 'O' and the_list[6] == 'O':
        return "O wins"
    if the_list[1] == 'O' and the_list[4] == 'O' and the_list[7] == 'O':
        return "O wins"
    if the_list[2] == 'O' and the_list[5] == 'O' and the_list[8] == 'O':
        return "O wins"
    if the_list[0] == 'O' and the_list[4] == 'O' and the_list[8] == 'O':
        return "O wins"
    if the_list[2] == 'O' and the_list[4] == 'O' and the_list[6] == 'O':
        return "O wins"
    else:
        return False


if difference == 0 or difference == 1:
    check_combination_x()
    check_combination_o()
    if check_combination_o() and check_combination_x():
        print("Impossible")
    elif (num_of_o <= 3 and num_of_x <= 3) and (check_combination_o() is False and check_combination_x() is False):
        print("Game not finished")
    elif check_combination_o():
        print(check_combination_o())
    elif check_combination_x():
        print(check_combination_x())
    else:
        print("Draw")
if difference >= 2:
    print("Impossible")
