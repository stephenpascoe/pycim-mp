"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.769738.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid



# Module exports.
__all__ = ['Rank']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.769738$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Rank(object):
    """A class within the cim v1.5 type system.

    
    """
    def __init__(self):
        """Constructor"""
        super(Rank, self).__init__()

        self.__increment = None                                     # type = int
        self.__max = None                                           # type = int
        self.__min = None                                           # type = int
        self.__value = None                                         # type = int


    @property
    def increment(self):
        """Gets value of {class-name} increment property."""
        return self.__increment

    @increment.setter
    def increment(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} increment property."""
        self.__increment = value

    @increment.deleter
    def increment(self, value):
        """Deletes {class-name} increment property."""
        raise TypeError("Cannot delete {class-name} increment property.")


    @property
    def max(self):
        """Gets value of {class-name} max property."""
        return self.__max

    @max.setter
    def max(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} max property."""
        self.__max = value

    @max.deleter
    def max(self, value):
        """Deletes {class-name} max property."""
        raise TypeError("Cannot delete {class-name} max property.")


    @property
    def min(self):
        """Gets value of {class-name} min property."""
        return self.__min

    @min.setter
    def min(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} min property."""
        self.__min = value

    @min.deleter
    def min(self, value):
        """Deletes {class-name} min property."""
        raise TypeError("Cannot delete {class-name} min property.")


    @property
    def value(self):
        """Gets value of {class-name} value property."""
        return self.__value

    @value.setter
    def value(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} value property."""
        self.__value = value

    @value.deleter
    def value(self, value):
        """Deletes {class-name} value property."""
        raise TypeError("Cannot delete {class-name} value property.")



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
        append(d, 'increment', self.__increment, False, True, False)
        append(d, 'max', self.__max, False, True, False)
        append(d, 'min', self.__min, False, True, False)
        append(d, 'value', self.__value, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = Rank()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('software.Rank', e)
