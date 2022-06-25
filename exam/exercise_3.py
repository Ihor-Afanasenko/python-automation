from typing import Union

"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message
of congratulations to the winner, and ask if the players want to start a new game)
Remember the rules:
    • Rock beats scissors
    • Scissors beats paper
    • Paper beats rock
"""


class Player:
    def __init__(
            self,
            name: str,
            choice: str
    ) -> None:
        self.__name = name
        self.__choice = choice

    """
        Describe player
    """

    @property
    def name(self) -> str:
        return self.__name

    @property
    def choice(self) -> str:
        return self.__choice


def create_player() -> Player:
    current_name = str(input('Hi, player. Firstly, please input your name: '))
    current_choice = input_choice(current_name)
    while current_choice not in ['Rock', 'Paper', 'Scissors']:
        print('Your input data is incorrect. Please try again.')
        current_choice = input_choice(current_name)

    print(f'{current_choice} - good choice, {current_name}')
    return Player(current_name, current_choice)


def input_choice(name: str) -> str:
    return str(input(f'{name}, choose your variant (Rock, Paper or Scissors) '))


def get_winner_by_choice(choice_first: str, choice_second: str) -> Union[str, int]:
    if choice_first == 'Rock' and choice_second == 'Scissors' \
            or choice_first == 'Paper' and choice_second == 'Rock' \
            or choice_first == 'Scissors' and choice_second == 'Paper':
        return 1
    elif choice_first == 'Scissors' and choice_second == 'Rock' \
            or choice_first == 'Rock' and choice_second == 'Paper' \
            or choice_first == 'Paper' and choice_second == 'Scissors':
        return 2
    else:
        return 'Draw'


def find_winner(players_list: list[Player]):
    if get_winner_by_choice(players_list[0].choice, players_list[1].choice) == 'Draw':
        print('Draw. Your choices are the same. Try next time.')
    else:
        print(
            f'Congratulates, win player -'
            f' {players_list[get_winner_by_choice(players_list[0].choice, players_list[1].choice) - 1].name}')


def check_continue_answer(answer: str):
    if answer == 'Yes':
        run_game()
    elif answer == 'No':
        print('Bye')
    else:
        print('Your choice is incorrect. Try again.')
        ask_continue()


def ask_continue():
    check_continue_answer(str(input('Do your want play again (Yes/No)? ')))


def run_game():
    player_1 = create_player()
    player_2 = create_player()
    find_winner([player_1, player_2])
    ask_continue()


if __name__ == "__main__":
    run_game()
