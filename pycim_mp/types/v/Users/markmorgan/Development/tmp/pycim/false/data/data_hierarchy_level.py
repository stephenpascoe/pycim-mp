"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.721843.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.data.data_hierarchy_type import DataHierarchyType


# Module exports.
__all__ = ['DataHierarchyLevel']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.721843$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class DataHierarchyLevel(object):
    """A class within the cim v1.5 type system.

    The type of data object that is grouped together into a particular hierarchy.  Currently, this is made up of terms describing how the Met Office splits up archived data and how THREDDS categorises variables.
    """
    def __init__(self):
        """Constructor"""
        super(DataHierarchyLevel, self).__init__()

        self.__is_open = None                                       # type = bool
        self.__name = None                                          # type = data.DataHierarchyType
        self.__value = None                                         # type = str


    @property
    def is_open(self):
        """Gets value of {class-name} is_open property."""
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if value is not None and not isinstance(value, bool):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} is_open property."""
        self.__is_open = value

    @is_open.deleter
    def is_open(self, value):
        """Deletes {class-name} is_open property."""
        raise TypeError("Cannot delete {class-name} is_open property.")


    @property
    def name(self):
        """Gets value of {class-name} name property.

        What level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject."""
        return self.__name

    @name.setter
    def name(self, value):
        if value is not None and not isinstance(value, DataHierarchyType):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} name property."""
        self.__name = value

    @name.deleter
    def name(self, value):
        """Deletes {class-name} name property."""
        raise TypeError("Cannot delete {class-name} name property.")


    @property
    def value(self):
        """Gets value of {class-name} value property.

        What is the name of the specific HierarchyLevel this DataObject is being organised at (ie: if the HierarchyLevel is "run" then the name might be the runid)."""
        return self.__value

    @value.setter
    def value(self, value):
        if value is not None and not isinstance(value, str):
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
        append(d, 'is_open', self.__is_open, False, True, False)
        append(d, 'name', self.__name, False, False, False)
        append(d, 'value', self.__value, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = DataHierarchyLevel()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('data.DataHierarchyLevel', e)
