"""A CIM meta-programming ontology class.

"""

# Module imports.
import re

from pycim_mp.core.generators.generator_utils import convert_to_camel_case

# Module exports.
__all__ = ['ClassInfo']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"



class ClassInfo(object):
    """Represents a class within an ontology.
    
    """

    def __init__(self, name, base, is_abstract, doc_string, properties, decodings):
        """Constructor.

        Keyword Arguments:
        name - name (see python conventions).
        base - base class used in object hierarchies.
        is_abstract - falg indicating whether this is an abstract class or not.
        doc_string - documentation string.
        properties - set of associated properties.
        decodings - set of associated decodings.
        
        """
        # Set relations.
        for prp in properties:
            prp.cls = self        

        # Set attributes.
        self.__all_decodings = None
        self.__all_properties = None
        self.__base = base
        self.__circular_imports = []
        self.__decodings = sorted(decodings, key=lambda dc: dc.property_name)
        self.__doc_string = doc_string if doc_string is not None else ''
        self.__imports = []
        self.__is_abstract = is_abstract
        self.__is_entity = False
        self.__name = name
        self.__package = None
        self.__properties = sorted(properties, key=lambda p: p.name)
        
        # Derive is entity flag.
        self.__is_entity = is_abstract == False and self.has_property('cim_info')


    def __repr__(self):
        """String representation for debugging."""
        return self.name


    @property
    def name(self):
        """Gets class name (see python conventions)."""
        return self.__name


    @property
    def base(self):
        """Gets base type used in object hierarchy."""
        return self.__base

    @base.setter
    def base(self, value):
        """Sets associated base type."""
        self.__base = value        


    @property
    def is_abstract(self):
        """Gets flag indicating whether this class is abstract or not."""
        return self.__is_abstract


    @property
    def is_entity(self):
        """Gets flag indicating whether the class is an entity or not."""
        return self.__is_entity


    @property
    def properties(self):
        """Gets associated properties (sorted by name)."""
        return self.__properties


    @property
    def all_properties(self):
        """Gets all associated properties including those of base class (sorted by name)."""
        if self.__all_properties is None:
            self.__all_properties = list(self.properties)
            if self.base is not None:
                self.__all_properties += self.base.all_properties
        return self.__all_properties


    @property
    def imports(self):
        """Gets associated imports."""
        return self.__imports


    @property
    def circular_imports(self):
        """Gets associated circular imports."""
        return self.__circular_imports


    @property
    def doc_string(self):
        """Gets class documentation string."""
        return self.__doc_string


    @property
    def decodings(self):
        """Gets class decodings."""
        return self.__decodings


    @property
    def all_decodings(self):
        """Gets class plus base class decodings."""
        if self.__all_decodings is None:
            self.__all_decodings = list(self.decodings)
            if self.base is not None:
                self.__all_decodings += self.base.all_decodings
        return self.__all_decodings


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


    def get_property_decodings(self, prp):
        """Returns set of property decodings.

        Keyword Arguments:
        prp - property being processed.

        """
        result = []
        for dc in [dc for dc in self.all_decodings if dc.property_name == prp.name]:
            result.append(dc)
        return result


    def has_property(self, property_name):
        """Gets flag indicating whether this class has a property with same name.

        Keyword Arguments:
        lang - target programming language.

        """
        for prp in self.properties:
            if prp.name == property_name:
                return True
        return False
