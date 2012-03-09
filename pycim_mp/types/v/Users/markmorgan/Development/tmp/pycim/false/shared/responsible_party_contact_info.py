"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.755460.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid



# Module exports.
__all__ = ['ResponsiblePartyContactInfo']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.755460$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class ResponsiblePartyContactInfo(object):
    """A class within the cim v1.5 type system.

    Maps gmd:contactInfo element.
    """
    def __init__(self):
        """Constructor"""
        super(ResponsiblePartyContactInfo, self).__init__()

        self.__address = None                                       # type = str
        self.__email = None                                         # type = str
        self.__url = None                                           # type = str


    @property
    def address(self):
        """Gets value of {class-name} address property."""
        return self.__address

    @address.setter
    def address(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} address property."""
        self.__address = value

    @address.deleter
    def address(self, value):
        """Deletes {class-name} address property."""
        raise TypeError("Cannot delete {class-name} address property.")


    @property
    def email(self):
        """Gets value of {class-name} email property."""
        return self.__email

    @email.setter
    def email(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} email property."""
        self.__email = value

    @email.deleter
    def email(self, value):
        """Deletes {class-name} email property."""
        raise TypeError("Cannot delete {class-name} email property.")


    @property
    def url(self):
        """Gets value of {class-name} url property."""
        return self.__url

    @url.setter
    def url(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} url property."""
        self.__url = value

    @url.deleter
    def url(self, value):
        """Deletes {class-name} url property."""
        raise TypeError("Cannot delete {class-name} url property.")



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
        append(d, 'address', self.__address, False, True, False)
        append(d, 'email', self.__email, False, True, False)
        append(d, 'url', self.__url, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = ResponsiblePartyContactInfo()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('shared.ResponsiblePartyContactInfo', e)
