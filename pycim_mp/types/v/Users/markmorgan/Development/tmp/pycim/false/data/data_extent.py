"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.717623.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.data.data_extent_geographical import DataExtentGeographical
from cim.v1_5.types.data.data_extent_temporal import DataExtentTemporal


# Module exports.
__all__ = ['DataExtent']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.717623$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class DataExtent(object):
    """A class within the cim v1.5 type system.

    A data object extent represents the geographical and temporal coverage associated with a data object.
    """
    def __init__(self):
        """Constructor"""
        super(DataExtent, self).__init__()

        self.__geographical = data.data_extent_geographical()       # type = data.DataExtentGeographical
        self.__temporal = data.data_extent_temporal()               # type = data.DataExtentTemporal


    @property
    def geographical(self):
        """Gets value of data extent geographical property."""
        return self.__geographical

    @geographical.setter
    def geographical(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, DataExtentGeographical):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of data extent geographical property."""
        self.__geographical = value

    @geographical.deleter
    def geographical(self, value):
        """Deletes data extent geographical property."""
        raise TypeError("Cannot delete data extent geographical property.")


    @property
    def temporal(self):
        """Gets value of data extent temporal property."""
        return self.__temporal

    @temporal.setter
    def temporal(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, DataExtentTemporal):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of data extent temporal property."""
        self.__temporal = value

    @temporal.deleter
    def temporal(self, value):
        """Deletes data extent temporal property."""
        raise TypeError("Cannot delete data extent temporal property.")



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
        append(d, 'geographical', self.__geographical, False, False, False)
        append(d, 'temporal', self.__temporal, False, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = DataExtent()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('data.DataExtent', e)
