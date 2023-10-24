grades = []
average = 0

for index in range(4):
    grades.append(float(input("Enter a grade: ")))

#Computes for the average
for index in grades:
    average += index

average /= 4

print("Average: ",average)

#Evaluates if Average is Passed or Failed
if average >= 75:
    print("You Passed!")
else:
    print("You Failed...")

#Evaluates the Grade
if average >= 90:
    print("Outstanding!")
elif average >= 85 and average < 90:
    print("Very Satisfactory")
elif average >= 75 and average < 85:
    print("Satisfactory")
elif average < 75:
    print("Needs Improvement")







