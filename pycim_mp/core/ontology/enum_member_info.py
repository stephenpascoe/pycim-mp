"""A CIM meta-programming ontology enumeration member.

"""

# Module imports.
import re


# Module exports.
__all__ = ['EnumMemberInfo']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"



class EnumMemberInfo(object):
    """Represents an enumeration member, i.e. a constrain value associated with an enumeration.

    """
    def __init__(self, name, doc_string):
        """Constructor.

        Keyword Arguments:
        name - enumeration member name.
        doc_string - documentation string.

        """
        # Set attributes.
        self.__name = name
        self.__doc_string = doc_string
        #!REVIEW: self.__enum not defined.

    def __repr__(self):
        """String representation for debugging."""
        return self.__name


    @property
    def name(self):
        """Gets enumeration name."""
        return self.__name


    @property
    def doc_string(self):
        """Gets enumeration member documentation string."""
        return self.__doc_string


    @property
    def enum(self):
        """Gets associated enumeration."""
        return self.__enum

    @enum.setter
    def enum(self, value):
        """Sets associated enumeration."""
        self.__enum = value


    @property
    def ontology(self):
        """Gets associated ontology."""
        return None if self.package is None else self.package.ontology


    @property
    def package(self):
        """Gets associated package."""
        return None if self.enum is None else self.enum.package
        


