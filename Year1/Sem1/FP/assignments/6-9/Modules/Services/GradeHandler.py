from Modules.Services.Handler import Handler
from Modules.Domain.Grade import Grade
from Modules.Repositories.Repository import Repository


class NoGradeException(Exception):
    pass


class GradeHandler(Handler):
    def __init__(self, repository):
        super(GradeHandler, self).__init__(repository)
        # self.__initialize_grades()

    def add(self, discipline_id, student_id, value):
        new_grade = Grade(discipline_id, student_id, value)
        self._repository.add_element(new_grade)
        return new_grade

    def remove_from_student(self, student_id):
        return self._repository.remove_by_attribute('student_id', student_id)

    def remove_from_discipline(self, discipline_id):
        return self._repository.remove_by_attribute('discipline_id', discipline_id)

    def remove_entity(self, entity):
        for grade in self._repository:
            if grade == entity:
                self._repository.remove(grade)
                return grade

    def get_failing_students(self):
        all_students = self.__get_all_students_with_grades()
        all_disciplines = self.__get__all_disciplines_with_grades()
        failing_students = []

        for student in all_students:
            for discipline in all_disciplines:
                try:
                    if self.get_average_for_student_at_discipline(student, discipline) < 5:
                        failing_students.append(student)
                except NoGradeException:
                    continue

        return failing_students

    def get_average_for_student_at_discipline(self, student_id, discipline_id):
        grade_sum, count = 0, 0

        for grade in self._repository:
            if grade.student_id is student_id and grade.discipline_id is discipline_id:
                grade_sum += grade.grade_value
                count += 1

        if count is 0:
            raise NoGradeException()
        return grade_sum / count

    def get_best_students(self):
        students = self.__get_all_students_with_grades()
        averages = {}

        for student in students:
            average = self.get_aggregated_average_for_student(student)
            averages[student] = average

        students.sort(key=lambda student: averages[student], reverse=True)
        return [(student, averages[student]) for student in students]

    def get_discipline_hierarchy(self):
        disciplines = self.__get__all_disciplines_with_grades()
        averages = {}

        for discipline in disciplines:
            average = self.get_average_for_discipline(discipline)
            averages[discipline] = average

        disciplines.sort(key=lambda discipline: averages[discipline], reverse=True)
        return [(discipline, averages[discipline]) for discipline in disciplines]

    def get_average_for_discipline(self, discipline_id):
        grade_sum, count = 0, 0

        for grade in self._repository:
            if grade.discipline_id is discipline_id:
                grade_sum += grade.grade_value
                count += 1

        return grade_sum / count

    def get_aggregated_average_for_student(self, student_id):
        disciplines = self.__get__all_disciplines_with_grades()
        sum_of_averages, count = 0, 0

        for discipline_id in disciplines:
            try:
                average_grade = self.get_average_for_student_at_discipline(student_id, discipline_id)
                sum_of_averages += average_grade
                count += 1
            except NoGradeException:
                continue

        if count is 0:
            raise NoGradeException()
        return sum_of_averages / count

    def __get_all_students_with_grades(self):
        students = []

        for grade in self._repository:
            if grade.student_id not in students:
                students.append(grade.student_id)

        return students

    def __get__all_disciplines_with_grades(self):
        disciplines = []

        for grade in self._repository:
            if grade.discipline_id not in disciplines:
                disciplines.append(grade.discipline_id)

        return disciplines

    def __initialize_grades(self):
        self.add(1, 1, 10)
        self.add(1, 2, 9)
        self.add(2, 3, 10)
        self.add(2, 3, 7)
        self.add(2, 4, 5)

