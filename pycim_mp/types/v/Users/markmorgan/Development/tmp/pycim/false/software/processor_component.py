"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.768827.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.shared.cim_info import CimInfo
from cim.v1_5.types.software.software_component import SoftwareComponent


# Module exports.
__all__ = ['ProcessorComponent']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.768827$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class ProcessorComponent(SoftwareComponent):
    """A class within the cim v1.5 type system.

    A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.
    """
    def __init__(self):
        """Constructor"""
        super(ProcessorComponent, self).__init__()

        self.__cim_info = shared.cim_info()                         # type = shared.CimInfo


    @property
    def cim_info(self):
        """Gets value of processor component cim_info property."""
        return self.__cim_info

    @cim_info.setter
    def cim_info(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, CimInfo):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of processor component cim_info property."""
        self.__cim_info = value

    @cim_info.deleter
    def cim_info(self, value):
        """Deletes processor component cim_info property."""
        raise TypeError("Cannot delete processor component cim_info property.")



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
        d = dict(super(ProcessorComponent, self).as_dict())
        append(d, 'cim_info', self.__cim_info, False, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = ProcessorComponent()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('software.ProcessorComponent', e)
