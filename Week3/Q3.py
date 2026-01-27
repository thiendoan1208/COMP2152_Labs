point1 = (3, 5)
point2 = (7, 2)

x1, y1 = point1
x2, y2 = point2

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

tuple_str = tuple("PYTHON")

print("Point 1: ", point1)
print("Point 2: ", point2)

print("x1 = ", x1, "," , "y1 = ", y1)
print("x2 = ", x2, "," , "y2 = ", y2)

print("Distance between points: ", distance)

print("Character tuple: ", tuple_str)

for item in tuple_str:
    print(item)
