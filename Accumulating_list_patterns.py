
import random 

def determine_week_productivity(weeks):
    """Returns how user week is spent based on daily input"""
    time = []
    
    
        

for i in range(7):
    week = []
    rating = input("How was your day (Rate it from 1-10): ")
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    while True:
        rating = input("How was your day (Rate it from 1-10): ")

        if rating in num:
            week.append(int(rating))
            break

print(week)




















