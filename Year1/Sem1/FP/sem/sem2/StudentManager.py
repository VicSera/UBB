class student:
    last_id = 0  # used as a static variable for automatic id generation

    unique_id = 0
    name = ""
    grade = 0

    def __init__(self, id, name, grade):
        self.unique_id = id
        self.name = name
        self.grade = grade
        student.last_id = self.unique_id

    def __str__(self):
        return str('ID: ' + str(self.unique_id) + ' || name: ' + self.name + ' || grade: ' + str(self.grade))

    def get_id(self):
        return self.unique_id

    def get_name(self):
        return self.name

    def get_grade(self):
        return self.grade

    def set_name(self, name):
        self.name = name

    def set_grade(self, grade):
        self.grade = grade


def print_students(student_list):
    print("Student list:")
    for student in student_list:
        print(student)


def add_student(name, grade, student_list):
    new_student = student(student.last_id + 1, name, grade)  # student.last_id is used as a static variable
    student_list.append(new_student)

def menu_add_student(student_list):
    print("Please specify the name and the grade of the student.\n")
    name = input("Name: ")
    grade = input("Grade: ")
    add_student(name, grade, student_list)

def remove_student(id, student_list):
    for student in student_list[:]:
        if student.get_id() == id:
            student_list.remove(student)

def menu_remove_student(student_list):
    id_to_remove = input("Please give the id of the student to be deleted.")
    remove_student(id_to_remove, student_list)

def run_menu():
    student_list = []
    options = {
        1 : menu_add_student,
        2 : print_students,
        3 : menu_remove_student
    }
    while True:
        print("Options:\n"
              "1. Insert a student\n"
              "2. Print list\n"
              "3. Remove a student.\n"
              "Press x to exit.\n")
        user_option = input("Choice: ")
        if user_option == 'x':
            break
        options[int(user_option)](student_list)

    print("Exiting application.\n")

if __name__ == "__main__":
    run_menu()
