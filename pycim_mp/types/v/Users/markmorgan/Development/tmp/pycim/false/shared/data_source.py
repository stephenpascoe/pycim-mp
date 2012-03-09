"""An abstract class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.745747.
"""

# Module imports.
import abc
from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty
import datetime
import types
import uuid

from cim.v1_5.types.shared.data_purpose import DataPurpose


# Module exports.
__all__ = ['DataSource']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.745747$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class DataSource(object):
    """An abstract class within the cim v1.5 type system.

    A DataSource can be realised by either a DataObject (file), a DataContent (variable), a Component (model), or a ComponentProperty (variable); all of those can supply data.
    """
    # Abstract Base Class module - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def __init__(self):
        """Constructor"""
        super(DataSource, self).__init__()

        self.__purpose = None                                       # type = shared.DataPurpose


    @property
    def purpose(self):
        """Gets value of {class-name} purpose property."""
        return self.__purpose

    @purpose.setter
    def purpose(self, value):
        if value is not None and not isinstance(value, DataPurpose):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} purpose property."""
        self.__purpose = value

    @purpose.deleter
    def purpose(self, value):
        """Deletes {class-name} purpose property."""
        raise TypeError("Cannot delete {class-name} purpose property.")



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
        append(d, 'purpose', self.__purpose, False, False, False)
        return d





