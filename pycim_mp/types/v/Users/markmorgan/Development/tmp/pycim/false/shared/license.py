"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.746812.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid



# Module exports.
__all__ = ['License']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.746812$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class License(object):
    """A class within the cim v1.5 type system.

    A description of a license restricting access to a unit of data or software
    """
    def __init__(self):
        """Constructor"""
        super(License, self).__init__()

        self.__contact = None                                       # type = str
        self.__description = None                                   # type = str
        self.__is_unrestricted = None                               # type = str
        self.__name = None                                          # type = str


    @property
    def contact(self):
        """Gets value of {class-name} contact property.

        The point of contact for access to this artifact; may be either a person or an institution."""
        return self.__contact

    @contact.setter
    def contact(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} contact property."""
        self.__contact = value

    @contact.deleter
    def contact(self, value):
        """Deletes {class-name} contact property."""
        raise TypeError("Cannot delete {class-name} contact property.")


    @property
    def description(self):
        """Gets value of {class-name} description property.

        A textual description of the license; might be the full text of the license, more likely to be a brief summary"""
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
    def is_unrestricted(self):
        """Gets value of {class-name} is_unrestricted property.

        If unrestricted="true" then the artifact can be downloaded with no restrictions (ie: there are no administrative steps for the user to deal with; code or data can be downloaded and used directly)."""
        return self.__is_unrestricted

    @is_unrestricted.setter
    def is_unrestricted(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} is_unrestricted property."""
        self.__is_unrestricted = value

    @is_unrestricted.deleter
    def is_unrestricted(self, value):
        """Deletes {class-name} is_unrestricted property."""
        raise TypeError("Cannot delete {class-name} is_unrestricted property.")


    @property
    def name(self):
        """Gets value of {class-name} name property.

        The name that the license goes by (ie: "GPL")"""
        return self.__name

    @name.setter
    def name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} name property."""
        self.__name = value

    @name.deleter
    def name(self, value):
        """Deletes {class-name} name property."""
        raise TypeError("Cannot delete {class-name} name property.")



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
        append(d, 'contact', self.__contact, False, True, False)
        append(d, 'description', self.__description, False, True, False)
        append(d, 'is_unrestricted', self.__is_unrestricted, False, True, False)
        append(d, 'name', self.__name, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = License()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('shared.License', e)
