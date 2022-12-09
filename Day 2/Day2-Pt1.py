def get_input():
    db = []
    with open(r"D:\Coding\AdventofCode2022\Day 2\21.in", "r") as f:
        for line in f.readlines():
            db.append([c for c in line.strip().split()])
    return db


def game_scorer(opp_hand, my_hand, winlose=False):
    winlosehands = {"X": 0, "Y": 3, "Z": 6}
    score = 0
    winner = {
        "A": {"X": [1, 3], "Y": [2, 6], "Z": [3, 0]},
        "B": {"X": [1, 0], "Y": [2, 3], "Z": [3, 6]},
        "C": {"X": [1, 6], "Y": [2, 0], "Z": [3, 3]},
    }
    if winlose == False:
        score = winner[opp_hand][my_hand][0] + winner[opp_hand][my_hand][1]

    else:
        for value in winner[opp_hand].values():
            if value[1] == winlosehands[my_hand]:
                score += value[0] + value[1]

    return score


def calculate_all_games(pt_two=False):
    db = get_input()
    total_score = 0
    for i in db:
        total_score += game_scorer(i[0], i[1], pt_two)

    return total_score


total_score = calculate_all_games(True)
print(total_score)
