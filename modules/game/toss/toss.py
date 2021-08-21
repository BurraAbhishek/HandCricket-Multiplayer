import random
# Toss: The AI has a number in its mind. You select any number from 0 to 6.
# You also select whether the sum of these two numbers is odd or even.
# If your prediction is correct, you win the toss.
# Otherwise, you lose the toss.
# Adapted from https://github.com/BurraAbhishek/Python-Hand-Cricket


def tossPlay(team1_data, team2_data):
    """ Toss for cricket matches, using the odd-or-even concept

    Arguments:
    team1_data: JSON representation of the team file of the first team
    team2_data: JSON representation of the team file of the second team

    Returns:
    A string, either "bat" or "field"

    Description:
    The player must select an integer.
    Then, the bot will select either 0 or 1.
    The player must decide if the sum of these integers is odd or even.
    If the prediction is correct, the player wins the toss.
    Then, the player can choose batting or fielding (bowling)
    If the player loses the toss, or chooses something else,
        then the bot will choose whether to bat or field first.

    """

    print("Time for the toss!")
    # NOTE: We will not enforce the 0 to 6 constraint.
    # Generally, people play in that range.
    # if team2 is not human, assign to team1
    if team1_data["isHuman"] and team2_data["isHuman"]:
        print("Team", team2_data["team_name"], ", it's your turn. ")
    try:
        numInput = int(input("Choose a number between 0 and 6 (in [0, 6]): "))
    except:
        numInput = 0
    # Now decide whether the sum is Odd or Even.
    # If something else is typed, the player loses the toss.
    # If team1 is not human, assign to team2
    if team1_data["isHuman"] and team2_data["isHuman"]:
        print("Team", team1_data["team_name"], ", it's your turn. ")
    print("Odd or Even? NOTE: Zero is counted as even. ")
    print("The sum of the second team's input and AI input is checked. ")
    print("The AI input is either 0 or 1. ")
    print("To win the toss, your prediction should be correct. ")
    turn = input("Either type 'Odd' or type 'Even': ")

    # Sum of the two input numbers = c
    c = (numInput + (random.randint(0, 1)))

    # The sum is actually even
    if c % 2 == 0:
        if turn == 'Even':
            if not team2_data["isHuman"]:
                print("You won the toss")
            else:
                print(team1_data["team_name"], "won the toss")
            toss = 1
        else:
            if not team2_data["isHuman"]:
                print("You lost the toss")
            else:
                print(team2_data["team_name"], "won the toss")
            toss = 0
    # The sum is actually odd
    else:
        if turn == 'Odd':
            if not team2_data["isHuman"]:
                print("You won the toss")
            else:
                print(team1_data["team_name"], "won the toss")
            toss = 1
        else:
            if not team2_data["isHuman"]:
                print("You lost the toss")
            else:
                print(team2_data["team_name"], "won the toss")
            toss = 0

    # team1 wins the toss
    if toss == 1:
        if team1_data["isHuman"]:
            choice = human_chooses_toss(team1_data["team_name"])
        else:
            choice = engine_chooses_toss()
    # team2 loses the toss
    elif toss == 0:
        if team2_data["isHuman"]:
            choice = reverse_toss(human_chooses_toss(team2_data["team_name"]))
        else:
            choice = engine_chooses_toss()

    # Return the choice
    return choice


def human_chooses_toss(team_name):
    """ If human player wins toss, let the human decide the toss. """

    choice = input("Choose to bat first or field first: ")
    play_start_with_possibilities = ["bat", "field"]
    # Ensure that bowling first redirects to fielding first
    if choice == "bowl":
        choice = "field"
    # Suppose the player types something else, randomly generate a decision
    if choice != "bat" and choice != "field":
        choice = random.choice(play_start_with_possibilities)
    print(team_name, "won the toss and chose to", choice, "first")
    return choice


def engine_chooses_toss():
    """ If human player loses toss, let the engine decide the toss. """
    opponent_input = random.randint(0, 1)
    if opponent_input == 0:
        choice = "bat"
        print("Your opponent won the toss and chose to field first")
    else:
        choice = "field"
        print("Your opponent won the toss and chose to bat first")
    return choice


def reverse_toss(choice):
    """ Reverse the toss """

    if choice == "bat":
        choice_new = "field"
    elif choice == "field":
        choice_new = "bat"
    else:
        choice_new = choice
    return choice_new