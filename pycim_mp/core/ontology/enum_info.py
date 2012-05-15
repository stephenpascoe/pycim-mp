"""A CIM meta-programming ontology enumeration.

"""

# Module imports.
import re

from pycim_mp.core.generators.generator_utils import convert_to_camel_case


# Module exports.
__all__ = ['EnumInfo']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"



class EnumInfo(object):
    """Represents an enumeration, i.e. a constrained set of values.

    """
    def __init__(self, name, is_open, doc_string, members):
        """Constructor.

        Keyword Arguments:
        name - enumeration name.
        is_open - flag indicating whether the enumeration is open or not.
        doc_string - documentation string.
        members - set of enumeration members.

        """
        # Set relations.
        for m in members:
            m.enum = self

        # Set attributes.
        self.__name = name
        self.__is_open = is_open
        self.__doc_string = doc_string if doc_string is not None else ''
        self.__members = sorted(members, key=lambda m: m.name)
        #!REVIEW: self.__package not defined.  Calling getter prior to setter will cause error.

    def __repr__(self):
        """String representation for debugging."""
        return self.name


    @property
    def name(self):
        """Gets enumeration name."""
        return self.__name


    @property
    def is_open(self):
        """Gets flag indicating whether the enumeration is open or not."""
        return self.__is_open


    @property
    def doc_string(self):
        """Gets enum documentation string."""
        return self.__doc_string


    @property
    def members(self):
        """Gets associated members (sorted by name)."""
        return self.__members


    @property
    def ontology(self):
        """Gets associated ontology."""
        return None if self.package is None else self.package.ontology


    @property
    def package(self):
        """Gets associated package."""
        return self.__package

    @package.setter
    def package(self, value):
        """Sets associated package."""
        self.__package = value


