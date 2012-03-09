"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.728740.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.shared.license import License


# Module exports.
__all__ = ['DataRestriction']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.728740$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class DataRestriction(object):
    """A class within the cim v1.5 type system.

    An access or use restriction on some element of the DataObject's actual data.
    """
    def __init__(self):
        """Constructor"""
        super(DataRestriction, self).__init__()

        self.__license = None                                       # type = shared.License
        self.__restriction = None                                   # type = str
        self.__scope = None                                         # type = str


    @property
    def license(self):
        """Gets value of {class-name} license property.

        The thing (data or metadata, access or use) that this restriction is applied to."""
        return self.__license

    @license.setter
    def license(self, value):
        if value is not None and not isinstance(value, License):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} license property."""
        self.__license = value

    @license.deleter
    def license(self, value):
        """Deletes {class-name} license property."""
        raise TypeError("Cannot delete {class-name} license property.")


    @property
    def restriction(self):
        """Gets value of {class-name} restriction property.

        The thing (data or metadata, access or use) that this restriction is applied to."""
        return self.__restriction

    @restriction.setter
    def restriction(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} restriction property."""
        self.__restriction = value

    @restriction.deleter
    def restriction(self, value):
        """Deletes {class-name} restriction property."""
        raise TypeError("Cannot delete {class-name} restriction property.")


    @property
    def scope(self):
        """Gets value of {class-name} scope property.

        The thing (data or metadata, access or use) that this restriction is applied to."""
        return self.__scope

    @scope.setter
    def scope(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} scope property."""
        self.__scope = value

    @scope.deleter
    def scope(self, value):
        """Deletes {class-name} scope property."""
        raise TypeError("Cannot delete {class-name} scope property.")



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
        append(d, 'license', self.__license, False, False, False)
        append(d, 'restriction', self.__restriction, False, True, False)
        append(d, 'scope', self.__scope, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = DataRestriction()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('data.DataRestriction', e)
