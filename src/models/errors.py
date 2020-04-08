
class Error(Exception):
    """
    Base class for exception in this module.
    """
    pass


class InvalidChildrenSizeError(ValueError):
    """
    Exception raised when the number of children is wrong.
    """
    pass
