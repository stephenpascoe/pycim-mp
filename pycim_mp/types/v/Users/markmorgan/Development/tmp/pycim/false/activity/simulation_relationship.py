"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.713527.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.activity.simulation_relationship_target import SimulationRelationshipTarget
from cim.v1_5.types.activity.simulation_relationship_type import SimulationRelationshipType
from cim.v1_5.types.shared.cim_relationship import CimRelationship


# Module exports.
__all__ = ['SimulationRelationship']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.713527$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class SimulationRelationship(CimRelationship):
    """A class within the cim v1.5 type system.

    Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.
    """
    def __init__(self):
        """Constructor"""
        super(SimulationRelationship, self).__init__()

        self.__target = activity.simulation_relationship_target()   # type = activity.SimulationRelationshipTarget
        self.__type = activity.simulation_relationship_type()       # type = activity.SimulationRelationshipType


    @property
    def target(self):
        """Gets value of simulation relationship target property."""
        return self.__target

    @target.setter
    def target(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, SimulationRelationshipTarget):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of simulation relationship target property."""
        self.__target = value

    @target.deleter
    def target(self, value):
        """Deletes simulation relationship target property."""
        raise TypeError("Cannot delete simulation relationship target property.")


    @property
    def type(self):
        """Gets value of simulation relationship type property."""
        return self.__type

    @type.setter
    def type(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, SimulationRelationshipType):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of simulation relationship type property."""
        self.__type = value

    @type.deleter
    def type(self, value):
        """Deletes simulation relationship type property."""
        raise TypeError("Cannot delete simulation relationship type property.")



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
        d = dict(super(SimulationRelationship, self).as_dict())
        append(d, 'target', self.__target, False, False, False)
        append(d, 'type', self.__type, False, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = SimulationRelationship()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('activity.SimulationRelationship', e)
