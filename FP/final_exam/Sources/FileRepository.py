from Repository.Repository import Repository


class FileRepository(Repository):
    def __init__(self, file_name, contained_class):
        super().__init__()
        self.__file_name = file_name
        self.__contained_class = contained_class

        self.__read_file()

    def add(self, object):
        super().add(object)
        self.__flush_to_file()

    def remove(self, id):
        super().remove(id)
        self.__flush_to_file()

    def __flush_to_file(self):
        contents = super().get_all()

        with open(self.__file_name, 'w') as file:
            for object in contents:
                file.write(object.save_format())

    def __read_file(self):
        with open(self.__file_name, 'r') as file:
            for line in file:
                args = line.split(',')
                object = self.__contained_class.from_line(*args)
                super().add(object)

