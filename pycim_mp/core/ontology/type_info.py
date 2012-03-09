"""A CIM meta-programming ontology class type.

"""

# Module imports.
import re

from pycim_mp.core.ontology.class_info import ClassInfo
from pycim_mp.core.ontology.enum_info import EnumInfo
from pycim_mp.core.ontology.package_info import PackageInfo


# Module exports.
__all__ = ['TypeInfo']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"



class TypeInfo(object):
    """Represents a type within an ontology.

    """

    def __init__(self, name):
        """Constructor.

        Keyword Arguments:
        property - associated property.
        name - type name.

        """
        # Set attributes.
        self.__complex_type = None
        self.__is_enum = False
        self.__is_complex = len(name.split('.')) > 1
        self.__name = name
        self.__name_of_package = ''
        self.__name_of_type = name

        # Derive attributes.
        if self.__is_complex:
            self.__name_of_package = name.split('.')[0]
            self.__name_of_type = name.split('.')[1]


    def __repr__(self):
        """Returns a string representation."""
        return self.name


    @property
    def name(self):
        """Gets name."""
        return self.__name


    @property
    def name_of_type(self):
        """Gets name of type."""
        return self.__name_of_type


    @property
    def name_of_package(self):
        """Gets name of associated package."""
        return self.__name_of_package


    @property
    def is_complex(self):
        """Gets flag indicating whether type represents a complex class or enum."""
        return self.__is_complex


    @property
    def is_simple(self):
        """Gets flag indicating whether type represents a simple type, e.g. a string."""
        return self.__is_complex == False


    @property
    def complex_type(self):
        """Gets complex type."""
        return self.__complex_type

    @complex_type.setter
    def complex_type(self, value):
        """Sets complex type."""
        if self.is_complex == False:
            raise TypeError("type is not complex.")
        if isinstance(value, ClassInfo) == False and isinstance(value, EnumInfo) == False:
            raise TypeError("value is of incorrect type.")
        self.__complex_type = value
        self.__is_enum = isinstance(value, EnumInfo)


    @property
    def is_enum(self):
        """Gets flag indicating whether type represents an enumerated type."""
        return self.__is_complex and self.__is_enum


    @property
    def is_class(self):
        """Gets flag indicating whether type represents a complex class."""
        return self.__is_complex and not self.__is_enum




