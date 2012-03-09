"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.710930.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.activity.activity import Activity
from cim.v1_5.types.activity.experiment import Experiment


# Module exports.
__all__ = ['MeasurementCampaign']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.710930$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class MeasurementCampaign(Activity):
    """A class within the cim v1.5 type system.

    
    """
    def __init__(self):
        """Constructor"""
        super(MeasurementCampaign, self).__init__()

        self.__duration = int()                                     # type = int
        self.__experiments = []                                     # type = activity.Experiment


    @property
    def duration(self):
        """Gets value of measurement campaign duration property."""
        return self.__duration

    @duration.setter
    def duration(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, int):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of measurement campaign duration property."""
        self.__duration = value

    @duration.deleter
    def duration(self, value):
        """Deletes measurement campaign duration property."""
        raise TypeError("Cannot delete measurement campaign duration property.")


    @property
    def experiments(self):
        """Gets value of {class-name} experiments property."""
        return list(self.__experiments)

    @experiments.setter
    def experiments(self, value):
        """Sets value of {class-name} experiments property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__experiments = []
        for i in value:
            self.append_to_experiments(i)

    @experiments.deleter
    def experiments(self, value):
        """Deletes {class-name} experiments property."""
        raise TypeError("Cannot delete {class-name} experiments property.")

    def append_to_experiments(self, item):
        """Appends an item to the managed {class-name} experiments collection."""
        if not isinstance(item, Experiment):
            raise TypeError("item is of incorrect type.")
        self.__experiments.append(item)

    def remove_from_experiments(self, item):
        """Removes an item from the managed {class-name} experiments collection."""
        if not isinstance(item, Experiment):
            raise TypeError("item is of incorrect type.")
        self.__experiments.remove(item)



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
        d = dict(super(MeasurementCampaign, self).as_dict())
        append(d, 'duration', self.__duration, False, True, False)
        append(d, 'experiments', self.__experiments, True, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = MeasurementCampaign()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('activity.MeasurementCampaign', e)
