"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.735362.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.shared.cim_document_relationship_target import CimDocumentRelationshipTarget
from cim.v1_5.types.shared.cim_document_relationship_type import CimDocumentRelationshipType
from cim.v1_5.types.shared.cim_relationship import CimRelationship


# Module exports.
__all__ = ['CimDocumentRelationship']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.735362$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class CimDocumentRelationship(CimRelationship):
    """A class within the cim v1.5 type system.

    Contains the set of relationships supported by a Document.
    """
    def __init__(self):
        """Constructor"""
        super(CimDocumentRelationship, self).__init__()

        self.__target = shared.cim_document_relationship_target()   # type = shared.CimDocumentRelationshipTarget
        self.__type = shared.cim_document_relationship_type()       # type = shared.CimDocumentRelationshipType


    @property
    def target(self):
        """Gets value of cim document relationship target property."""
        return self.__target

    @target.setter
    def target(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, CimDocumentRelationshipTarget):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of cim document relationship target property."""
        self.__target = value

    @target.deleter
    def target(self, value):
        """Deletes cim document relationship target property."""
        raise TypeError("Cannot delete cim document relationship target property.")


    @property
    def type(self):
        """Gets value of cim document relationship type property."""
        return self.__type

    @type.setter
    def type(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, CimDocumentRelationshipType):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of cim document relationship type property."""
        self.__type = value

    @type.deleter
    def type(self, value):
        """Deletes cim document relationship type property."""
        raise TypeError("Cannot delete cim document relationship type property.")



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
        d = dict(super(CimDocumentRelationship, self).as_dict())
        append(d, 'target', self.__target, False, False, False)
        append(d, 'type', self.__type, False, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = CimDocumentRelationship()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('shared.CimDocumentRelationship', e)
