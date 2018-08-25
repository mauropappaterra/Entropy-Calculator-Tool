# Entropy Calculator Tool
# controller.py
# Created by Mauro J. Pappaterra on 25 of August 2018.
import time

#MAIN PROGRAM METHOD / START SCREEN
def start(m,v):

    exit = False
    while (not exit):
        print (v.welcome)
        exit = main_menu(m,v)

    print(v.exit)

# MAIN MENU
def main_menu (m,v):
    print(v.menu)
    read = input().lower()

    while (read != 'c' and read != 's' and read != 'a' and read != 'q'):
        print(v.error_input)
        read = input().lower()

    if (read == 'c'):
        entropy(m, v)

    if (read == 'a'):
        settings(m, v)

    if (read == 'a'):
        about(m, v)

    if (read == 'q'):
        return True  # quit

# GENERATE NUMBER MENU
def entropy (m,v):
    print("entropy menu")

    print(v.size)
    size = ask_int(m,v,0,999999)

    print(v.choose)
    choose = ask_int(m,v,0, 999999)

    entropy = m.getEntropy (size, choose)

    time.sleep(1)

    print(v.explosion)

    print (v.print_entropy(size, choose, entropy))

    ten = m.estimateLength(10, entropy)
    twenty_six = m.estimateLength(26, entropy)
    fifty_two = m.estimateLength(52, entropy)
    sixty_two = m.estimateLength(62, entropy)

    time.sleep(1)

    v.compare(ten, twenty_six, fifty_two, sixty_two)

    print (v.entropy_menu)

    read = input().lower()

    while (read != 'c' and read != 'b' and read != 'q'):
        print(v.error_start)
        read = input().lower()

    if (read == 'c'):
        entropy(m, v)

    if (read == 'b'):
        main_menu(m, v)

    if (read == 'q'):
        return True  # quit


# SETTINGS MENU
def settings(m, v):
    print(v.settings)

# ABOUT MENU
def about (m,v):
    print(v.about)

    read = input().lower()
    while (read != 'b' and read != 'q'):
        print(v.error_input)
        read = input().lower()

    if (read == 'b'):
        return main_menu(m, v)  # main menu
    elif (read == 'q'):
        return True  # quit


# Ask user for integer in between a determined range (as method)
def ask_int (m, v, min, max):
    number = input()

    while (not (number.lstrip("-").isdigit()) or not (min <= int(number) <= max)):
        print(v.error_size(min, max))
        number = input()

    return int(number)