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
        print("\n")
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

class student_manager(student_class, course_class):
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

# Add the new courses here 
obj.add_course("101", "Python", "Anmol Singla")
obj.add_course("102", "Java", "Girish Patil")
obj.add_course("103", "C++", "Priyesh Thakur")

# Add the new students here
obj.add_student("A4159", "Meherdeep Singh", 19)
obj.add_student("A4160", "Lavanya Jain", 19)

# If you want to remove any students, do it here

# If you want to enroll a paticular student in a course, do it here
obj.enroll_student("A4159", "101")
obj.enroll_student("A4159", "102")

obj.enroll_student("A4160", "101")
obj.enroll_student("A4160", "102")

# If you want to assign a grade, do it here
obj.assign_grade("A4159", "101", 96)
obj.assign_grade("A4159", "102", 91)

obj.assign_grade("A4160", "101", 93)
obj.assign_grade("A4160", "102", 92)

# Fetch any student, do it here
obj.get_student("A4159")
obj.get_student("A4160")








        


