import random


class InvalidDecision(Exception):
    pass


def main():
    rock = """
            _______
        ---'   ____)
              (_____)
             (_____)
             (____)
        ---.__(___)
        """

    paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

    scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


    game_assets = [rock, paper, scissors]
    user_choice = get_choice()
    paper_rock_scissors(user_choice, game_assets)

def get_choice():
    while True:
        try:
            user_choice = int(
                input(f"Hi, Type 0 for Rock, 1 for Paper or 2 for Scissors ")
            )
            if user_choice != 0 and user_choice != 1 and user_choice != 2:
                raise InvalidDecision("Wrong Input. Choose 0, 1 or 2")
            else:
                return user_choice
        except ValueError:
            print("Value is not a integer")
        except InvalidDecision:
            print("Please enter asked value")
            pass


def paper_rock_scissors(user_choice, game_assets):
    pc_choice = random.randint(0, 2)
    if user_choice == 0 and pc_choice == 0:
        print("Your choice:")
        print(game_assets[0])
        print("Pc choice:")
        print(game_assets[pc_choice])
        print("Draw!")
    elif user_choice == 0 and pc_choice == 1:
        print("Your choice:")
        print(game_assets[0])
        print("Pc choice:")
        print(game_assets[pc_choice])
        print("PC Won!!")
    elif user_choice == 0 and pc_choice == 2:
        print("Your choice:")
        print(game_assets[0])
        print("Pc choice:")
        print(game_assets[pc_choice])
        print("PC Win!!")

    if user_choice == 1 and pc_choice == 0:
        print("Your choice:")
        print(game_assets[1])
        print("Pc choice:")
        print(game_assets[pc_choice])
        print("You Win")
    elif user_choice == 1 and pc_choice == 1:
        print("Your choice:")
        print(game_assets[1])
        print("Pc choice:")
        print(game_assets[pc_choice])
        print("Draw!!")
    elif user_choice == 1 and pc_choice == 2:
        print("Your choice:")
        print(game_assets[1])
        print("Pc choice:")
        print(game_assets[pc_choice])
        print("PC Win!!")

    if user_choice == 2 and pc_choice == 0:
        print("Your choice:")
        print(game_assets[2])
        print("Pc choice:")
        print(game_assets[pc_choice])
        print("PC Win")
    elif user_choice == 2 and pc_choice == 1:
        print("Your choice:")
        print(game_assets[2])
        print("Pc choice:")
        print(game_assets[pc_choice])
        print("PC Won")
    elif user_choice == 2 and pc_choice == 2:
        print("Your choice:")
        print(game_assets[2])
        print("Pc choice:")
        print(game_assets[pc_choice])
        print("Draw!!")




if __name__ == "__main__":
    main()
