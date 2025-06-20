# team_manager.py
import json
import random
import os

TEAM_NAMES = [
    "Real Madrid", "Barcelona", "Liverpool", "Manchester City", "Chelsea", "PSG",
    "Bayern Munich", "Juventus", "Inter Milan", "AC Milan", "Arsenal", "Napoli",
    "Atletico Madrid", "Sevilla", "Dortmund", "RB Leipzig", "Benfica", "Ajax",
    "Porto", "Shakhtar", "Galatasaray", "Celtic", "Rangers", "Marseille",
    "Sporting", "Feyenoord", "Lazio", "Roma", "Monaco", "Valencia", "Brugge", "Salzburg"
]

DATA_PATH = "data/teams.json"

def create_teams():
    teams = []
    for name in TEAM_NAMES:
        team = {
            "name": name,
            "strength": random.randint(50, 100),
            "goals_scored": 0,
            "goals_conceded": 0
        }
        teams.append(team)
    return teams

def save_teams(teams):
    os.makedirs("data", exist_ok=True)
    with open(DATA_PATH, "w") as f:
        json.dump(teams, f, indent=2)

def load_teams():
    with open(DATA_PATH, "r") as f:
        return json.load(f)

if __name__ == "__main__":
    teams = create_teams()
    save_teams(teams)
    print(f"{len(teams)} équipes créées et sauvegardées dans '{DATA_PATH}'")
