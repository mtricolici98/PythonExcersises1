"""
Complete the ??? below to make the following program work.

The program registers the names and the grades of various students in a school.
The program should find the highest grade of each student and print it out in the following fashion:

"Student Marius has 8 as his highest grade"

Additionally, add a 4th student to the students_info dictionary.

What would happen if we added another grade (9) to Marius' grades?
"""

students_info = {
    "Marius": {
        "grades": [5, 7, 8, 2]
    },
    "Iva": {
        "grades": [8, 9, 10, 6]
    },
    "Anton": {
        "grades": [7, 6, 5, 9]
    }
}

for student in students_info:
    student_grades = students_info[student]["???"]
    highest_grade = max(???)
    print(f"Student {???} has {???} as his highest grade")
