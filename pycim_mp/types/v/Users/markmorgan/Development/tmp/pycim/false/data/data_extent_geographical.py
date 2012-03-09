"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.718517.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid



# Module exports.
__all__ = ['DataExtentGeographical']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.718517$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class DataExtentGeographical(object):
    """A class within the cim v1.5 type system.

    A data object geographical extent represents the geographical coverage associated with a data object.
    """
    def __init__(self):
        """Constructor"""
        super(DataExtentGeographical, self).__init__()

        self.__east = None                                          # type = float
        self.__north = None                                         # type = float
        self.__south = None                                         # type = float
        self.__west = None                                          # type = float


    @property
    def east(self):
        """Gets value of {class-name} east property."""
        return self.__east

    @east.setter
    def east(self, value):
        if value is not None and not isinstance(value, float):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} east property."""
        self.__east = value

    @east.deleter
    def east(self, value):
        """Deletes {class-name} east property."""
        raise TypeError("Cannot delete {class-name} east property.")


    @property
    def north(self):
        """Gets value of {class-name} north property."""
        return self.__north

    @north.setter
    def north(self, value):
        if value is not None and not isinstance(value, float):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} north property."""
        self.__north = value

    @north.deleter
    def north(self, value):
        """Deletes {class-name} north property."""
        raise TypeError("Cannot delete {class-name} north property.")


    @property
    def south(self):
        """Gets value of {class-name} south property."""
        return self.__south

    @south.setter
    def south(self, value):
        if value is not None and not isinstance(value, float):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} south property."""
        self.__south = value

    @south.deleter
    def south(self, value):
        """Deletes {class-name} south property."""
        raise TypeError("Cannot delete {class-name} south property.")


    @property
    def west(self):
        """Gets value of {class-name} west property."""
        return self.__west

    @west.setter
    def west(self, value):
        if value is not None and not isinstance(value, float):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} west property."""
        self.__west = value

    @west.deleter
    def west(self, value):
        """Deletes {class-name} west property."""
        raise TypeError("Cannot delete {class-name} west property.")



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
        append(d, 'east', self.__east, False, True, False)
        append(d, 'north', self.__north, False, True, False)
        append(d, 'south', self.__south, False, True, False)
        append(d, 'west', self.__west, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = DataExtentGeographical()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('data.DataExtentGeographical', e)
