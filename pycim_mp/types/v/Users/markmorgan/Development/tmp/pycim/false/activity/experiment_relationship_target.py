"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.709840.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.activity.numerical_experiment import NumericalExperiment
from cim.v1_5.types.shared.cim_reference import CimReference


# Module exports.
__all__ = ['ExperimentRelationshipTarget']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.709840$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class ExperimentRelationshipTarget(object):
    """A class within the cim v1.5 type system.

    
    """
    def __init__(self):
        """Constructor"""
        super(ExperimentRelationshipTarget, self).__init__()

        self.__numerical_experiment = None                          # type = activity.NumericalExperiment
        self.__reference = None                                     # type = shared.CimReference


    @property
    def numerical_experiment(self):
        """Gets value of {class-name} numerical_experiment property."""
        return self.__numerical_experiment

    @numerical_experiment.setter
    def numerical_experiment(self, value):
        if value is not None and not isinstance(value, NumericalExperiment):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} numerical_experiment property."""
        self.__numerical_experiment = value

    @numerical_experiment.deleter
    def numerical_experiment(self, value):
        """Deletes {class-name} numerical_experiment property."""
        raise TypeError("Cannot delete {class-name} numerical_experiment property.")


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
        append(d, 'numerical_experiment', self.__numerical_experiment, False, False, False)
        append(d, 'reference', self.__reference, False, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = ExperimentRelationshipTarget()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('activity.ExperimentRelationshipTarget', e)
