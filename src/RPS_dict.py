import random
from enum import IntEnum


class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


Victories = {
    GameAction.Rock: GameAction.Paper,
    GameAction.Paper: GameAction.Scissors,
    GameAction.Scissors: GameAction.Rock
}
class Game:
    def __init__(self):
        self.user_action = ""
        self.computer_action = ""
        self.game_result = None



    def assess_game(self):

        game_result = None

        if self.user_action == self.computer_action:
            print(f"User and computer picked {self.user_action.name}. Draw game!")
            game_result = GameResult.Tie

    
        elif self.user_action == GameAction.Rock:
            if self.computer_action == GameAction.Scissors:
                print("Rock smashes scissors. You won!")
                game_result = GameResult.Victory
            else:
                print("Paper covers rock. You lost!")
                game_result = GameResult.Defeat

    # You picked Paper
        elif self.user_action == GameAction.Paper:
            if self.computer_action == GameAction.Rock:
                print("Paper covers rock. You won!")
                game_result = GameResult.Victory
            else:
                print("Scissors cuts paper. You lost!")
                game_result = GameResult.Defeat

    # You picked Scissors
        elif self.user_action == GameAction.Scissors:
            if self.computer_action == GameAction.Rock:
                print("Rock smashes scissors. You lost!")
                game_result = GameResult.Defeat
            else:
                print("Scissors cuts paper. You won!")
                game_result = GameResult.Victory

        return game_result

class IncorrectOptionException(Exception):
    pass

    def get_computer_action(self):
        computer_selection = random.randint(0, len(GameAction) - 1)
        computer_action = GameAction(computer_selection)
        print(f"Computer picked {computer_action.name}.")

        return computer_action


    def get_user_action(self):
        game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
        game_choices_str = ", ".join(game_choices)
        try:
            user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
            user_action = GameAction(user_selection)
        except ValueError:
            raise IncorrectOptionException("Invalid selection. Pick a choice in range [0, 2]!")

        return user_action


    def play_another_round(self):
        another_round = input("\nAnother round? (y/n): ")
        return another_round.lower() == 'y'


    def main(self):

        while True:
            try:
                user_action = self.get_user_action()
            except ValueError:
                range_str = f"[0, {len(GameAction) - 1}]"
                print(f"Invalid selection. Pick a choice in range {range_str}!")
                continue

            computer_action = self.get_computer_action()
            assess_game(user_action, computer_action)

            if not play_another_round():
                break


if __name__ == "__main__":
    main()