"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.733320.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.data.data_storage import DataStorage


# Module exports.
__all__ = ['DataStorageIp']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.733320$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class DataStorageIp(DataStorage):
    """A class within the cim v1.5 type system.

    Contains attributes to describe a DataObject stored as a database file.
    """
    def __init__(self):
        """Constructor"""
        super(DataStorageIp, self).__init__()

        self.__file_name = None                                     # type = str
        self.__host = None                                          # type = str
        self.__path = None                                          # type = str
        self.__protocol = None                                      # type = str


    @property
    def file_name(self):
        """Gets value of {class-name} file_name property."""
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} file_name property."""
        self.__file_name = value

    @file_name.deleter
    def file_name(self, value):
        """Deletes {class-name} file_name property."""
        raise TypeError("Cannot delete {class-name} file_name property.")


    @property
    def host(self):
        """Gets value of {class-name} host property."""
        return self.__host

    @host.setter
    def host(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} host property."""
        self.__host = value

    @host.deleter
    def host(self, value):
        """Deletes {class-name} host property."""
        raise TypeError("Cannot delete {class-name} host property.")


    @property
    def path(self):
        """Gets value of {class-name} path property."""
        return self.__path

    @path.setter
    def path(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} path property."""
        self.__path = value

    @path.deleter
    def path(self, value):
        """Deletes {class-name} path property."""
        raise TypeError("Cannot delete {class-name} path property.")


    @property
    def protocol(self):
        """Gets value of {class-name} protocol property."""
        return self.__protocol

    @protocol.setter
    def protocol(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} protocol property."""
        self.__protocol = value

    @protocol.deleter
    def protocol(self, value):
        """Deletes {class-name} protocol property."""
        raise TypeError("Cannot delete {class-name} protocol property.")



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
        d = dict(super(DataStorageIp, self).as_dict())
        append(d, 'file_name', self.__file_name, False, True, False)
        append(d, 'host', self.__host, False, True, False)
        append(d, 'path', self.__path, False, True, False)
        append(d, 'protocol', self.__protocol, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = DataStorageIp()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('data.DataStorageIp', e)
