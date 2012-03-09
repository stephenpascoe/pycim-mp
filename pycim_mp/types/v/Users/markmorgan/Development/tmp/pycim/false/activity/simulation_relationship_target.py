"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.714553.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.activity.simulation_type import SimulationType
from cim.v1_5.types.shared.cim_reference import CimReference


# Module exports.
__all__ = ['SimulationRelationshipTarget']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.714553$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class SimulationRelationshipTarget(object):
    """A class within the cim v1.5 type system.

    
    """
    def __init__(self):
        """Constructor"""
        super(SimulationRelationshipTarget, self).__init__()

        self.__reference = None                                     # type = shared.CimReference
        self.__target = None                                        # type = activity.SimulationType


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


    @property
    def target(self):
        """Gets value of {class-name} target property."""
        return self.__target

    @target.setter
    def target(self, value):
        if value is not None and not isinstance(value, SimulationType):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} target property."""
        self.__target = value

    @target.deleter
    def target(self, value):
        """Deletes {class-name} target property."""
        raise TypeError("Cannot delete {class-name} target property.")



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
        append(d, 'reference', self.__reference, False, False, False)
        append(d, 'target', self.__target, False, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = SimulationRelationshipTarget()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('activity.SimulationRelationshipTarget', e)
