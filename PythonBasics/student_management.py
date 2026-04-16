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
        print("Name of the student: ", self.name)
        print("Student ID of ", self.name, "is: ", self.student_id)
        print("Age of the student is: ", self.age)
        print("enrolled courses are: ", self.courses)
        print("Grades for all the courses are: ", self.grades)
# this is student class - storing every detail about the student

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

    def remove_student(self):
        remove_id = input("Enter the ID of the student: ")
        if(remove_id in self.students):
            del self.students[remove_id] #removes that id if present
        else: print("There is no such student present in the database")

    def get_student(self, student_id):
        if(student_id in self.students):
            self.students[student_id].display() #displays the details of the student with that id
        else: print("There is no such student present in the database")  

    def enroll_student(self, student_id, course_id):
        if(student_id in self.students and course_id in self.courses):
            self.students[student_id].enroll(course_id) #enrolls the student to the course
        else: print("There is no such student or course present in the database")  

student = student_manager()
student.add_student("1", "John", 20)
student.add_course("101", "Python", "Dr. Smith")
student.enroll_student("1", "101")

student.get_student("1")




        


