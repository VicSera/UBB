import configparser


class Settings:
    REPOSITORY_TYPE = ''
    STUDENTS_FILE = ''
    DISCIPLINE_FILE = ''
    GRADES_FILE = ''

    @staticmethod
    def initialize():
        config = configparser.ConfigParser()
        config.read('settings.properties')

        Settings.REPOSITORY_TYPE = config.get('repository_config', 'repository')
        Settings.STUDENTS_FILE = config.get('repository_config', 'students')
        Settings.DISCIPLINE_FILE = config.get('repository_config', 'disciplines')
        Settings.GRADES_FILE = config.get('repository_config', 'grades')