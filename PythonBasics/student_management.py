# ============================================================
#  Student Management System — Phase 1: OOP Foundations
#  Concepts: Encapsulation, @property, dunder methods,
#            @classmethod, @staticmethod, class variables
# ============================================================


class Student:
    # ── CLASS VARIABLE ───────────────────────────────────────
    # Shared across ALL instances. Every new Student increments this.
    # Access via Student.count — not self.count (that would be instance).
    count = 0

    def __init__(self, student_id, name, age):
        # ── ENCAPSULATION ────────────────────────────────────
        # Double underscore (__) makes an attribute "private".
        # Python mangles the name to _Student__name internally,
        # so outside code can't accidentally do student.__name.
        # You MUST go through the @property getter/setter below.
        self.__student_id = student_id
        self.__name = name
        self.__age = age          # setter will validate this
        self.__courses = []
        self.__grades = {}        # { course_name: marks }

        Student.count += 1        # update class variable on each new student

    # ── PROPERTIES (getter + setter) ─────────────────────────
    # @property turns a method into a "smart attribute".
    # Reading  student.name  calls the getter.
    # Writing  student.name = "x"  calls the setter.

    @property
    def student_id(self):
        return self.__student_id  # read-only: no setter defined

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            print("Error: Name must be a non-empty string.")
            return
        self.__name = value.strip()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            print("Error: Age must be a positive integer.")
            return
        self.__age = value

    @property
    def courses(self):
        # Return a copy so outside code can't mutate the private list directly
        return list(self.__courses)

    @property
    def grades(self):
        return dict(self.__grades)

    # ── STATIC METHOD ────────────────────────────────────────
    # @staticmethod belongs to the class, not any instance.
    # No 'self' or 'cls' — it's just a plain utility function
    # that logically lives here because it relates to Student marks.
    @staticmethod
    def is_valid_marks(marks):
        """Returns True if marks are between 0 and 100."""
        return isinstance(marks, (int, float)) and 0 <= marks <= 100

    # ── CLASS METHOD ─────────────────────────────────────────
    # @classmethod receives the CLASS itself as the first arg (cls).
    # Used as an alternative constructor — a second way to build a Student.
    # Useful in Phase 4 when we load students from a JSON file.
    @classmethod
    def from_dict(cls, data):
        """Create a Student from a dictionary. e.g. Student.from_dict(d)"""
        student = cls(data["student_id"], data["name"], data["age"])
        for course in data.get("courses", []):
            student.__courses.append(course)
        for course, marks in data.get("grades", {}).items():
            student.__grades[course] = marks
        return student

    # ── REGULAR METHODS ──────────────────────────────────────
    def enroll(self, course):
        if course not in self.__courses:
            self.__courses.append(course)

    def add_grade(self, course, marks):
        if not Student.is_valid_marks(marks):   # reusing our @staticmethod
            print(f"Error: Marks {marks} are invalid. Must be between 0–100.")
            return
        self.__grades[course] = marks

    def get_average(self):
        if not self.__grades:
            return 0.0
        return sum(self.__grades.values()) / len(self.__grades)

    # ── DUNDER METHODS ───────────────────────────────────────
    # Python calls these automatically in specific situations.

    def __str__(self):
        # Called by print(student) or str(student).
        # Replaces the old display() method — cleaner and more Pythonic.
        courses_str = ", ".join(self.__courses) if self.__courses else "None"
        grades_str = "\n".join(
            f"    {course}: {marks}" for course, marks in self.__grades.items()
        ) if self.__grades else "    No grades yet"

        return (
            f"\n{'='*42}\n"
            f"  Student Details\n"
            f"{'='*42}\n"
            f"  ID   : {self.__student_id}\n"
            f"  Name : {self.__name}\n"
            f"  Age  : {self.__age}\n"
            f"{'─'*42}\n"
            f"  Courses  : {courses_str}\n"
            f"  Grades   :\n{grades_str}\n"
            f"  Average  : {self.get_average():.2f}\n"
            f"{'='*42}"
        )

    def __repr__(self):
        # Called in the Python REPL or inside lists/dicts.
        # Should ideally be a string you could paste back to recreate the object.
        return f"Student(id={self.__student_id!r}, name={self.__name!r}, age={self.__age})"

    def __eq__(self, other):
        # Called when you do:  student_a == student_b
        # Two students are equal if they share the same ID.
        if not isinstance(other, Student):
            return NotImplemented
        return self.__student_id == other.__student_id

    def __len__(self):
        # Called by len(student) — returns number of enrolled courses.
        return len(self.__courses)


# ─────────────────────────────────────────────────────────────


class Course:
    count = 0  # class variable — tracks total courses created

    def __init__(self, course_id, course_name, instructor):
        self.__course_id = course_id
        self.__course_name = course_name
        self.__instructor = instructor
        Course.count += 1

    @property
    def course_id(self):
        return self.__course_id

    @property
    def course_name(self):
        return self.__course_name

    @property
    def instructor(self):
        return self.__instructor

    @classmethod
    def from_dict(cls, data):
        return cls(data["course_id"], data["course_name"], data["instructor"])

    def __str__(self):
        return (
            f"\n{'='*42}\n"
            f"  Course Details\n"
            f"{'='*42}\n"
            f"  ID         : {self.__course_id}\n"
            f"  Name       : {self.__course_name}\n"
            f"  Instructor : {self.__instructor}\n"
            f"{'='*42}"
        )

    def __repr__(self):
        return f"Course(id={self.__course_id!r}, name={self.__course_name!r})"


