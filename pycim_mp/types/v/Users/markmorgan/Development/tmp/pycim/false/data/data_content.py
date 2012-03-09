"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.715462.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.data.data_topic import DataTopic
from cim.v1_5.types.shared.data_source import DataSource


# Module exports.
__all__ = ['DataContent']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.715462$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class DataContent(DataSource):
    """A class within the cim v1.5 type system.

    The contents of the data object; like ISO: MD_ContentInformation.
    """
    def __init__(self):
        """Constructor"""
        super(DataContent, self).__init__()

        self.__aggregation = None                                   # type = str
        self.__frequency = None                                     # type = str
        self.__topic = data.data_topic()                            # type = data.DataTopic


    @property
    def aggregation(self):
        """Gets value of {class-name} aggregation property.

        Describes how the content has been aggregated together: sum, min, mean, max, ..."""
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} aggregation property."""
        self.__aggregation = value

    @aggregation.deleter
    def aggregation(self, value):
        """Deletes {class-name} aggregation property."""
        raise TypeError("Cannot delete {class-name} aggregation property.")


    @property
    def frequency(self):
        """Gets value of {class-name} frequency property.

        Describes the frequency of the data content: daily, hourly, ..."""
        return self.__frequency

    @frequency.setter
    def frequency(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} frequency property."""
        self.__frequency = value

    @frequency.deleter
    def frequency(self, value):
        """Deletes {class-name} frequency property."""
        raise TypeError("Cannot delete {class-name} frequency property.")


    @property
    def topic(self):
        """Gets value of data content topic property."""
        return self.__topic

    @topic.setter
    def topic(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, DataTopic):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of data content topic property."""
        self.__topic = value

    @topic.deleter
    def topic(self, value):
        """Deletes data content topic property."""
        raise TypeError("Cannot delete data content topic property.")



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
        d = dict(super(DataContent, self).as_dict())
        append(d, 'aggregation', self.__aggregation, False, True, False)
        append(d, 'frequency', self.__frequency, False, True, False)
        append(d, 'topic', self.__topic, False, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = DataContent()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('data.DataContent', e)
