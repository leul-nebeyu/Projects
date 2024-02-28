from random import randint

def get_user_input(player):
    while True:
        try:
            user_input = int(input(f"Please select a position (1-9) to place an '{player}': "))
            if user_input < 1 or user_input > 9:
                raise ValueError
            break
        except ValueError:
            pass
    return user_input

# Placeholders for the grid
q = w = e = r = t = y = u = i = o = " "

# Function to show the grid
def show_grid():
    print("   |   |   ")  
    print(f" {q} | {w} | {e} ") 
    print("   |   |   ") 
    print("-----------")
    print("   |   |   ") 
    print(f" {r} | {t} | {y} ") 
    print("   |   |   ") 
    print("-----------")
    print("   |   |   ") 
    print(f" {u} | {i} | {o} ") 
    print("   |   |   ") 

# Function to update the grid
def update_grid(user_input, l):
    global q, w, e, r, t, y, u, i, o
    if user_input == 1 and q == " ":
        q = l
    elif user_input == 2 and w == " ":
        w = l
    elif user_input == 3 and e == " ":
        e = l
    elif user_input == 4 and r == " ":
        r = l
    elif user_input == 5 and t == " ":
        t = l
    elif user_input == 6 and y == " ":
        y = l
    elif user_input == 7 and u == " ":
        u = l
    elif user_input == 8 and i == " ":
        i = l
    elif user_input == 9 and o == " ":
        o = l

# Function to check if someone won
def check_win():
    if q == w == e and q != " ":
        return True, q
    elif r == t == y and r != " ":
        return True, r
    elif u == i == o and u != " ":
        return True, u
    elif q == r == u and q != " ":
        return True, q
    elif w == t == i and w != " ":
        return True, w
    elif e == y == o and e != " ":
        return True, e
    elif q == t == o and q != " ":
        return True, q
    elif e == t == u and e != " ":
        return True, e
    return False, None

# Function to check if there is a draw:
def check_draw():
    if (q == " " or w == " " or e == " " or r == " " or t == " " or y == " " or u == " " or i == " " or o == " "):
        return False
    elif check_win()[0]:
        return False
    return True

# Function to play vs computer
def vs_computer():
    used_position = []
    player1 = "X"
    player2 = "O"
    show_grid()
    while not check_win()[0]:
        user_input = get_user_input(player1)
        if user_input in used_position:
            continue
        else:
            used_position.append(user_input)
            update_grid(user_input, player1)
            if check_win()[0]:
                show_grid()
                break
            elif check_draw():
                show_grid()
                break
            while True:
                computer = randint(1, 9)
                if computer not in used_position:
                    break
            if check_win()[0]:
                show_grid()
                break
            used_position.append(computer)
            update_grid(computer, player2)
            print(f"Computer placed an 'O' in position {computer}:")
            show_grid()
    if check_win()[1] == "X":
        print("Player won!")
    elif check_win()[1] == "O":
        print("Computer won!")
    else:
        print("Tie!")

# Function to playe vs player
def vs_player():
    used_position = []
    player1 = "X"
    player2 = "O"
    show_grid()
    while not check_win()[0]:
        user_input = get_user_input(player1)
        if user_input in used_position:
            continue
        else: 
            used_position.append(user_input)
            update_grid(user_input, player1)
            if check_win()[0]:
                show_grid()
                break
            elif check_draw():
                show_grid()
                break 
            show_grid()
            while not check_win()[0]:
                user_input = get_user_input(player2)
                if user_input in used_position:
                    continue
                else: 
                    used_position.append(user_input)
                    update_grid(user_input, player2)
                    if check_win()[0]:
                        show_grid()
                        break
                    elif check_draw():
                        show_grid()
                        break
                    show_grid()
                    break
    if check_win()[1] == "X":
        print("Player1 won!")
    elif check_win()[1] == "O":
        print("Player2 won!")
    else:
        print("Tie!")

# Function to reset the grid
def reset():
    global q, w, e, r, t, y, u, i, o
    q = w = e = r = t = y = u = i = o = " "
    
# Main function 
def main():
    print("Welcome to Tic Tac Toe")
    while True:
        reset()
        user_choice = input("Choose an opponent:\n1. Computer\n2. Player\n")
        if user_choice == "1":
            vs_computer()
            answer = input("Play again? (y)es/(n)o ").lower()
            if answer in ["y", "yes"]:
                continue
            elif answer in ["n", "no"]:
                return
        elif user_choice == "2":
            vs_player()
            answer = input("Play again? (y)es/(n)o ").lower()
            if answer in ["y", "yes"]:
                continue
            elif answer in ["n", "no"]:
                return  
        else:
            continue

