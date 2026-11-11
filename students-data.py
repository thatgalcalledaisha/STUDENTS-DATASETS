import random
import csv

departments = ["Computer Science", "Software Engineering", "Cybersecurity",
               "Artificial Intelligence", "Information Technology"]
levels = [100, 200, 300, 400]

students = []

for i in range(1, 101):  # 100 students
    attendance = round(random.uniform(40, 100), 1)
    score = round(min(100, random.uniform(attendance * 0.5, attendance * 0.9)), 1)

    student = {
        "student_id": f"STU{i:03d}",
        "department": random.choice(departments),
        "level": random.choice(levels),
        "attendance": attendance,
        "avg_exam_score": score,
    }
    students.append(student)

with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=students[0].keys())
    writer.writeheader()
    writer.writerows(students)

print("Done! students.csv created")