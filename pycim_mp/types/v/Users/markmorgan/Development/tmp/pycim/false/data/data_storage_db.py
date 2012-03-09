"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.731266.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.data.data_storage import DataStorage


# Module exports.
__all__ = ['DataStorageDb']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.731266$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class DataStorageDb(DataStorage):
    """A class within the cim v1.5 type system.

    Contains attributes to describe a DataObject stored as a database file.
    """
    def __init__(self):
        """Constructor"""
        super(DataStorageDb, self).__init__()

        self.__access_string = None                                 # type = str
        self.__name = None                                          # type = str
        self.__owner = None                                         # type = str
        self.__table = None                                         # type = str


    @property
    def access_string(self):
        """Gets value of {class-name} access_string property."""
        return self.__access_string

    @access_string.setter
    def access_string(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} access_string property."""
        self.__access_string = value

    @access_string.deleter
    def access_string(self, value):
        """Deletes {class-name} access_string property."""
        raise TypeError("Cannot delete {class-name} access_string property.")


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
    def owner(self):
        """Gets value of {class-name} owner property."""
        return self.__owner

    @owner.setter
    def owner(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} owner property."""
        self.__owner = value

    @owner.deleter
    def owner(self, value):
        """Deletes {class-name} owner property."""
        raise TypeError("Cannot delete {class-name} owner property.")


    @property
    def table(self):
        """Gets value of {class-name} table property."""
        return self.__table

    @table.setter
    def table(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} table property."""
        self.__table = value

    @table.deleter
    def table(self, value):
        """Deletes {class-name} table property."""
        raise TypeError("Cannot delete {class-name} table property.")



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
        d = dict(super(DataStorageDb, self).as_dict())
        append(d, 'access_string', self.__access_string, False, True, False)
        append(d, 'name', self.__name, False, True, False)
        append(d, 'owner', self.__owner, False, True, False)
        append(d, 'table', self.__table, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = DataStorageDb()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('data.DataStorageDb', e)
