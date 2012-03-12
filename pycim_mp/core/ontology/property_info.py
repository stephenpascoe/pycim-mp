"""A CIM meta-programming ontology class property.

"""

# Module imports.
import re

from pycim_mp.core.cim_exception import CIMException
from pycim_mp.core.ontology.type_info import TypeInfo
from pycim_mp.core.generators.generator_utils import convert_to_camel_case
from pycim_mp.core.generators.generator_utils import convert_to_pascal_case

# Module exports.
__all__ = ['PropertyInfo']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"


class PropertyInfo(object):
    """Represents a property within an ontology.

    """

    def __init__(self, name, doc_string, type_name, cardinality):
        """Constructor.

        Keyword Arguments:
        name - name (see python conventions).
        doc_string - documentation string.
        type_name - associated property type name.
        cardinality - 0.1, 1.1, 0.N, 1.N.

        """
        # Set attributes.
        self.__cls = None
        self.__decodings = []
        self.__doc_string = doc_string if doc_string is not None else ''
        self.__is_required = False
        self.__is_iterative = False
        self.__max_occurs = cardinality.split('.')[1]
        self.__min_occurs = cardinality.split('.')[0]
        self.__name = name
        self.__ontology = None
        self.__type = TypeInfo(type_name)

        # Derived attributes.
        self.__is_required = self.__min_occurs != '0'
        self.__is_iterative = self.__max_occurs == 'N'


    def __repr__(self):
        """String representation for debugging."""
        return self.name


    @property
    def name(self):
        """Gets property name (see python conventions)."""
        return self.__name


    @property
    def type(self):
        """Gets associated property type."""
        return self.__type


    @property
    def is_required(self):
        """Gets flag indicating whether property represents a required value."""
        return self.__is_required


    @property
    def is_iterative(self):
        """Gets flag indicating whether property is iterative."""
        return self.__is_iterative


    @property
    def decodings(self):
        """Gets property decodings."""
        return self.__decodings


    @property
    def doc_string(self):
        """Gets property documentation string."""
        return self.__doc_string


    @property
    def min_occurs(self):
        """Gets property minimum number of occurrences."""
        return self.__min_occurs


    @property
    def max_occurs(self):
        """Gets property maximum number of occurrences."""
        return self.__max_occurs


    @property
    def ontology(self):
        """Gets associated ontology."""
        return None if self.cls is None else self.cls.ontology


    @property
    def package(self):
        """Gets associated package."""
        return None if self.cls is None else self.cls.package


    @property
    def cls(self):
        """Gets associated class."""
        return self.__cls

    @cls.setter
    def cls(self, value):
        """Sets associated class."""
        self.__cls = value


