"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.768023.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.software.rank import Rank


# Module exports.
__all__ = ['Parallelisation']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.768023$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Parallelisation(object):
    """A class within the cim v1.5 type system.

    Describes how a deployment has been parallelised across a computing platform.
    """
    def __init__(self):
        """Constructor"""
        super(Parallelisation, self).__init__()

        self.__processes = int()                                    # type = int
        self.__ranks = []                                           # type = software.Rank


    @property
    def processes(self):
        """Gets value of parallelisation processes property."""
        return self.__processes

    @processes.setter
    def processes(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, int):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of parallelisation processes property."""
        self.__processes = value

    @processes.deleter
    def processes(self, value):
        """Deletes parallelisation processes property."""
        raise TypeError("Cannot delete parallelisation processes property.")


    @property
    def ranks(self):
        """Gets value of {class-name} ranks property."""
        return list(self.__ranks)

    @ranks.setter
    def ranks(self, value):
        """Sets value of {class-name} ranks property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__ranks = []
        for i in value:
            self.append_to_ranks(i)

    @ranks.deleter
    def ranks(self, value):
        """Deletes {class-name} ranks property."""
        raise TypeError("Cannot delete {class-name} ranks property.")

    def append_to_ranks(self, item):
        """Appends an item to the managed {class-name} ranks collection."""
        if not isinstance(item, Rank):
            raise TypeError("item is of incorrect type.")
        self.__ranks.append(item)

    def remove_from_ranks(self, item):
        """Removes an item from the managed {class-name} ranks collection."""
        if not isinstance(item, Rank):
            raise TypeError("item is of incorrect type.")
        self.__ranks.remove(item)



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
        append(d, 'processes', self.__processes, False, True, False)
        append(d, 'ranks', self.__ranks, True, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = Parallelisation()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('software.Parallelisation', e)
