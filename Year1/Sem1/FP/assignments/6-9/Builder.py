from Modules.Repositories.JsonRepository import JsonRepository
from Modules.Services.DisciplineHandler import *
from Modules.Services.GradeHandler import *
from Modules.Services.StudentHandler import *
from Settings import Settings
from Modules.Domain.Discipline import Discipline
from Modules.Domain.Grade import Grade
from Modules.Domain.Student import Student
from Modules.Repositories.Repository import Repository
from Modules.Repositories.BinaryRepository import BinaryRepository
from Modules.Repositories.FileBasedRepository import FileRepository


repository_options = {
    'inmemory': Repository,
    'textfiles': FileRepository,
    'binaryfiles': BinaryRepository,
    'jsonfiles': JsonRepository
}


class Builder:
    repository_constructor = None
    @staticmethod
    def initialize():
        Builder.repository_constructor = repository_options[Settings.REPOSITORY_TYPE]

    @staticmethod
    def get_student_repository():
        if Settings.REPOSITORY_TYPE == 'inmemory':
            return Builder.repository_constructor()
        elif Settings.REPOSITORY_TYPE == 'textfiles':
            return Builder.repository_constructor(Settings.STUDENTS_FILE, Student)
        elif Settings.REPOSITORY_TYPE == 'binaryfiles':
            return Builder.repository_constructor(Settings.STUDENTS_FILE)
        elif Settings.REPOSITORY_TYPE == 'jsonfiles':
            return Builder.repository_constructor(Settings.STUDENTS_FILE, Student)

    @staticmethod
    def get_discipline_repository():
        if Settings.REPOSITORY_TYPE == 'inmemory':
            return Builder.repository_constructor()
        elif Settings.REPOSITORY_TYPE == 'textfiles':
            return Builder.repository_constructor(Settings.DISCIPLINE_FILE, Discipline)
        elif Settings.REPOSITORY_TYPE == 'binaryfiles':
            return Builder.repository_constructor(Settings.DISCIPLINE_FILE)
        elif Settings.REPOSITORY_TYPE == 'jsonfiles':
            return Builder.repository_constructor(Settings.DISCIPLINE_FILE, Discipline)

    @staticmethod
    def get_grade_repository():
        if Settings.REPOSITORY_TYPE == 'inmemory':
            return Builder.repository_constructor(has_id=False)
        elif Settings.REPOSITORY_TYPE == 'textfiles':
            return Builder.repository_constructor(Settings.GRADES_FILE, Grade, has_id=False)
        elif Settings.REPOSITORY_TYPE == 'binaryfiles':
            return Builder.repository_constructor(Settings.GRADES_FILE, has_id=False)
        elif Settings.REPOSITORY_TYPE == 'jsonfiles':
            return Builder.repository_constructor(Settings.GRADES_FILE, Grade, has_id=False)