# ─────────────────────────────────────────────────────────────


class StudentManager:
    def __init__(self):
        self.__students = {}   # { student_id: Student }
        self.__courses = {}    # { course_id: Course }

    def add_student(self, student_id, name, age):
        if student_id in self.__students:
            print(f"Student with ID '{student_id}' already exists.")
            return
        self.__students[student_id] = Student(student_id, name, age)
        print(f"Student '{name}' added. Total students: {Student.count}")

    def add_course(self, course_id, course_name, instructor):
        if course_id in self.__courses:
            print(f"Course with ID '{course_id}' already exists.")
            return
        self.__courses[course_id] = Course(course_id, course_name, instructor)
        print(f"Course '{course_name}' added. Total courses: {Course.count}")

    def remove_student(self, student_id):
        if student_id in self.__students:
            name = self.__students[student_id].name
            del self.__students[student_id]
            print(f"Student '{name}' removed.")
        else:
            print(f"No student found with ID '{student_id}'.")

    def get_student(self, student_id):
        if student_id in self.__students:
            # __str__ is called automatically by print()
            print(self.__students[student_id])
        else:
            print(f"No student found with ID '{student_id}'.")

    def enroll_student(self, student_id, course_id):
        if student_id not in self.__students:
            print(f"No student found with ID '{student_id}'.")
            return
        if course_id not in self.__courses:
            print(f"No course found with ID '{course_id}'.")
            return
        course_name = self.__courses[course_id].course_name
        self.__students[student_id].enroll(course_name)
        print(f"Enrolled in '{course_name}' successfully.")

    def assign_grade(self, student_id, course_id, marks):
        if student_id not in self.__students:
            print(f"No student found with ID '{student_id}'.")
            return
        if course_id not in self.__courses:
            print(f"No course found with ID '{course_id}'.")
            return
        course_name = self.__courses[course_id].course_name
        self.__students[student_id].add_grade(course_name, marks)

    def get_top_student(self, course_id):
        if course_id not in self.__courses:
            print(f"No course found with ID '{course_id}'.")
            return
        course_name = self.__courses[course_id].course_name
        top_student = None
        top_marks = -1
        for student in self.__students.values():
            marks = student.grades.get(course_name)
            if marks is not None and marks > top_marks:
                top_marks = marks
                top_student = student
        if top_student:
            print(f"Top student in '{course_name}': {top_student.name} with {top_marks} marks.")
        else:
            print(f"No grades assigned in '{course_name}' yet.")

    def show_all_students(self):
        if not self.__students:
            print("No students in the system.")
            return
        for student in self.__students.values():
            print(repr(student))   # __repr__ in action

    def __len__(self):
        # len(manager) gives number of students
        return len(self.__students)


# ─────────────────────────────────────────────────────────────
#  Entry Point
# ─────────────────────────────────────────────────────────────

manager = StudentManager()

print("Welcome to the Student Management System")
print("(Phase 1 — OOP Foundations)")

while True:
    print("\n")
    print("1.  Add Student")
    print("2.  Add Course")
    print("3.  Remove Student")
    print("4.  Get Student Details")
    print("5.  Enroll Student in Course")
    print("6.  Assign Grade to Student")
    print("7.  Get Top Student in Course")
    print("8.  Show All Students (uses __repr__)")
    print("9.  Show Student & Course counts (class variable)")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sid  = input("Enter student ID: ")
        name = input("Enter student name: ")
        age  = int(input("Enter student age: "))
        manager.add_student(sid, name, age)

    elif choice == 2:
        cid       = input("Enter course ID: ")
        cname     = input("Enter course name: ")
        instructor = input("Enter instructor name: ")
        manager.add_course(cid, cname, instructor)

    elif choice == 3:
        sid = input("Enter student ID to remove: ")
        manager.remove_student(sid)

    elif choice == 4:
        sid = input("Enter student ID: ")
        manager.get_student(sid)

    elif choice == 5:
        sid = input("Enter student ID: ")
        cid = input("Enter course ID: ")
        manager.enroll_student(sid, cid)

    elif choice == 6:
        sid   = input("Enter student ID: ")
        cid   = input("Enter course ID: ")
        marks = float(input("Enter marks (0–100): "))
        manager.assign_grade(sid, cid, marks)

    elif choice == 7:
        cid = input("Enter course ID: ")
        manager.get_top_student(cid)

    elif choice == 8:
        manager.show_all_students()

    elif choice == 9:
        # Accessing class variables directly on the class
        print(f"Total students ever created : {Student.count}")
        print(f"Total courses ever created  : {Course.count}")
        print(f"Students currently in system: {len(manager)}")   # __len__

    elif choice == 10:
        print("Exiting. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
