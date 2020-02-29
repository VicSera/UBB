class IllegalUndo(Exception):
    """
    Exception for cases when the user tries to undo more than he's allowed to
    """
    pass