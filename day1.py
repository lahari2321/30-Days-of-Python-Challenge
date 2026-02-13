# ✅ DAY 1 CHALLENGE (Practical + Useful)
# 🎯 Problem: Student Marks Analyzer
# 📌 Task:
# Create a Python program that:
# Takes a list of student marks
# Calculates:
# Average marks
# Highest marks
# Lowest marks
# Count how many students passed (pass mark = 40)
# Print Grade:
# 90+ → A
# 75–89 → B
# 50–74 → C
# Below 50 → Fail

marks = [85, 92, 78, 96, 45, 67, 88, 54, 72, 90]
print('Student Marks:' , marks)
count=0
avearge_marks=sum(marks)/len(marks)
height_marks=max(marks)
lowest_marks=min(marks)

for i in marks:
    if i >40:
        count=count+1
        

print('Average Marks: ',avearge_marks)
print('Highest Marks: ',height_marks)
print('Lowest Marks: ',lowest_marks)
print('Passed Students: ',count)
print('Grades:')

for mark in marks: 
    if mark >= 90:
        Grade ='A'
    elif mark >= 75 and mark < 90:
        Grade='B'
    elif mark >= 50 and mark < 75:
        Grade='C'
    else:
        Grade='Fail'

    print(f'{mark} : {Grade}')

