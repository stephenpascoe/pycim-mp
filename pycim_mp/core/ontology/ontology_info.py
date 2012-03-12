"""A CIM meta-programming ontology.

"""

# Module imports.
from operator import add
from functools import reduce

from pycim_mp.core.ontology.class_info import ClassInfo


# Module exports.
__all__ = ['OntologyInfo']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"



class OntologyInfo(object):
    """Represents an ontology, i.e. a set of classes organised into packages.

    """

    def __init__(self, name, version, doc_string, packages):
        """Constructor.

        Keyword Arguments:
        name - name (see python conventions).
        version - version.
        doc_string - documentation string.
        packages - set of associated packages.

        """
        # Set relations.
        for pkg in packages:
            pkg.ontology = self

        # Set attributes.
        self.__name = name
        self.__version = version
        self.__doc_string = doc_string
        self.__packages = sorted(packages, key=lambda p: p.name)
        self.__validation_error = None

        # Set supersets.
        self.__classes = reduce(add, map(lambda p : p.classes, packages))
        self.__enums = reduce(add, map(lambda p : p.enums, packages))
        self.__enum_members = reduce(add, map(lambda e : e.members, self.__enums))
        self.__entities = reduce(add, map(lambda p : p.entities, packages))
        self.__properties = reduce(add, map(lambda c : c.properties, self.__classes))
        self.__property_types = map(lambda p : p.type, self.__properties)
        self.__types = sorted(self.__classes + self.__enums)

        # Set base classes.
        for c in [c for c in self.__classes if c.base is not None]:
            t = self.get_type(c.base)
            if t is not None:
                c.base = t

        # Set property type is_class flag.
        for pt in [pt for pt in self.__property_types if pt.is_complex]:
            t = self.get_type(pt.name)
            if t is not None:
                pt.is_class = isinstance(t, ClassInfo)


    def __repr__(self):
        """String representation for debugging."""
        return self.__name + ' v' + self.__version


    @property
    def name(self):
        """Gets ontology name."""
        return self.__name


    @property
    def version(self):
        """Gets ontology version."""
        return self.__version


    @property
    def doc_string(self):
        """Gets ontology documentation string."""
        return self.__doc_string


    @property
    def packages(self):
        """Gets superset of packages (sorted by name)."""
        return self.__packages

    
    @property
    def classes(self):
        """Gets superset of classes."""
        return self.__classes


    @property
    def enums(self):
        """Gets superset of enums."""
        return self.__enums


    @property
    def entities(self):
        """Gets superset of entities."""
        return self.__entities


    @property
    def properties(self):
        """Gets superset of class properties."""
        return self.__properties
    

    @property
    def property_types(self):
        """Gets superset of class property types."""
        return self.__property_types


    @property
    def enum_members(self):
        """Gets superset of enum members."""
        return self.__enums


    @property
    def types(self):
        """Gets superset of types (i.e. classes and enums)."""
        return self.__types
        

    def get_type(self, type_name):
        """Returns type with matching name.

        Keyword Arguments:
        name - name of target package.

        """
        pkg_name = type_name.split('.')[0]
        type_name = type_name.split('.')[1]
        for t in self.types:
            if t.package.name == pkg_name and t.name == type_name:
                return t
        return None

            