from geometric_lib import circle
from geometric_lib import square

try:
    value = int(input("Enter a num: "))
    print(f"Square:\n\tS = {square.area(value)}\n\tP = {square.perimeter(value)}")
    print(f"Circle:\n\tS = {circle.area(value)}\n\tP = {circle.perimeter(value)}")

except ValueError:
    print("This is not a number! :(")
