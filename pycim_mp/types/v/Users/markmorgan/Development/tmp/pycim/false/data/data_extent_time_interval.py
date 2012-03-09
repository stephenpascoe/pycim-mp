"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.720705.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid



# Module exports.
__all__ = ['DataExtentTimeInterval']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.720705$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class DataExtentTimeInterval(object):
    """A class within the cim v1.5 type system.

    A data object temporal extent represents the temporal coverage associated with a data object.
    """
    def __init__(self):
        """Constructor"""
        super(DataExtentTimeInterval, self).__init__()

        self.__factor = None                                        # type = int
        self.__radix = None                                         # type = int
        self.__unit = None                                          # type = str


    @property
    def factor(self):
        """Gets value of {class-name} factor property."""
        return self.__factor

    @factor.setter
    def factor(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} factor property."""
        self.__factor = value

    @factor.deleter
    def factor(self, value):
        """Deletes {class-name} factor property."""
        raise TypeError("Cannot delete {class-name} factor property.")


    @property
    def radix(self):
        """Gets value of {class-name} radix property."""
        return self.__radix

    @radix.setter
    def radix(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} radix property."""
        self.__radix = value

    @radix.deleter
    def radix(self, value):
        """Deletes {class-name} radix property."""
        raise TypeError("Cannot delete {class-name} radix property.")


    @property
    def unit(self):
        """Gets value of {class-name} unit property."""
        return self.__unit

    @unit.setter
    def unit(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} unit property."""
        self.__unit = value

    @unit.deleter
    def unit(self, value):
        """Deletes {class-name} unit property."""
        raise TypeError("Cannot delete {class-name} unit property.")



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
        append(d, 'factor', self.__factor, False, True, False)
        append(d, 'radix', self.__radix, False, True, False)
        append(d, 'unit', self.__unit, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = DataExtentTimeInterval()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('data.DataExtentTimeInterval', e)
