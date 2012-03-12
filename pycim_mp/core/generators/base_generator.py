"""Base class encapsulating functionality common to all cim code generators.

"""
# Module imports.
import abc
from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty
import datetime
import os
import sys

from pycim_mp.core.cim_exception import CIMException


# Module exports.
__all__ = ['BaseGenerator']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"



class BaseGenerator(object):
    """Base class encapsulating functionality common to all code generators.

    """

    # Abstract Base Class module - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def __init__(self, ontology, opts):
        """Constructor.

        Keyword Arguments:
        ontology - ontology to be parsed during course of code generation.
        opts - code generation options.

        """
        from pycim_mp.core.ontology.ontology_info import OntologyInfo

        # Defensive programming.
        if ontology is None:
            raise CIMException("Ontology is unspecified.")
        if isinstance(ontology, OntologyInfo) == False:
            raise CIMException("Ontology must be an instance of {0}.".format(OntologyInfo))
        if opts is None:
            raise CIMException("Code generation options are unspecified.")

        self.__ontology = ontology
        self.__opts = opts


    @property
    def ontology(self):
        """Gets ontology being parsed during course of code generation."""
        return self.__ontology


    @property
    def opts(self):
        """Gets code generation options."""
        return self.__opts


    def execute(self):
        """Executes the code generator.

        """
        # Parse ontology firing events accordingly.
        self.on_ontology_parse(self.__ontology)
        for pkg in self.__ontology.packages:
            self.on_package_parse(pkg)
        for cls in self.__ontology.classes:
            self.on_class_parse(cls)
        for enum in self.__ontology.enums:
            self.on_enum_parse(enum)
        

    def on_ontology_parse(self, ont):
        """Event handlers for the ontology parse event.

        Keyword Arguments:
        ont - ontology being processed.

        """
        pass


    def on_package_parse(self, pkg):
        """Event handlers for the package parse event.

        Keyword Arguments:
        pkg - package being processed.

        """
        pass



    def on_class_parse(self, cls):
        """Event handlers for the class parse event.

        Keyword Arguments:
        cls - class being processed.

        """
        pass



    def on_enum_parse(self, enum):
        """Event handlers for the enum parse event.

        Keyword Arguments:
        enum - enum being processed.

        """
        pass


