"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.776859.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.software.timing_units import TimingUnits


# Module exports.
__all__ = ['Timing']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.776859$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Timing(object):
    """A class within the cim v1.5 type system.

    Provides information about the rate of couplings and connections and/or the timing characteristics of individual components - for example, the start and stop times that the component was run for or the units of time that a component is able to model (in a single timestep).
    """
    def __init__(self):
        """Constructor"""
        super(Timing, self).__init__()

        self.__end = None                                           # type = datetime.datetime
        self.__rate = None                                          # type = int
        self.__start = None                                         # type = datetime.datetime
        self.__units = None                                         # type = software.TimingUnits
        self.__variable_rate = None                                 # type = bool


    @property
    def end(self):
        """Gets value of {class-name} end property."""
        return self.__end

    @end.setter
    def end(self, value):
        if value is not None and not isinstance(value, datetime.datetime):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} end property."""
        self.__end = value

    @end.deleter
    def end(self, value):
        """Deletes {class-name} end property."""
        raise TypeError("Cannot delete {class-name} end property.")


    @property
    def rate(self):
        """Gets value of {class-name} rate property."""
        return self.__rate

    @rate.setter
    def rate(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} rate property."""
        self.__rate = value

    @rate.deleter
    def rate(self, value):
        """Deletes {class-name} rate property."""
        raise TypeError("Cannot delete {class-name} rate property.")


    @property
    def start(self):
        """Gets value of {class-name} start property."""
        return self.__start

    @start.setter
    def start(self, value):
        if value is not None and not isinstance(value, datetime.datetime):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} start property."""
        self.__start = value

    @start.deleter
    def start(self, value):
        """Deletes {class-name} start property."""
        raise TypeError("Cannot delete {class-name} start property.")


    @property
    def units(self):
        """Gets value of {class-name} units property."""
        return self.__units

    @units.setter
    def units(self, value):
        if value is not None and not isinstance(value, TimingUnits):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} units property."""
        self.__units = value

    @units.deleter
    def units(self, value):
        """Deletes {class-name} units property."""
        raise TypeError("Cannot delete {class-name} units property.")


    @property
    def variable_rate(self):
        """Gets value of {class-name} variable_rate property.

        Describes whether or not the model supports a variable timestep. If set to true, then rate should not be specified."""
        return self.__variable_rate

    @variable_rate.setter
    def variable_rate(self, value):
        if value is not None and not isinstance(value, bool):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} variable_rate property."""
        self.__variable_rate = value

    @variable_rate.deleter
    def variable_rate(self, value):
        """Deletes {class-name} variable_rate property."""
        raise TypeError("Cannot delete {class-name} variable_rate property.")



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
        append(d, 'end', self.__end, False, True, False)
        append(d, 'rate', self.__rate, False, True, False)
        append(d, 'start', self.__start, False, True, False)
        append(d, 'units', self.__units, False, False, False)
        append(d, 'variable_rate', self.__variable_rate, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = Timing()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('software.Timing', e)
