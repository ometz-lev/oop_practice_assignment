# Class Definition:
# Create a class called Student with attributes name, email and list of grades.
# The class should have methods to add a grade, calculate the average grade and display the student's information.
class Student:
    def __init__(self, name, email, grades):
        self.name = name                                   # Initialize the name, email and grades attributes
        self.email = email                                 # Public attributes
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades)
    
    def display_info(self):
        print(f"Name: {self.name}", f"Email: {self.email}", f"Grades: {self.grades}", sep="\n")

    def grades_tuple(self):
        return tuple(self.grades)                                

# Working with Objects:
# Create 3 student objects with different names, emails, and grades
student1 = Student("Mary Brown", "mbrown@xyz.com", [95])
student2 = Student("John Doe", "jdoe@xyz.com", [85])
student3 = Student("Kim Smith", "ksmith@xyz.com", [100])

# Add new 2 grades to each student using the add_grade method
student1.add_grade(80)
student1.add_grade(75)
student2.add_grade(65)
student2.add_grade(75)
student3.add_grade(85)
student3.add_grade(95)

# Print the students' information and their average grade using the display_info and average_grade methods
for student in [student1, student2, student3]:
    student.display_info()
    print(f"Average Grade: {student.average_grade():.2f}\n")

# Dictionary and Set Integration:
# Create a dictionary that maps student emails to their corresponding student objects and use 
# the get method to retrieve a student object by email and display their information.
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3,
}

def get_student_by_email(email):
    student = student_dict.get(email)
    if student:
        student.display_info()
    else:
        print("Student not found.")

# Call the get function to retrieve a student object from the dictionary safely and display their information.
get_student_by_email("mbrown@xyz.com")
get_student_by_email("jdoe@xyz.com")
get_student_by_email("tcole@xyz.com")               # This email does not exist in the dictionary Output: Student not found.

# Create a set of all unique grades from all students and print the set.
unique_grades = set()
for student in [student1, student2, student3]:
    unique_grades.update(student.grades)
print(f"The set of unique grades: {unique_grades}\n")

# Part 4 Tuple Practice:
# Create a method in the Student class that returns a tuple of the student's grades, and call this method
# for each student to display their grades as tuples.
# Add try/except blocks to handle changing a grade to a non-numeric value and display an error message if this occurs.
for student in [student1, student2, student3]:
    print(f"{student.name}'s grades as a tuple: {student.grades_tuple()}")
    try:
        test = input(f"Enter a new grade for {student.name} (or type 'skip' to skip): ")
        student.grades_tuple().__add__(test)         # This will raise a TypeError since tuples are immutable
    except TypeError:
        print(f"Error: Tuples are immutable, cannot  modify it directly.\n")

# Part 5 List Operations:
# Remove the last grade from each student's grade list and print the updated list of grades for each student.
# Print the first and last grade for each student, and the case where the student has no grades to display.
# Also print the number of grades each student now has after the removal of the last grade.
for student in [student1, student2, student3]:
    print(f"{student.name}'s number of grades: {len(student.grades)} before removal.")
    if student.grades:                              # Check if the grades list is not empty
        student.grades.pop()                        # Remove the last grade
        print(f"{student.name}'s first grade: {student.grades[0]}, last grade: {student.grades[-1]}")
        print(f"{student.name}'s number of grades: {len(student.grades)}\n")
    else:
        print(f"{student.name} has no grades to display.")

# Part 6 Bonus:
# Use regular expressions to validate the email format when creating a student object, and 
# raise a ValueError if the email is invalid.
import re

for email in [student1.email, student2.email, student3.email, "1234@kjucom9"]:
    found = re.search(r"[\w.-]+@[\w.-]+\.[a-z]{2,3}", email)           # Validate email format using regex
    if found:
        print(f"{email} is valid.")
    else:
        print(f"{email} is invalid.")

# Count how many grades are above 90 for all students
count = 0
for student in [student1, student2, student3]:
    count += sum(1 for grade in student.grades if grade > 90)
print(f"The number of grades above 90: {count}")                    # Output: The number of grades above 90: 2