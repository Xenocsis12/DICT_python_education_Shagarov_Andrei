"""tictactoe"""


def print_field(field):
    """
    prints game field
    :param field: 9 symbols string
    :return: none
    """
    print("_"*9)
    for i in range(3):
        print("|", end=" ")
        print(" ".join(field[i*3:i*3+3:]), end=" ")
        print("|")
    print("—" * 9)

def victory_check(field,player,moves):
    """
    checking if the game must be over

    :param str field: current game field
    :param str player: the name of player, must be "o" or "x"
    :param int moves:
    :return: Bool: Returns True if there is winner or it's a draw
    """
    for i in range(3):
        if field[i*3:i*3+3:] == player*3:
            print(f"player {player} won")
            return True
        elif field[i::3] == player*3:
            print(f"player {player} won")
            return True
        elif field[0::4] == player*3:
            print(f"player {player} won")
            return True
        elif field[2:7:2] == player*3:
            print(f"player {player} won")
            return True
        elif moves == 9:
            print("It's a draw!")
            return True
    return False

def make_move(field,player):
    """
    function for making moves on the game board

    :param str field: current game field
    :param player: the name of player, must be "o" or "x"
    :return str: current game board with player`s move
    """
    while True:
        try:
            a = input(f"It's turn for {player} player>")
            a = "".join(a.split())

            if not a[0].isdigit() or len(a) != 2 or not a[1].isdigit():
                print("Invalid input. Please enter two digits.")
                continue
            if not (1 <= int(a[0]) <= 3 and 1 <= int(a[1]) <= 3):
                print("Invalid input. Row and column values must be between 1 and 3.")
                continue
            index = (int(a[0]) - 1) * 3 + (int(a[1]) - 1)
            if field[index] == "_":
                new_field = field[0:index:] + field[index].replace("_",player) + field[index+1:]
                return new_field
            else:
                print("the cell is already taken")
        except ValueError:
            print("Error: wrong value ")


game_field = "_________"
moves = 0
print_field(game_field)
while True:
    game_field = make_move(game_field,"x")
    moves += 1
    print_field(game_field)
    if victory_check(game_field,"x",moves):
        break
    game_field = make_move(game_field,"o")
    print_field(game_field)
    moves += 1
    if victory_check(game_field,"o",moves):
        break
