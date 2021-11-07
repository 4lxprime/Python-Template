from pystyle import Colors, Colorate, Center
from art import text2art
import os
# LOGO

# IMPORT MODULES

creator = Center.XCenter("""
╔═════════════════════════════════╗ 
|   <== CREATED BY 4LXPRIME ==>   | 
╚═════════════════════════════════╝ 
""")
#  DEFINE CREATOR

tables = Center.XCenter("""
╔════════════════╗ 
|   1) text 1    |
╠════════════════╣ 
|   2) text 2    |
╠════════════════╣ 
|   3) text 3    |
╚════════════════╝ 
""")

# DEFINE TABLE


def intro():
    logo = Center.XCenter(text2art("NAME", "random"))
    # "NAME" IS THE TITLE OF THE TOOL AND "random" IS THE POLICE
    print(Colorate.Horizontal(Colors.yellow_to_red, logo, 1))
    print(" ")
    print(Colorate.Horizontal(Colors.yellow_to_red, creator, 1))
    print(" ")
    print(" ")

# CODE

    # DEFINE MAIN


def main():
    os.system("cls")  # CLEAN SCREEN
    intro()  # PRINT LOGO
    print(Colorate.Horizontal(Colors.yellow_to_red, tables))  # PRINT TABLES
    cmd = input("-> ")
    if cmd == "1":  # GO TO ONE
        one()
    elif cmd == "2":  # GO TO TWO
        two()
    elif cmd == "3":  # GO TO THREE
        three()


def one():  # DEFINE ONE
    input(Colorate.Horizontal(Colors.yellow_to_red, "Choice one"))
    main()


def two():  # DEFINE TWO
    input(Colorate.Horizontal(Colors.yellow_to_red, "Choice two"))
    main()


def three():  # DEFINE THREE
    input(Colorate.Horizontal(Colors.yellow_to_red, "Choice three"))
    main()


while True:
    main()
