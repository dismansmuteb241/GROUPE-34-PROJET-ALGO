# match_simulator.py
import random

def simulate_match(team1, team2):
    strength1 = team1["strength"]
    strength2 = team2["strength"]

    goals1 = max(0, int(random.gauss(strength1 / 25, 1.5)))
    goals2 = max(0, int(random.gauss(strength2 / 25, 1.5)))

    team1["goals_scored"] += goals1
    team1["goals_conceded"] += goals2
    team2["goals_scored"] += goals2
    team2["goals_conceded"] += goals1

    return goals1, goals2

def simulate_penalty_shootout():
    return random.choice(["team1", "team2"])
