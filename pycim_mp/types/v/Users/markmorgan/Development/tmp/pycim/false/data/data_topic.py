"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.734400.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid



# Module exports.
__all__ = ['DataTopic']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.734400$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class DataTopic(object):
    """A class within the cim v1.5 type system.

    Describes the content  of a data object; the variable's name, units, etc.
    """
    def __init__(self):
        """Constructor"""
        super(DataTopic, self).__init__()

        self.__description = None                                   # type = str
        self.__name = None                                          # type = str
        self.__unit = None                                          # type = str


    @property
    def description(self):
        """Gets value of {class-name} description property."""
        return self.__description

    @description.setter
    def description(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} description property."""
        self.__description = value

    @description.deleter
    def description(self, value):
        """Deletes {class-name} description property."""
        raise TypeError("Cannot delete {class-name} description property.")


    @property
    def name(self):
        """Gets value of {class-name} name property."""
        return self.__name

    @name.setter
    def name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} name property."""
        self.__name = value

    @name.deleter
    def name(self, value):
        """Deletes {class-name} name property."""
        raise TypeError("Cannot delete {class-name} name property.")


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
        append(d, 'description', self.__description, False, True, False)
        append(d, 'name', self.__name, False, True, False)
        append(d, 'unit', self.__unit, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = DataTopic()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('data.DataTopic', e)
