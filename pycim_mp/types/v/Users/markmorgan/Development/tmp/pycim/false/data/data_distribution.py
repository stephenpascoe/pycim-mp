"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.716703.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.shared.responsible_party import ResponsibleParty


# Module exports.
__all__ = ['DataDistribution']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.716703$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class DataDistribution(object):
    """A class within the cim v1.5 type system.

    Describes how a DataObject is distributed.
    """
    def __init__(self):
        """Constructor"""
        super(DataDistribution, self).__init__()

        self.__access = None                                        # type = str
        self.__fee = None                                           # type = str
        self.__format = None                                        # type = str
        self.__responsible_party = None                             # type = shared.ResponsibleParty


    @property
    def access(self):
        """Gets value of {class-name} access property."""
        return self.__access

    @access.setter
    def access(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} access property."""
        self.__access = value

    @access.deleter
    def access(self, value):
        """Deletes {class-name} access property."""
        raise TypeError("Cannot delete {class-name} access property.")


    @property
    def fee(self):
        """Gets value of {class-name} fee property."""
        return self.__fee

    @fee.setter
    def fee(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} fee property."""
        self.__fee = value

    @fee.deleter
    def fee(self, value):
        """Deletes {class-name} fee property."""
        raise TypeError("Cannot delete {class-name} fee property.")


    @property
    def format(self):
        """Gets value of {class-name} format property."""
        return self.__format

    @format.setter
    def format(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} format property."""
        self.__format = value

    @format.deleter
    def format(self, value):
        """Deletes {class-name} format property."""
        raise TypeError("Cannot delete {class-name} format property.")


    @property
    def responsible_party(self):
        """Gets value of {class-name} responsible_party property."""
        return self.__responsible_party

    @responsible_party.setter
    def responsible_party(self, value):
        if value is not None and not isinstance(value, ResponsibleParty):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} responsible_party property."""
        self.__responsible_party = value

    @responsible_party.deleter
    def responsible_party(self, value):
        """Deletes {class-name} responsible_party property."""
        raise TypeError("Cannot delete {class-name} responsible_party property.")



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
        append(d, 'access', self.__access, False, True, False)
        append(d, 'fee', self.__fee, False, True, False)
        append(d, 'format', self.__format, False, True, False)
        append(d, 'responsible_party', self.__responsible_party, False, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = DataDistribution()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('data.DataDistribution', e)
