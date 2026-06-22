
"""Recommends a Khan Academy course based on grade and subject preferences."""

# Course options to choose from for our recommendation.
fin_lit = "Financial Literacy"
math = "math"
Bio = "Biology"
chem = "chemistry"
phy = "physics"
psy = "psychology"
pixar = "Pixar in a Box"
grammar = "Grammar"

# Collect user attributes to inform our recommendation.
grade = int(input("What grade are you in? "))
favorite_subject = input("What is your favorite subject? ")
topic = input("Fav topic? ")
clas = input("Fav class? ")
lecture= input("Fav lecture? ")

# Make a course recommendation based on the user's attributes.
recommendation = ""

if topic == "math" and clas == "physics":
    recommendation = chem
elif topic == "Financial Literacy":
    recommendation = grammar
else:
    recommendation = psy


    

    

print("We recommend the Khan Academy course: " + recommendation)








