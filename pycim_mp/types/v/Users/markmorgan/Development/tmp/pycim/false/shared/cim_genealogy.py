"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.736923.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.shared.cim_relationship import CimRelationship


# Module exports.
__all__ = ['CimGenealogy']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.736923$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class CimGenealogy(object):
    """A class within the cim v1.5 type system.

    A record of a document's history. A genealogy element contains a textual description and a set of relationships. Each relationship has a type and a reference to some target. There are different relationships for different document types.
    """
    def __init__(self):
        """Constructor"""
        super(CimGenealogy, self).__init__()

        self.__relationships = []                                   # type = shared.CimRelationship


    @property
    def relationships(self):
        """Gets value of {class-name} relationships property."""
        return list(self.__relationships)

    @relationships.setter
    def relationships(self, value):
        """Sets value of {class-name} relationships property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__relationships = []
        for i in value:
            self.append_to_relationships(i)

    @relationships.deleter
    def relationships(self, value):
        """Deletes {class-name} relationships property."""
        raise TypeError("Cannot delete {class-name} relationships property.")

    def append_to_relationships(self, item):
        """Appends an item to the managed {class-name} relationships collection."""
        if not isinstance(item, CimRelationship):
            raise TypeError("item is of incorrect type.")
        self.__relationships.append(item)

    def remove_from_relationships(self, item):
        """Removes an item from the managed {class-name} relationships collection."""
        if not isinstance(item, CimRelationship):
            raise TypeError("item is of incorrect type.")
        self.__relationships.remove(item)



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
        append(d, 'relationships', self.__relationships, True, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = CimGenealogy()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('shared.CimGenealogy', e)
