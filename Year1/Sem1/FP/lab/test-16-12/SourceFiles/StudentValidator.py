class ValidationError(Exception):
    pass


class StudentValidator:
    @staticmethod
    def check_name(name):
        # check if name contains 2 words
        words = name.split()
        if len(words) < 2:
            raise ValidationError('Not enough words in name')

        # check if each word has at least 3 letters
        for word in words:
            if len(word) < 3:
                raise ValidationError('Not enough characters in the name')

    @staticmethod
    def check_grade(grade):
        # check if grade is between 0 and 10
        if grade < 0 or grade > 10:
            raise ValidationError('Grade not in range 0-10')

    @staticmethod
    def check_attendance(attendance):
        # check if attendance is a positive number
        if attendance < 0:
            raise ValidationError('Attendance can\'t be a negative number')

    @staticmethod
    def check_unique_id(id, all_ids):
        # check if the id is unique
        if id in all_ids:
            raise ValidationError('ID not unique')

    @staticmethod
    def validate(student, all_student_ids):
        StudentValidator.check_name(student.name)
        StudentValidator.check_grade(student.grade)
        StudentValidator.check_attendance(student.attendance_count)
        StudentValidator.check_unique_id(student.id, all_student_ids)