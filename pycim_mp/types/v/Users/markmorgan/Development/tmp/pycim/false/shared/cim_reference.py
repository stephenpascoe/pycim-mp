"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.739567.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid



# Module exports.
__all__ = ['CimReference']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.739567$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class CimReference(object):
    """A class within the cim v1.5 type system.

    A reference to another cim entity
    """
    def __init__(self):
        """Constructor"""
        super(CimReference, self).__init__()

        self.__change = None                                        # type = str
        self.__description = None                                   # type = str
        self.__external_id = None                                   # type = str
        self.__id = None                                            # type = uuid.UUID
        self.__name = None                                          # type = str
        self.__type = None                                          # type = str
        self.__version = None                                       # type = str


    @property
    def change(self):
        """Gets value of {class-name} change property.

        An optional description of how the item being referenced has been modified.  This is particularly useful for dealing with Ensembles (a set of simulations where something about each simulation has changed) or Conformances."""
        return self.__change

    @change.setter
    def change(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} change property."""
        self.__change = value

    @change.deleter
    def change(self, value):
        """Deletes {class-name} change property."""
        raise TypeError("Cannot delete {class-name} change property.")


    @property
    def description(self):
        """Gets value of {class-name} description property.

        A description of the element being referenced, in the context of the current class."""
        return self.__description

    @description.setter
    def description(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} description property."""
        self.__description = value

    @description.deleter
    def description(self, value):
        """Deletes {class-name} description property."""
        raise TypeError("Cannot delete {class-name} description property.")


    @property
    def external_id(self):
        """Gets value of {class-name} external_id property.

        A non-CIM (non-GUID) id used to reference the element in question."""
        return self.__external_id

    @external_id.setter
    def external_id(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} external_id property."""
        self.__external_id = value

    @external_id.deleter
    def external_id(self, value):
        """Deletes {class-name} external_id property."""
        raise TypeError("Cannot delete {class-name} external_id property.")


    @property
    def id(self):
        """Gets value of {class-name} id property.

        The ID of the element being referenced."""
        return self.__id

    @id.setter
    def id(self, value):
        if value is not None and not isinstance(value, uuid.UUID):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} id property."""
        self.__id = value

    @id.deleter
    def id(self, value):
        """Deletes {class-name} id property."""
        raise TypeError("Cannot delete {class-name} id property.")


    @property
    def name(self):
        """Gets value of {class-name} name property.

        The name of the element being referenced."""
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
    def type(self):
        """Gets value of {class-name} type property.

        The type of the element being referenced."""
        return self.__type

    @type.setter
    def type(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} type property."""
        self.__type = value

    @type.deleter
    def type(self, value):
        """Deletes {class-name} type property."""
        raise TypeError("Cannot delete {class-name} type property.")


    @property
    def version(self):
        """Gets value of {class-name} version property.

        The version of the element being referenced."""
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
        append(d, 'change', self.__change, False, True, False)
        append(d, 'description', self.__description, False, True, False)
        append(d, 'external_id', self.__external_id, False, True, False)
        append(d, 'id', self.__id, False, True, False)
        append(d, 'name', self.__name, False, True, False)
        append(d, 'type', self.__type, False, True, False)
        append(d, 'version', self.__version, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = CimReference()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('shared.CimReference', e)
