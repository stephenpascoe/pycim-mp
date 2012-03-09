"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.719513.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.data.data_extent_time_interval import DataExtentTimeInterval


# Module exports.
__all__ = ['DataExtentTemporal']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.719513$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class DataExtentTemporal(object):
    """A class within the cim v1.5 type system.

    A data object temporal extent represents the temporal coverage associated with a data object.
    """
    def __init__(self):
        """Constructor"""
        super(DataExtentTemporal, self).__init__()

        self.__begin = None                                         # type = datetime.date
        self.__end = None                                           # type = datetime.date
        self.__time_interval = None                                 # type = data.DataExtentTimeInterval


    @property
    def begin(self):
        """Gets value of {class-name} begin property."""
        return self.__begin

    @begin.setter
    def begin(self, value):
        if value is not None and not isinstance(value, datetime.date):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} begin property."""
        self.__begin = value

    @begin.deleter
    def begin(self, value):
        """Deletes {class-name} begin property."""
        raise TypeError("Cannot delete {class-name} begin property.")


    @property
    def end(self):
        """Gets value of {class-name} end property."""
        return self.__end

    @end.setter
    def end(self, value):
        if value is not None and not isinstance(value, datetime.date):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} end property."""
        self.__end = value

    @end.deleter
    def end(self, value):
        """Deletes {class-name} end property."""
        raise TypeError("Cannot delete {class-name} end property.")


    @property
    def time_interval(self):
        """Gets value of {class-name} time_interval property."""
        return self.__time_interval

    @time_interval.setter
    def time_interval(self, value):
        if value is not None and not isinstance(value, DataExtentTimeInterval):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} time_interval property."""
        self.__time_interval = value

    @time_interval.deleter
    def time_interval(self, value):
        """Deletes {class-name} time_interval property."""
        raise TypeError("Cannot delete {class-name} time_interval property.")



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
        append(d, 'begin', self.__begin, False, True, False)
        append(d, 'end', self.__end, False, True, False)
        append(d, 'time_interval', self.__time_interval, False, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = DataExtentTemporal()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('data.DataExtentTemporal', e)
