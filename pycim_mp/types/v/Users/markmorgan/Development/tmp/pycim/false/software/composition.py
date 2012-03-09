"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.760875.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid



# Module exports.
__all__ = ['Composition']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.760875$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Composition(object):
    """A class within the cim v1.5 type system.

    The set of Couplings used by a Component. Couplings can only occur between child components. That is, a composition must belong to an ancestor component of the components whose fields are being connected.
    """
    def __init__(self):
        """Constructor"""
        super(Composition, self).__init__()

        self.__couplings = []                                       # type = str
        self.__description = None                                   # type = str


    @property
    def couplings(self):
        """Gets value of {class-name} couplings property."""
        return list(self.__couplings)

    @couplings.setter
    def couplings(self, value):
        """Sets value of {class-name} couplings property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__couplings = []
        for i in value:
            self.append_to_couplings(i)

    @couplings.deleter
    def couplings(self, value):
        """Deletes {class-name} couplings property."""
        raise TypeError("Cannot delete {class-name} couplings property.")

    def append_to_couplings(self, item):
        """Appends an item to the managed {class-name} couplings collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__couplings.append(item)

    def remove_from_couplings(self, item):
        """Removes an item from the managed {class-name} couplings collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__couplings.remove(item)


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
        append(d, 'couplings', self.__couplings, True, True, False)
        append(d, 'description', self.__description, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = Composition()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('software.Composition', e)
