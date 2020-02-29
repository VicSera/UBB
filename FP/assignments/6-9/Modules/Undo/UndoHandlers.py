from enum import Enum


class UndoResolver:
    @staticmethod
    def undo_add(handler, entity):
        handler.remove(entity.id)

    @staticmethod
    def undo_add_grade(handler, grade):
        handler.remove_entity(grade)

    @staticmethod
    def undo_remove_student(handler, student):
        handler.add(student.id, student.name)

    @staticmethod
    def undo_remove_discipline(handler, discipline):
        handler.add(discipline.id, discipline.name)

    @staticmethod
    def undo_remove_grade(handler, grade):
        handler.add(grade.discipline_id, grade.student_id, grade.grade_value)

    @staticmethod
    def undo_update(handler, id, attribute, old_value, new_value):
        handler.update_attribute(id, attribute, old_value)

    @staticmethod
    def revert_undo_update(handler, id, attribute, old_value, new_value):
        handler.update_attribute(id, attribute, new_value)


class UndoHandler:#(Enum):
    ADD_STUDENT = (UndoResolver.undo_add, UndoResolver.undo_remove_student)
    ADD_DISCIPLNE = (UndoResolver.undo_add, UndoResolver.undo_remove_discipline)
    ADD_GRADE = (UndoResolver.undo_add_grade, UndoResolver.undo_remove_grade)

    REMOVE_STUDENT = (UndoResolver.undo_remove_student, UndoResolver.undo_add)
    REMOVE_DISCIPLINE = (UndoResolver.undo_remove_discipline, UndoResolver.undo_add)
    REMOVE_GRADE = (UndoResolver.undo_remove_grade, UndoResolver.undo_add_grade)

    UPDATE_STUDENT = (UndoResolver.undo_update, UndoResolver.revert_undo_update)
    UPDATE_DISCIPLINE = (UndoResolver.undo_update, UndoResolver.revert_undo_update)

