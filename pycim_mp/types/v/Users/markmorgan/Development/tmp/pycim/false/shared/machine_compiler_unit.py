"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.750561.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.shared.compiler import Compiler
from cim.v1_5.types.shared.machine import Machine


# Module exports.
__all__ = ['MachineCompilerUnit']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.750561$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class MachineCompilerUnit(object):
    """A class within the cim v1.5 type system.

    Associates a machine with a [set of] compilers.  This is a separate class in case a platform needs to specify more than one machine/compiler pair.
    """
    def __init__(self):
        """Constructor"""
        super(MachineCompilerUnit, self).__init__()

        self.__compiler = []                                        # type = shared.Compiler
        self.__machine = None                                       # type = shared.Machine


    @property
    def compiler(self):
        """Gets value of {class-name} compiler property."""
        return list(self.__compiler)

    @compiler.setter
    def compiler(self, value):
        """Sets value of {class-name} compiler property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__compiler = []
        for i in value:
            self.append_to_compiler(i)

    @compiler.deleter
    def compiler(self, value):
        """Deletes {class-name} compiler property."""
        raise TypeError("Cannot delete {class-name} compiler property.")

    def append_to_compiler(self, item):
        """Appends an item to the managed {class-name} compiler collection."""
        if not isinstance(item, Compiler):
            raise TypeError("item is of incorrect type.")
        self.__compiler.append(item)

    def remove_from_compiler(self, item):
        """Removes an item from the managed {class-name} compiler collection."""
        if not isinstance(item, Compiler):
            raise TypeError("item is of incorrect type.")
        self.__compiler.remove(item)


    @property
    def machine(self):
        """Gets value of {class-name} machine property."""
        return self.__machine

    @machine.setter
    def machine(self, value):
        if value is not None and not isinstance(value, Machine):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} machine property."""
        self.__machine = value

    @machine.deleter
    def machine(self, value):
        """Deletes {class-name} machine property."""
        raise TypeError("Cannot delete {class-name} machine property.")



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
        append(d, 'compiler', self.__compiler, True, False, False)
        append(d, 'machine', self.__machine, False, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = MachineCompilerUnit()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('shared.MachineCompilerUnit', e)
