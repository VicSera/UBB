from Modules.UI.MenuUI import MenuUI
from Modules.Services.DisciplineHandler import *
from Modules.Services.GradeHandler import *
from Modules.Services.StudentHandler import *
from Settings import Settings
from Builder import Builder


if __name__ == '__main__':
    Settings.initialize()
    Builder.initialize()

    student_repository = Builder.get_student_repository()
    discipline_repository = Builder.get_discipline_repository()
    grade_repository = Builder.get_grade_repository()

    # initialize handlers
    student_handler = StudentHandler(student_repository)
    discipline_handler = DisciplineHandler(discipline_repository)
    grade_handler = GradeHandler(grade_repository)

    # initialize UI
    ui = MenuUI(discipline_handler, student_handler, grade_handler)

    ui.launch()