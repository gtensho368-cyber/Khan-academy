
# let's start with def functions

# finding the area and perimeter of a rectangle
def Area(a, b):
    return a * b

def Perimeter(a, b):
    return 2 * (a + b)

length = int(input("Enter the length:"))
width = int(input("Enter the width:"))

print("The area is: " + str(Area(length, width)))
print("The perimeter is: " + str(Perimeter(length, width)))

