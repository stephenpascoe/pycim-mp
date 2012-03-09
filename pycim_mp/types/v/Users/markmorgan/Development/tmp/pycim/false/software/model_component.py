"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.766595.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.shared.cim_info import CimInfo
from cim.v1_5.types.software.model_component_type import ModelComponentType
from cim.v1_5.types.software.software_component import SoftwareComponent
from cim.v1_5.types.software.timing import Timing


# Module exports.
__all__ = ['ModelComponent']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.766595$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class ModelComponent(SoftwareComponent):
    """A class within the cim v1.5 type system.

    A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.
    """
    def __init__(self):
        """Constructor"""
        super(ModelComponent, self).__init__()

        self.__activity = None                                      # type = str
        self.__cim_info = shared.cim_info()                         # type = shared.CimInfo
        self.__timing = None                                        # type = software.Timing
        self.__types = []                                           # type = software.ModelComponentType


    @property
    def activity(self):
        """Gets value of {class-name} activity property."""
        return self.__activity

    @activity.setter
    def activity(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} activity property."""
        self.__activity = value

    @activity.deleter
    def activity(self, value):
        """Deletes {class-name} activity property."""
        raise TypeError("Cannot delete {class-name} activity property.")


    @property
    def cim_info(self):
        """Gets value of model component cim_info property."""
        return self.__cim_info

    @cim_info.setter
    def cim_info(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, CimInfo):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of model component cim_info property."""
        self.__cim_info = value

    @cim_info.deleter
    def cim_info(self, value):
        """Deletes model component cim_info property."""
        raise TypeError("Cannot delete model component cim_info property.")


    @property
    def timing(self):
        """Gets value of {class-name} timing property.

        Describes information about how this component simulates time."""
        return self.__timing

    @timing.setter
    def timing(self, value):
        if value is not None and not isinstance(value, Timing):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} timing property."""
        self.__timing = value

    @timing.deleter
    def timing(self, value):
        """Deletes {class-name} timing property."""
        raise TypeError("Cannot delete {class-name} timing property.")


    @property
    def types(self):
        """Gets value of {class-name} types property.

        Describes the type of component. There can be multiple types."""
        return list(self.__types)

    @types.setter
    def types(self, value):
        """Sets value of {class-name} types property.

        Describes the type of component. There can be multiple types."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__types = []
        for i in value:
            self.append_to_types(i)

    @types.deleter
    def types(self, value):
        """Deletes {class-name} types property."""
        raise TypeError("Cannot delete {class-name} types property.")

    def append_to_types(self, item):
        """Appends an item to the managed {class-name} types collection."""
        if not isinstance(item, ModelComponentType):
            raise TypeError("item is of incorrect type.")
        self.__types.append(item)

    def remove_from_types(self, item):
        """Removes an item from the managed {class-name} types collection."""
        if not isinstance(item, ModelComponentType):
            raise TypeError("item is of incorrect type.")
        self.__types.remove(item)



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
        d = dict(super(ModelComponent, self).as_dict())
        append(d, 'activity', self.__activity, False, True, False)
        append(d, 'cim_info', self.__cim_info, False, False, False)
        append(d, 'timing', self.__timing, False, False, False)
        append(d, 'types', self.__types, True, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = ModelComponent()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('software.ModelComponent', e)
