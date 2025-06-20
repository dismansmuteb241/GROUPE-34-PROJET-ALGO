# tournament_logic.py
import random
import json
from match_simulator import simulate_match, simulate_penalty_shootout

GROUPS_PATH = "data/group_stage.json"
KNOCKOUT_PATH = "data/knockout_stage.json"

def draw_groups(teams):
    random.shuffle(teams)
    groups = {chr(65 + i): teams[i*4:(i+1)*4] for i in range(8)}
    return groups

def play_group_stage(groups):
    results = {}
    qualified = []

    for group_name, teams in groups.items():
        scores = {team["name"]: {"points": 0, "diff": 0, "team": team} for team in teams}

        for i in range(4):
            for j in range(i + 1, 4):
                t1, t2 = teams[i], teams[j]
                g1, g2 = simulate_match(t1, t2)

                scores[t1["name"]]["diff"] += (g1 - g2)
                scores[t2["name"]]["diff"] += (g2 - g1)

                if g1 > g2:
                    scores[t1["name"]]["points"] += 3
                elif g1 < g2:
                    scores[t2["name"]]["points"] += 3
                else:
                    scores[t1["name"]]["points"] += 1
                    scores[t2["name"]]["points"] += 1

        sorted_teams = sorted(scores.values(), key=lambda x: (x["points"], x["diff"]), reverse=True)
        qualified.extend([sorted_teams[0]["team"], sorted_teams[1]["team"]])
        results[group_name] = sorted_teams

    with open(GROUPS_PATH, "w") as f:
        json.dump({k: [{"name": t["team"]["name"], "points": t["points"], "diff": t["diff"]} for t in v] for k, v in results.items()}, f, indent=2)
    return qualified

def draw_knockout(qualified):
    random.shuffle(qualified)
    pairs = [(qualified[i], qualified[i + 1]) for i in range(0, 16, 2)]
    return pairs

def play_knockout_stage(pairs):
    winners = []

    for team1, team2 in pairs:
        g1, g2 = simulate_match(team1, team2)
        if g1 > g2:
            winners.append(team1)
        elif g2 > g1:
            winners.append(team2)
        else:
            winner = team1 if simulate_penalty_shootout() == "team1" else team2
            winners.append(winner)

    return winners
