from Modules.Domain.Student import Student
from Modules.Domain.StudentValidator import StudentValidator


class StudentService:
    def __init__(self, repository):
        self.__repository = repository

    def add_student(self, id, name, attendance_count, grades):
        """
        Function that constructs a student, calls the validator, and adds the student to the repository
        if everything went fine
        """
        new_student = Student(id, name, attendance_count, grades)
        StudentValidator.validate(new_student, self.__repository.get_all_ids())

        self.__repository.add(new_student)

    def get_all_students(self):
        """
        Function that return all students from the repository
        """
        return self.__repository.get_all_students()

    def give_bonus(self, minimum_attendance, bonus):
        """
        Function that handles the bonus-based-on-attendance functionality
        """
        students = self.__repository.get_all_students()
        maximum_grade = 10

        for student in students:
            if student.attendance_count >= minimum_attendance:
                student.grade = min(student.grade + bonus, maximum_grade)

    def get_all_with_name(self, name):
        """
        Function that searches for a given name in the student list, and returns all matches
        """
        students = self.__repository.get_all_students()
        filtered_students = []

        for student in students:
            if name in student.name:
                filtered_students.append(student)

        filtered_students.sort(key=lambda student: student.name)

        return filtered_students