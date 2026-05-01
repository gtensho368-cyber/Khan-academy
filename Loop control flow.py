
# team points statistics
import random   

team1 = 0
team2 = 0

for time in range(10, 100, 10):
    # Simulate scoring: add random points each time step
    team1 += random.randint(0, 3)
    team2 += random.randint(0, 3)
    
    print(f"At {time} minutes: Team1 has {team1} points, Team2 has {team2} points")

    # Check if any team has reached 10 points
    if team1 >= 10 or team2 >= 10:
        if team1 > team2:
            print("Team1 wins!")
            break
        elif team2 > team1:
            print("Team2 wins!")
            break
        else:
            print("Both teams have reached 10 points! It's a tie.")
            break
    
else:
    print("Game ended without a winner reaching 10 points.")

