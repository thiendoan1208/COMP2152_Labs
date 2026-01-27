print("=" * 40)
print("Question 4: Class Attendance")
print("=" * 40)

monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class =  {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")

print("Monday class", monday_class)
print("Wednesday class", wednesday_class)
print("Attended both classes: ", monday_class & wednesday_class)
print("Attended either classes: ", monday_class | wednesday_class)
print("Only Monday: ", monday_class - wednesday_class)
print("Only one class (not both): ", monday_class ^ wednesday_class)
print("Is monday subset of all students: ", monday_class <= (monday_class | wednesday_class))