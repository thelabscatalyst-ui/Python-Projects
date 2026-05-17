# ── Grading config ─────────────────────────────────────
GRADE_SCALE = [
    (90, "A+", 4.0),
    (80, "A",  3.7),
    (70, "B+", 3.3),
    (60, "C+", 2.3),
    (50, "D",  1.0),
    (40, "C-", 1.7),
    (0,  "F",  0.0),
]
students = [
    {"name": "Aarav",   "marks": {"Maths": 88, "Science": 76, "English": 91, "Hindi": 65, "CS": 95}},
    {"name": "Sneha",   "marks": {"Maths": 55, "Science": 60, "English": 72, "Hindi": 80, "CS": 38}},
    {"name": "Rohan",   "marks": {"Maths": 35, "Science": 42, "English": 50, "Hindi": 38, "CS": 60}},
    {"name": "Priya",   "marks": {"Maths": 92, "Science": 89, "English": 95, "Hindi": 88, "CS": 97}},
    {"name": "Karan",   "marks": {"Maths": 70, "Science": 65, "English": 58, "Hindi": 72, "CS": 80}},
    {"name": "Meera",   "marks": {"Maths": 45, "Science": 38, "English": 62, "Hindi": 55, "CS": 50}},
    {"name": "Arjun",   "marks": {"Maths": 78, "Science": 82, "English": 74, "Hindi": 69, "CS": 88}},
]

PASS_MARK = 40

def get_letter_grade(average):
    for marks, grade, gpa in GRADE_SCALE:
        if average >= marks:
            return grade, gpa
    return "F"
    pass

def get_average(marks_dict):
    total_marks = sum(marks_dict.values())
    average = total_marks / len(marks_dict)
    return average
    pass

def get_failed_subjects(marks_dict):
    sub_f=[]
    for subject, marks in marks_dict.items():
        if marks < PASS_MARK:
            sub_f.append(subject)
    print('Failed Subjects:', sub_f)
    return sub_f
    pass

def build_results(students):
    answer = [] # list created

    for stud in students:
        sample_average = get_average(stud["marks"].values())
        stud["average"] = sample_average
    # got the average

    for stud in students:
        sample_grade, sample_gpa = get_letter_grade(stud["average"].values())
        stud.append(sample_grade)
        stud.append(sample_gpa)
        # got the grade and gpa

    for stud in students:
        sample_failed = get_failed_subjects(stud["marks"].values())
        stud.append(sample_failed)
        # got failed subjects 

    sorted_students = students.sort(key = lambda x: x["average"], reverse = True)
    for rank, student in enumerate(sorted_students, start=1):
        student["rank"] = rank

    return sorted_students
    pass

def print_report_table():

    for student in results:
        print(f"{student['rank']:<5} {student['name']:<5} {student['average']:<10.2f} {student['grade']:<10} {student['gpa']:<10.2f} {', '.join(student['failed_subjects']):<20}")
