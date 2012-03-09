"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.741223.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid



# Module exports.
__all__ = ['CimTypeInfo']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.741223$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class CimTypeInfo(object):
    """A class within the cim v1.5 type system.

    Encapsulates cim type information.
    """
    def __init__(self):
        """Constructor"""
        super(CimTypeInfo, self).__init__()

        self.__package = str()                                      # type = str
        self.__schema = str()                                       # type = str
        self.__type = str()                                         # type = str
        self.__type_display_name = str()                            # type = str


    @property
    def package(self):
        """Gets value of cim type info package property.

        Package name."""
        return self.__package

    @package.setter
    def package(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of cim type info package property."""
        self.__package = value

    @package.deleter
    def package(self, value):
        """Deletes cim type info package property."""
        raise TypeError("Cannot delete cim type info package property.")


    @property
    def schema(self):
        """Gets value of cim type info schema property.

        Schema version."""
        return self.__schema

    @schema.setter
    def schema(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of cim type info schema property."""
        self.__schema = value

    @schema.deleter
    def schema(self, value):
        """Deletes cim type info schema property."""
        raise TypeError("Cannot delete cim type info schema property.")


    @property
    def type(self):
        """Gets value of cim type info type property.

        Type name."""
        return self.__type

    @type.setter
    def type(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of cim type info type property."""
        self.__type = value

    @type.deleter
    def type(self, value):
        """Deletes cim type info type property."""
        raise TypeError("Cannot delete cim type info type property.")


    @property
    def type_display_name(self):
        """Gets value of cim type info type_display_name property.

        Type display name."""
        return self.__type_display_name

    @type_display_name.setter
    def type_display_name(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of cim type info type_display_name property."""
        self.__type_display_name = value

    @type_display_name.deleter
    def type_display_name(self, value):
        """Deletes cim type info type_display_name property."""
        raise TypeError("Cannot delete cim type info type_display_name property.")



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
        append(d, 'package', self.__package, False, True, False)
        append(d, 'schema', self.__schema, False, True, False)
        append(d, 'type', self.__type, False, True, False)
        append(d, 'type_display_name', self.__type_display_name, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = CimTypeInfo()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('shared.CimTypeInfo', e)
