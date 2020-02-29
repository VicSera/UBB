import copy


class CustomList:
    def __init__(self):
        self.__contents = []

    @property
    def count(self):
        return len(self.__contents)

    def __str__(self):
        return "Custom: " + str(self.__contents)

    def __len__(self):
        return self.count

    def values(self):
        return self.__contents[:]

    def set_values(self, values):
        self.__contents = values

    def append(self, item):
        self.__contents.append(item)

    def remove(self, object_to_remove):
        for index, object in enumerate(self.__contents[:]):
            if object == object_to_remove:
                del self.__contents[index]
                return object

    def __setitem__(self, key, value):
        if type(key) != int:
            raise TypeError('CustomList index must be of type int')
        self.__contents[key] = value

    def __delitem__(self, key):
        self.__contents.pop(key)

    def __getitem__(self, index):
        return self.__contents[index]

    def __next__(self):
        if self.__current_index < len(self.__contents):
            self.__current_index += 1
            return self.__contents[self.__current_index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        self.__current_index = 0
        return self

    @staticmethod
    def sort(custom_list, comparison_function):
        if type(custom_list) is not CustomList:
            raise TypeError('CustomList.sort is only designed to work for the CustomList type')

        position = 0
        while position < custom_list.count:
            if position == 0 or comparison_function(custom_list[position - 1], custom_list[position]) == True:
                position += 1
            else:
                auxiliary_object = custom_list[position]
                custom_list[position] = custom_list[position - 1]
                custom_list[position - 1] = auxiliary_object
                position -= 1

    @staticmethod
    def filter(custom_list, acceptance_function):
        if type(custom_list) is not CustomList:
            raise TypeError('CustomList.filter is only designed to work for the CustomList type')

        new_list = []
        for object in custom_list:
            if acceptance_function(object) == True:
                new_list.append(object)
        custom_list.set_values(new_list)