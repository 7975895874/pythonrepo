class Student:
    def _init_(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def _str_(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


students = {}


def input_student_data():
    
    num_students = int(input("Enter the number of students: "))
    
    for i in range(num_students):
        print(f"\nEnter details for student {i+1}:")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        
        
        student = Student(name, age, grade)
        
                students[name] = student


input_student_data()


print("\nStudent objects dictionary:")
for name, student in students.items():
    print(name, ":", student)
