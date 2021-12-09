import random

same_team_count = 0
total_count = 0

for j in range(1, 100000):
    team1 = []
    team2 = []

    for i in range(9):
        if len(team1) == 5:
            team2.append(i)
            continue
        if len(team2) == 5:
            team1.append(i)
            continue
        team = random.randint(1,2)
        if team == 1:
            team1.append(i)
        if team == 2:
            team2.append(i)

    if (1 in team1 and 2 in team1) or (1 in team2 and 2 in team2):
        same_team_count += 1

    total_count += 1

print(f'percentage of times that players are on same team: {same_team_count / total_count}')