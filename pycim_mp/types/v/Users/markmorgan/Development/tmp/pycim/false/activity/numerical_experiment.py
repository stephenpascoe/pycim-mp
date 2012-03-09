"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.712280.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.shared.cim_info import CimInfo


# Module exports.
__all__ = ['NumericalExperiment']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.712280$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class NumericalExperiment(object):
    """A class within the cim v1.5 type system.

    A numerical experiment may be generated by an experiment, in which case it is inSupportOf the experiment. But a numerical experiment may also exist as an activity in its own right (as it might be if it were needed for a MIP). Examples: AR4 individual experiments, AR5 individual experiments, RAPID THC experiments etc.
    """
    def __init__(self):
        """Constructor"""
        super(NumericalExperiment, self).__init__()

        self.__cim_info = shared.cim_info()                         # type = shared.CimInfo
        self.__description = None                                   # type = str
        self.__experiment_id = None                                 # type = str
        self.__long_name = None                                     # type = str
        self.__short_name = str()                                   # type = str


    @property
    def cim_info(self):
        """Gets value of numerical experiment cim_info property."""
        return self.__cim_info

    @cim_info.setter
    def cim_info(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, CimInfo):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of numerical experiment cim_info property."""
        self.__cim_info = value

    @cim_info.deleter
    def cim_info(self, value):
        """Deletes numerical experiment cim_info property."""
        raise TypeError("Cannot delete numerical experiment cim_info property.")


    @property
    def description(self):
        """Gets value of {class-name} description property.

        A free-text description of the experiment."""
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


    @property
    def experiment_id(self):
        """Gets value of {class-name} experiment_id property.

        An experiment ID takes the form <number>.<number>[-<letter>]."""
        return self.__experiment_id

    @experiment_id.setter
    def experiment_id(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} experiment_id property."""
        self.__experiment_id = value

    @experiment_id.deleter
    def experiment_id(self, value):
        """Deletes {class-name} experiment_id property."""
        raise TypeError("Cannot delete {class-name} experiment_id property.")


    @property
    def long_name(self):
        """Gets value of {class-name} long_name property.

        The name of the experiment (that is recognized externally)."""
        return self.__long_name

    @long_name.setter
    def long_name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} long_name property."""
        self.__long_name = value

    @long_name.deleter
    def long_name(self, value):
        """Deletes {class-name} long_name property."""
        raise TypeError("Cannot delete {class-name} long_name property.")


    @property
    def short_name(self):
        """Gets value of numerical experiment short_name property.

        The name of the experiment (that is used internally)."""
        return self.__short_name

    @short_name.setter
    def short_name(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of numerical experiment short_name property."""
        self.__short_name = value

    @short_name.deleter
    def short_name(self, value):
        """Deletes numerical experiment short_name property."""
        raise TypeError("Cannot delete numerical experiment short_name property.")



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
        append(d, 'cim_info', self.__cim_info, False, False, False)
        append(d, 'description', self.__description, False, True, False)
        append(d, 'experiment_id', self.__experiment_id, False, True, False)
        append(d, 'long_name', self.__long_name, False, True, False)
        append(d, 'short_name', self.__short_name, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = NumericalExperiment()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('activity.NumericalExperiment', e)
