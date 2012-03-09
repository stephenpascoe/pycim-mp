"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.752064.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.shared.machine_compiler_unit import MachineCompilerUnit
from cim.v1_5.types.shared.responsible_party import ResponsibleParty


# Module exports.
__all__ = ['Platform']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.752064$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Platform(object):
    """A class within the cim v1.5 type system.

    A platform is a description of resources used to deploy a component/simulation.  A platform pairs a machine with a (set of) compilers.  There is also a point of contact for the platform.
    """
    def __init__(self):
        """Constructor"""
        super(Platform, self).__init__()

        self.__contact = []                                         # type = shared.ResponsibleParty
        self.__description = None                                   # type = str
        self.__long_name = None                                     # type = str
        self.__short_name = None                                    # type = str
        self.__unit = None                                          # type = shared.MachineCompilerUnit


    @property
    def contact(self):
        """Gets value of {class-name} contact property."""
        return list(self.__contact)

    @contact.setter
    def contact(self, value):
        """Sets value of {class-name} contact property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__contact = []
        for i in value:
            self.append_to_contact(i)

    @contact.deleter
    def contact(self, value):
        """Deletes {class-name} contact property."""
        raise TypeError("Cannot delete {class-name} contact property.")

    def append_to_contact(self, item):
        """Appends an item to the managed {class-name} contact collection."""
        if not isinstance(item, ResponsibleParty):
            raise TypeError("item is of incorrect type.")
        self.__contact.append(item)

    def remove_from_contact(self, item):
        """Removes an item from the managed {class-name} contact collection."""
        if not isinstance(item, ResponsibleParty):
            raise TypeError("item is of incorrect type.")
        self.__contact.remove(item)


    @property
    def description(self):
        """Gets value of {class-name} description property."""
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
    def long_name(self):
        """Gets value of {class-name} long_name property."""
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
        """Gets value of {class-name} short_name property."""
        return self.__short_name

    @short_name.setter
    def short_name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} short_name property."""
        self.__short_name = value

    @short_name.deleter
    def short_name(self, value):
        """Deletes {class-name} short_name property."""
        raise TypeError("Cannot delete {class-name} short_name property.")


    @property
    def unit(self):
        """Gets value of {class-name} unit property."""
        return self.__unit

    @unit.setter
    def unit(self, value):
        if value is not None and not isinstance(value, MachineCompilerUnit):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} unit property."""
        self.__unit = value

    @unit.deleter
    def unit(self, value):
        """Deletes {class-name} unit property."""
        raise TypeError("Cannot delete {class-name} unit property.")



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
        append(d, 'contact', self.__contact, True, False, False)
        append(d, 'description', self.__description, False, True, False)
        append(d, 'long_name', self.__long_name, False, True, False)
        append(d, 'short_name', self.__short_name, False, True, False)
        append(d, 'unit', self.__unit, False, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = Platform()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('shared.Platform', e)
