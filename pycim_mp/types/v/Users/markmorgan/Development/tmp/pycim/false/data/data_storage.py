"""An abstract class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.729948.
"""

# Module imports.
import abc
from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty
import datetime
import types
import uuid



# Module exports.
__all__ = ['DataStorage']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.729948$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class DataStorage(object):
    """An abstract class within the cim v1.5 type system.

    Describes the method that the DataObject is stored. An abstract class with specific child classes for each supported method.
    """
    # Abstract Base Class module - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def __init__(self):
        """Constructor"""
        super(DataStorage, self).__init__()

        self.__format = None                                        # type = str
        self.__location = None                                      # type = str
        self.__modification_date = None                             # type = datetime.datetime
        self.__size = None                                          # type = int


    @property
    def format(self):
        """Gets value of {class-name} format property."""
        return self.__format

    @format.setter
    def format(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} format property."""
        self.__format = value

    @format.deleter
    def format(self, value):
        """Deletes {class-name} format property."""
        raise TypeError("Cannot delete {class-name} format property.")


    @property
    def location(self):
        """Gets value of {class-name} location property."""
        return self.__location

    @location.setter
    def location(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} location property."""
        self.__location = value

    @location.deleter
    def location(self, value):
        """Deletes {class-name} location property."""
        raise TypeError("Cannot delete {class-name} location property.")


    @property
    def modification_date(self):
        """Gets value of {class-name} modification_date property."""
        return self.__modification_date

    @modification_date.setter
    def modification_date(self, value):
        if value is not None and not isinstance(value, datetime.datetime):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} modification_date property."""
        self.__modification_date = value

    @modification_date.deleter
    def modification_date(self, value):
        """Deletes {class-name} modification_date property."""
        raise TypeError("Cannot delete {class-name} modification_date property.")


    @property
    def size(self):
        """Gets value of {class-name} size property."""
        return self.__size

    @size.setter
    def size(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} size property."""
        self.__size = value

    @size.deleter
    def size(self, value):
        """Deletes {class-name} size property."""
        raise TypeError("Cannot delete {class-name} size property.")



    def as_dict(self):
        """Gets dictionary representation of self used to create other representations such as json, xml ...etc.

        """
        def append(d, key, value, is_iterative, is_primitive, is_enum):
            if value is None:
                if is_iterative:
                    value = []
            elif is_primitive == False and is_enum == False:
                if is_iterative:
                    value = map(lambda i : i.as_dict(), value)
                else:
                    value = value.as_dict()
            d[key] = value

        # Populate a deep dictionary.
        d = dict()
        append(d, 'format', self.__format, False, True, False)
        append(d, 'location', self.__location, False, True, False)
        append(d, 'modification_date', self.__modification_date, False, True, False)
        append(d, 'size', self.__size, False, True, False)
        return d





