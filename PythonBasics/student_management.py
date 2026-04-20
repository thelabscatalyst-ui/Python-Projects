# we will create a student management system - oops heavy 

class student_class:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = []
        self.grades = {}

    def enroll(self, course):
        # this would add a course to the list of courses of that student 
        self.courses.append(course)
    def add_grade(self, course, marks):
        # adds the grade to the grades dictionary with course
        self.grades[course] = marks    
    def get_average(self):
        # returns the average of all the marks
        return sum(self.grades.values())/len(self.grades)
    def display(self):
        print("\n")
        print(" ---------- Student Details ---------- ")
        print("Name of the student: ", self.name)
        print("Student ID of is : ", self.student_id)
        print("Age of the student is: ", self.age)
        print(end = "\n")

        print("---------- Academic Details ---------")

        print("Enrolled Courses are: ", end="")
        print(", ".join(self.courses))

        for course, marks in self.grades.items():
            print("Marks obtained in ", course, "is: ", marks)

        print("Average marks obtained is: ", self.get_average())

class course_class:
    def __init__(self, course_id, course_name, instructor):
        self.course_name = course_name
        self.course_id = course_id
        self.instructor = instructor

    def display(self):
        print("Name of the course :", self.course_name)
        print("Course ID assigned is: ", self.course_id)
        print("Instaructor appointed for the course - ", self.course_name, "is: ", self.instructor)
        # this is course class - storing all the detail about the courses

class student_manager:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, student_id, name, age):
        student = student_class(student_id, name, age)
        self.students[student_id] = student
    def add_course(self, course_id, course_name, instructor):
        course = course_class(course_id, course_name, instructor)
        self.courses[course_id] = course
    def remove_student(self, remove_id):
        if(remove_id in self.students):
            del self.students[remove_id] 
        else: print("There is no such student present in the database")
        #removes that id if present
    def get_student(self, student_id):
        if(student_id in self.students):
            self.students[student_id].display() 
        else: print("There is no such student present in the database")  
        #displays the details of the student with that id      
    def enroll_student(self, student_id, course_id):
        if(student_id in self.students and course_id in self.courses):
            student = self.students[student_id]
            course = self.courses[course_id].course_name
            student.enroll(course)
        else: print("There is no such student or course present in the database") 
        #enrolls the student to the course
    def assign_grade(self, student_id, course_id, marks):
        if(student_id in self.students and course_id in self.courses):
            course = self.courses[course_id].course_name
            self.students[student_id].add_grade(course, marks) 
        else: print("There is no such student or course present in the database")
        #assigns the grade to the student for that course
    def get_top_student(self, course_id):
        top_marks = -1
        top_student = None
        for student in self.students.values():
            if course_id in student.grades:
                if student.grades[course_id] > top_marks:
                    top_marks = student.grades[course_id]
                    top_student = student
        if top_student:
            print("Top student in course ", course_id, "is: ", top_student.name, "with marks: ", top_marks)
        else: print("No students enrolled in this course or no grades assigned yet")

#now we will try to create a report 

obj = student_manager() # started my brain

print("Welcome to the student management system")

while True:
    print("\n")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Remove Student")
    print("4. Get Student Details")
    print("5. Enroll Student in Course")
    print("6. Assign Grade to Student")
    print("7. Get Top Student in Course")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        obj.add_student(student_id, name, age)
        print("Student added successfully!")
    
    elif choice == 2:
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        instructor = input("Enter instructor name: ")
        obj.add_course(course_id, course_name, instructor)
        print("Course added successfully!")
    
    elif choice == 3:
        remove_id = input("Enter student ID to remove: ")
        obj.remove_student(remove_id)
    
    elif choice == 4:
        student_id = input("Enter student ID to get details: ")
        obj.get_student(student_id)
    
    elif choice == 5:
        student_id = input("Enter student ID to enroll: ")
        course_id = input("Enter course ID to enroll in: ")
        obj.enroll_student(student_id, course_id)
    
    elif choice == 6:
        student_id = input("Enter student ID to assign grade: ")
        course_id = input("Enter course ID for grade assignment: ")
        marks = float(input("Enter marks obtained: "))
        obj.assign_grade(student_id, course_id, marks)
    
    elif choice == 7:
        course_id = input("Enter course ID to get top student: ")
        obj.get_top_student(course_id)
    
    elif choice == 8:
        print("Exiting the system. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please try again.")
