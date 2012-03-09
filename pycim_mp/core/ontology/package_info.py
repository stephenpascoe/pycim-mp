"""A CIM meta-programming ontology package.

"""
# Module imports.
import re
from operator import add

from pycim_mp.core.generators.utils import convert_to_camel_case


# Module exports.
__all__ = ['PackageInfo']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"



class PackageInfo(object):
    """Represents a package within an ontology.

    """

    def __init__(self, name, doc_string, classes, enums):
        """Constructor.

        Keyword Arguments:
        name - name (see python conventions).
        doc_string - documentation string.
        classes - set of associated classes.
        enums - set of associated enums.

        """
        # Set relations.
        for cls in classes:
            cls.package = self
        for enum in enums:
            enum.package = self

        # Set attributes.
        self.__classes = sorted(classes, key=lambda c: c.name)
        self.__doc_string = doc_string
        self.__entities = []
        self.__enums = sorted(enums, key=lambda e: e.name)
        self.__external_types = []
        self.__name = name
        self.__ontology = None
        self.__properties = []
        self.__types = []
        
        # Derive superset of entities.
        self.__entities = sorted([c for c in classes if c.is_entity])

        # Derive superset of types.
        self.__types = sorted(classes + enums, key=lambda t: t.name)

        # Derive superset of properties.
        for cls in self.__classes:
            for prp in cls.properties:
                self.__properties.append(prp)
        
        # Derive superset of external types.
        for prp in self.__properties:
            if prp.type.is_complex and \
               prp.type.name_of_package != self.name and \
               prp.type not in self.__external_types:
                self.__external_types.append(prp.type)


    def __repr__(self):
        """String representation for debugging."""
        return self.__name


    @property
    def name(self):
        """Gets package name (see python conventions)."""
        return self.__name

    
    @property
    def doc_string(self):
        """Gets package documentation string."""
        return self.__doc_string


    @property
    def classes(self):
        """Gets associated classes (sorted by name)."""
        return self.__classes


    @property
    def entities(self):
        """Gets associated entities (sorted by name)."""
        return self.__entities


    @property
    def enums(self):
        """Gets associated enums (sorted by name)."""
        return self.__enums


    @property
    def types(self):
        """Gets set of package types (sorted by name)."""
        return self.__types
    

    @property
    def external_types(self):
        """Gets set of package extenal type (sorted by name)."""
        return self.__external_types


    @property
    def ontology(self):
        """Gets associated ontology."""
        return self.__ontology

    @ontology.setter
    def ontology(self, value):
        """Sets associated ontology."""
        self.__ontology = value




