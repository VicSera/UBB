from Modules.Repositories.FileRepository import FileRepository
from Modules.Services.StudentService import StudentService
from Modules.UI.ConsoleUI import ConsoleUI

student_repository = FileRepository('students.txt')
student_service = StudentService(student_repository)

ui = ConsoleUI(student_service)