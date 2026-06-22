
import random
import functions
import lists_data

data = lists_data.screen_time



minutes = functions.minutes_spent(data, [])
print(f"You spent a total of {minutes} minutes.")

personal = functions.minutes_spent(data, ["zoom", "khan_academy", "gmail"])
print(f"You spent {personal} personal minutes")

sessions = functions.sessions_taken(data)
print(f"Total of {sessions} sessions.")

average = functions.screen_time_average(minutes, sessions)
print(f"Average session is {average} minutes long.")







