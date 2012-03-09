"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.708625.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.activity.experiment_relationship_target import ExperimentRelationshipTarget
from cim.v1_5.types.activity.experiment_relationship_type import ExperimentRelationshipType
from cim.v1_5.types.shared.cim_relationship import CimRelationship


# Module exports.
__all__ = ['ExperimentRelationship']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.708625$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class ExperimentRelationship(CimRelationship):
    """A class within the cim v1.5 type system.

    Contains a set of relationship types specific to a experiment document that can be used to describe its genealogy.
    """
    def __init__(self):
        """Constructor"""
        super(ExperimentRelationship, self).__init__()

        self.__target = activity.experiment_relationship_target()   # type = activity.ExperimentRelationshipTarget
        self.__type = activity.experiment_relationship_type()       # type = activity.ExperimentRelationshipType


    @property
    def target(self):
        """Gets value of experiment relationship target property."""
        return self.__target

    @target.setter
    def target(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, ExperimentRelationshipTarget):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of experiment relationship target property."""
        self.__target = value

    @target.deleter
    def target(self, value):
        """Deletes experiment relationship target property."""
        raise TypeError("Cannot delete experiment relationship target property.")


    @property
    def type(self):
        """Gets value of experiment relationship type property."""
        return self.__type

    @type.setter
    def type(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, ExperimentRelationshipType):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of experiment relationship type property."""
        self.__type = value

    @type.deleter
    def type(self, value):
        """Deletes experiment relationship type property."""
        raise TypeError("Cannot delete experiment relationship type property.")



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
        d = dict(super(ExperimentRelationship, self).as_dict())
        append(d, 'target', self.__target, False, False, False)
        append(d, 'type', self.__type, False, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = ExperimentRelationship()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('activity.ExperimentRelationship', e)
