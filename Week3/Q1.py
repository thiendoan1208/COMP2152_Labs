print("=" * 50)
print("Question 1: Student Grade List")
print("=" * 50)

grade = [85, 93, 78, 95, 88]
grade.append(94)
grade.sort()

print("Sorted list: ", grade)
print("Highest grade: ", grade[-1])
print("Lowest grade: ", grade[0])
print("Total number of grades: ", len(grade))
print("=" * 50)