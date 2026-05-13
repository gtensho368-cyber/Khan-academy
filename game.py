
from time import time

import functions

# football match simulator

for time in range(90):
    home = functions.home_goal(time)
    away = functions.away_goal(time)
    if time == 89:
        print(f"Time: 90 minutes")
        print(f"Home team goals: {home}")
        print(f"Away team goals: {away}")


if home > away:
    print("The home team has won!")
elif away > home:
    print("The away team has won!")
else:
    print("The match is a draw!")
