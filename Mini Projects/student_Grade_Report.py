# ── Grading config ─────────────────────────────────────
# NOTE: original scale was non-monotonic — GPA went 1.0 (at 50) then 1.7 (at 40),
# so a LOWER score got a HIGHER GPA. Swapped the two rows. Revert if intentional.
GRADE_SCALE = [
    (90, "A+", 4.0),
    (80, "A",  3.7),
    (70, "B+", 3.3),
    (60, "C+", 2.3),
    (50, "C-", 1.7),   # was (50, "D",  1.0)
    (40, "D",  1.0),   # was (40, "C-", 1.7)
    (0,  "F",  0.0),
]

students = [
    {"name": "Aarav", "marks": {"Maths": 88, "Science": 76, "English": 91, "Hindi": 65, "CS": 95}},
    {"name": "Sneha", "marks": {"Maths": 55, "Science": 60, "English": 72, "Hindi": 80, "CS": 38}},
    {"name": "Rohan", "marks": {"Maths": 35, "Science": 42, "English": 50, "Hindi": 38, "CS": 60}},
    {"name": "Priya", "marks": {"Maths": 92, "Science": 89, "English": 95, "Hindi": 88, "CS": 97}},
    {"name": "Karan", "marks": {"Maths": 70, "Science": 65, "English": 58, "Hindi": 72, "CS": 80}},
    {"name": "Meera", "marks": {"Maths": 45, "Science": 38, "English": 62, "Hindi": 55, "CS": 50}},
    {"name": "Arjun", "marks": {"Maths": 78, "Science": 82, "English": 74, "Hindi": 69, "CS": 88}},
]

PASS_MARK = 40


def get_letter_grade(average):
    # GRADE_SCALE is sorted high->low, so the first threshold met is the band
    for threshold, grade, gpa in GRADE_SCALE:
        if average >= threshold:
            return grade, gpa
    return "F", 0.0  # safety net (unreachable while a 0-threshold row exists)


def get_average(marks_source):
    """
    Compute average from either a mapping (dict) of subject->marks or
    an iterable of numeric marks (e.g., dict_values or list).
    """
    # If a dict-like with .values(), use its values; otherwise assume iterable
    if hasattr(marks_source, "values"):
        marks_iter = marks_source.values()
    else:
        marks_iter = marks_source

    marks_list = list(marks_iter)
    if not marks_list:
        return 0.0
    return sum(marks_list) / len(marks_list)


def get_failed_subjects(marks_dict):
    return [subject for subject, mark in marks_dict.items() if mark < PASS_MARK]


def build_results(students):
    # single pass: enrich each student dict
    for stud in students:
        stud["average"] = get_average(stud["marks"])
        stud["grade"], stud["gpa"] = get_letter_grade(stud["average"])
        stud["failed_subjects"] = get_failed_subjects(stud["marks"])

    # sorted() returns a NEW list. list.sort() returns None -> was the crash.
    ranked = sorted(students, key=lambda s: s["average"], reverse=True)
    for rank, stud in enumerate(ranked, start=1):
        stud["rank"] = rank

    return ranked


def print_report_table(results):
    header = f"{'Rank':<5}{'Name':<10}{'Total':<8}{'Average':<10}{'Grade':<8}{'GPA':<6}"
    print(header)
    print("-" * len(header))

    for stud in results:
        total = sum(stud["marks"].values())
        print(
            f"{stud['rank']:<5}{stud['name']:<10}{total:<8}"
            f"{stud['average']:<10.2f}{stud['grade']:<8}{stud['gpa']:<6.2f}"
        )

    print()
    for stud in results:
        if stud["failed_subjects"]:
            print(f"{stud['name']} failed in: {', '.join(stud['failed_subjects'])}")


def subject_stats(students):
    stats = {}
    subjects = list(students[0]["marks"].keys())

    for subject in subjects:
        total = 0
        min_mark, max_mark = float("inf"), float("-inf")  # robust sentinels
        min_student = max_student = ""

        for stud in students:
            mark = stud["marks"][subject]
            total += mark
            if mark < min_mark:
                min_mark, min_student = mark, stud["name"]
            if mark > max_mark:
                max_mark, max_student = mark, stud["name"]

        stats[subject] = {
            "average": total / len(students),
            "min": {"name": min_student, "marks": min_mark},
            "max": {"name": max_student, "marks": max_mark},
        }
    return stats


def print_subject_stats(stats):
    print(f"\n{'Subject':<10}{'Average':<10}{'Topper':<22}{'Lowest':<22}")
    print("-" * 64)
    for subject, data in stats.items():
        topper = f"{data['max']['name']} ({data['max']['marks']})"
        lowest = f"{data['min']['name']} ({data['min']['marks']})"
        print(f"{subject:<10}{data['average']:<10.2f}{topper:<22}{lowest:<22}")


# ── Run ────────────────────────────────────────────────
if __name__ == "__main__":
    results = build_results(students)
    print_report_table(results)
    print_subject_stats(subject_stats(students))