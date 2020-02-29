class UndoException(Exception):
    pass


class UndoOperation:
    def __init__(self, caller, undo_handler, redo_handler, parameters):
        self.__caller = caller
        self.__undo_handler = undo_handler
        self.__redo_handler = redo_handler
        self.__parameters = parameters

        # print('Added op with params {}'.format(self.__parameters))

    def __call__(self, undo=True):
        if undo:
            self.__undo_handler(self.__caller, *self.__parameters)
        else:
            self.__redo_handler(self.__caller, *self.__parameters)


class UndoManager:
    __undo_list = []
    __redo_list = []

    __temporary_undo_list = []
    __temporary_redo_list = []

    @staticmethod
    def add_undo_operation(caller, handler, *parameters):
        UndoManager.__temporary_undo_list.append(
            UndoOperation(caller, handler[0], handler[1], parameters)
        )
        # cut off the redo branch, since it's no longer reachable
        UndoManager.__redo_list = []

    @staticmethod
    def flush_operations():
        # Save all the operations as one big operation, to be undone at the same time
        if len(UndoManager.__temporary_undo_list) is not 0:
            UndoManager.__undo_list.append(UndoManager.__temporary_undo_list)
            UndoManager.__temporary_undo_list = []

        if len(UndoManager.__temporary_redo_list) is not 0:
            UndoManager.__redo_list.append(UndoManager.__temporary_redo_list)
            UndoManager.__temporary_redo_list = []

    @staticmethod
    def undo():
        # Get the last batch of operations and undo all of them
        if len(UndoManager.__undo_list) is 0:
            raise UndoException('Cannot undo any further')

        operations = UndoManager.__undo_list.pop()
        # print('Undoing {} operations'.format(len(operations)))
        for operation in operations:
            UndoManager.__temporary_redo_list.append(operation)
            operation(undo=True)

        UndoManager.flush_operations()

    @staticmethod
    def redo():
        if len(UndoManager.__redo_list) is 0:
            raise UndoException('Cannot redo any further')

        operations = UndoManager.__redo_list.pop()
        # print('Redoing {} operations'.format(len(operations)))
        for operation in operations:
            UndoManager.__temporary_undo_list.append(operation)
            operation(undo=False)

        UndoManager.flush_operations()