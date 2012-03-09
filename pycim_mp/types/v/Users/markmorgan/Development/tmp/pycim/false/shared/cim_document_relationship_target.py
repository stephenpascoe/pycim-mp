"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.736201.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.shared.cim_document_type import CimDocumentType
from cim.v1_5.types.shared.cim_reference import CimReference


# Module exports.
__all__ = ['CimDocumentRelationshipTarget']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.736201$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class CimDocumentRelationshipTarget(object):
    """A class within the cim v1.5 type system.

    
    """
    def __init__(self):
        """Constructor"""
        super(CimDocumentRelationshipTarget, self).__init__()

        self.__document = None                                      # type = shared.CimDocumentType
        self.__reference = None                                     # type = shared.CimReference


    @property
    def document(self):
        """Gets value of {class-name} document property."""
        return self.__document

    @document.setter
    def document(self, value):
        if value is not None and not isinstance(value, CimDocumentType):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} document property."""
        self.__document = value

    @document.deleter
    def document(self, value):
        """Deletes {class-name} document property."""
        raise TypeError("Cannot delete {class-name} document property.")


    @property
    def reference(self):
        """Gets value of {class-name} reference property."""
        return self.__reference

    @reference.setter
    def reference(self, value):
        if value is not None and not isinstance(value, CimReference):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} reference property."""
        self.__reference = value

    @reference.deleter
    def reference(self, value):
        """Deletes {class-name} reference property."""
        raise TypeError("Cannot delete {class-name} reference property.")



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
        append(d, 'document', self.__document, False, False, False)
        append(d, 'reference', self.__reference, False, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = CimDocumentRelationshipTarget()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('shared.CimDocumentRelationshipTarget', e)
