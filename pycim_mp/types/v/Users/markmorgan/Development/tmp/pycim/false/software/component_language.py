"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.756311.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.software.component_language_property import ComponentLanguageProperty


# Module exports.
__all__ = ['ComponentLanguage']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.756311$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class ComponentLanguage(object):
    """A class within the cim v1.5 type system.

    Details of the programming language a component is written in. There is an assumption that all EntryPoints use the same ComponentLanguage.
    """
    def __init__(self):
        """Constructor"""
        super(ComponentLanguage, self).__init__()

        self.__name = str()                                         # type = str
        self.__properties = []                                      # type = software.ComponentLanguageProperty


    @property
    def name(self):
        """Gets value of component language name property.

        The name of the language."""
        return self.__name

    @name.setter
    def name(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of component language name property."""
        self.__name = value

    @name.deleter
    def name(self, value):
        """Deletes component language name property."""
        raise TypeError("Cannot delete component language name property.")


    @property
    def properties(self):
        """Gets value of {class-name} properties property."""
        return list(self.__properties)

    @properties.setter
    def properties(self, value):
        """Sets value of {class-name} properties property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__properties = []
        for i in value:
            self.append_to_properties(i)

    @properties.deleter
    def properties(self, value):
        """Deletes {class-name} properties property."""
        raise TypeError("Cannot delete {class-name} properties property.")

    def append_to_properties(self, item):
        """Appends an item to the managed {class-name} properties collection."""
        if not isinstance(item, ComponentLanguageProperty):
            raise TypeError("item is of incorrect type.")
        self.__properties.append(item)

    def remove_from_properties(self, item):
        """Removes an item from the managed {class-name} properties collection."""
        if not isinstance(item, ComponentLanguageProperty):
            raise TypeError("item is of incorrect type.")
        self.__properties.remove(item)



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
        append(d, 'name', self.__name, False, True, False)
        append(d, 'properties', self.__properties, True, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = ComponentLanguage()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('software.ComponentLanguage', e)
