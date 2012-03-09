"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.744714.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.shared.compiler_type import CompilerType


# Module exports.
__all__ = ['Compiler']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.744714$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Compiler(object):
    """A class within the cim v1.5 type system.

    A language of a compiler used on a particular platform
    """
    def __init__(self):
        """Constructor"""
        super(Compiler, self).__init__()

        self.__environment_variables = None                         # type = str
        self.__language = None                                      # type = str
        self.__name = None                                          # type = str
        self.__options = None                                       # type = str
        self.__type = None                                          # type = shared.CompilerType
        self.__version = None                                       # type = str


    @property
    def environment_variables(self):
        """Gets value of {class-name} environment_variables property.

        The set of environment_variables used during compilation (recorded here as a single string rather than separate elements)"""
        return self.__environment_variables

    @environment_variables.setter
    def environment_variables(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} environment_variables property."""
        self.__environment_variables = value

    @environment_variables.deleter
    def environment_variables(self, value):
        """Deletes {class-name} environment_variables property."""
        raise TypeError("Cannot delete {class-name} environment_variables property.")


    @property
    def language(self):
        """Gets value of {class-name} language property."""
        return self.__language

    @language.setter
    def language(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} language property."""
        self.__language = value

    @language.deleter
    def language(self, value):
        """Deletes {class-name} language property."""
        raise TypeError("Cannot delete {class-name} language property.")


    @property
    def name(self):
        """Gets value of {class-name} name property."""
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


    @property
    def options(self):
        """Gets value of {class-name} options property.

        The set of options used during compilation (recorded here as a single string rather than separate elements)"""
        return self.__options

    @options.setter
    def options(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} options property."""
        self.__options = value

    @options.deleter
    def options(self, value):
        """Deletes {class-name} options property."""
        raise TypeError("Cannot delete {class-name} options property.")


    @property
    def type(self):
        """Gets value of {class-name} type property."""
        return self.__type

    @type.setter
    def type(self, value):
        if value is not None and not isinstance(value, CompilerType):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} type property."""
        self.__type = value

    @type.deleter
    def type(self, value):
        """Deletes {class-name} type property."""
        raise TypeError("Cannot delete {class-name} type property.")


    @property
    def version(self):
        """Gets value of {class-name} version property."""
        return self.__version

    @version.setter
    def version(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} version property."""
        self.__version = value

    @version.deleter
    def version(self, value):
        """Deletes {class-name} version property."""
        raise TypeError("Cannot delete {class-name} version property.")



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
        append(d, 'environment_variables', self.__environment_variables, False, True, False)
        append(d, 'language', self.__language, False, True, False)
        append(d, 'name', self.__name, False, True, False)
        append(d, 'options', self.__options, False, True, False)
        append(d, 'type', self.__type, False, False, False)
        append(d, 'version', self.__version, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = Compiler()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('shared.Compiler', e)
