from Modules.Services.GradeHandler import GradeHandler
from Modules.Services.StudentHandler import StudentHandler
from Modules.Services.DisciplineHandler import DisciplineHandler


class UI:
    def __init__(self, discipline_handler, student_handler, grade_handler):

        self._student_handler = student_handler
        self._discipline_handler = discipline_handler
        self._grade_handler = grade_handler



