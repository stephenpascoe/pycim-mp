"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.742917.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.shared.cim_reference import CimReference


# Module exports.
__all__ = ['Citation']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.742917$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Citation(object):
    """A class within the cim v1.5 type system.

    An academic reference to published work.
    """
    def __init__(self):
        """Constructor"""
        super(Citation, self).__init__()

        self.__alternative_title = None                             # type = str
        self.__collective_title = None                              # type = str
        self.__date = None                                          # type = datetime.datetime
        self.__date_type = None                                     # type = str
        self.__location = None                                      # type = str
        self.__organisation = None                                  # type = str
        self.__reference = None                                     # type = shared.CimReference
        self.__role = None                                          # type = str
        self.__title = None                                         # type = str
        self.__type = None                                          # type = str


    @property
    def alternative_title(self):
        """Gets value of {class-name} alternative_title property."""
        return self.__alternative_title

    @alternative_title.setter
    def alternative_title(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} alternative_title property."""
        self.__alternative_title = value

    @alternative_title.deleter
    def alternative_title(self, value):
        """Deletes {class-name} alternative_title property."""
        raise TypeError("Cannot delete {class-name} alternative_title property.")


    @property
    def collective_title(self):
        """Gets value of {class-name} collective_title property."""
        return self.__collective_title

    @collective_title.setter
    def collective_title(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} collective_title property."""
        self.__collective_title = value

    @collective_title.deleter
    def collective_title(self, value):
        """Deletes {class-name} collective_title property."""
        raise TypeError("Cannot delete {class-name} collective_title property.")


    @property
    def date(self):
        """Gets value of {class-name} date property."""
        return self.__date

    @date.setter
    def date(self, value):
        if value is not None and not isinstance(value, datetime.datetime):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} date property."""
        self.__date = value

    @date.deleter
    def date(self, value):
        """Deletes {class-name} date property."""
        raise TypeError("Cannot delete {class-name} date property.")


    @property
    def date_type(self):
        """Gets value of {class-name} date_type property."""
        return self.__date_type

    @date_type.setter
    def date_type(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} date_type property."""
        self.__date_type = value

    @date_type.deleter
    def date_type(self, value):
        """Deletes {class-name} date_type property."""
        raise TypeError("Cannot delete {class-name} date_type property.")


    @property
    def location(self):
        """Gets value of {class-name} location property."""
        return self.__location

    @location.setter
    def location(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} location property."""
        self.__location = value

    @location.deleter
    def location(self, value):
        """Deletes {class-name} location property."""
        raise TypeError("Cannot delete {class-name} location property.")


    @property
    def organisation(self):
        """Gets value of {class-name} organisation property."""
        return self.__organisation

    @organisation.setter
    def organisation(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} organisation property."""
        self.__organisation = value

    @organisation.deleter
    def organisation(self, value):
        """Deletes {class-name} organisation property."""
        raise TypeError("Cannot delete {class-name} organisation property.")


    @property
    def reference(self):
        """Gets value of {class-name} reference property."""
        return self.__reference

    @reference.setter
    def reference(self, value):
        if value is not None and not isinstance(value, CimReference):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} reference property."""
        self.__reference = value

    @reference.deleter
    def reference(self, value):
        """Deletes {class-name} reference property."""
        raise TypeError("Cannot delete {class-name} reference property.")


    @property
    def role(self):
        """Gets value of {class-name} role property."""
        return self.__role

    @role.setter
    def role(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} role property."""
        self.__role = value

    @role.deleter
    def role(self, value):
        """Deletes {class-name} role property."""
        raise TypeError("Cannot delete {class-name} role property.")


    @property
    def title(self):
        """Gets value of {class-name} title property."""
        return self.__title

    @title.setter
    def title(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} title property."""
        self.__title = value

    @title.deleter
    def title(self, value):
        """Deletes {class-name} title property."""
        raise TypeError("Cannot delete {class-name} title property.")


    @property
    def type(self):
        """Gets value of {class-name} type property."""
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
        append(d, 'alternative_title', self.__alternative_title, False, True, False)
        append(d, 'collective_title', self.__collective_title, False, True, False)
        append(d, 'date', self.__date, False, True, False)
        append(d, 'date_type', self.__date_type, False, True, False)
        append(d, 'location', self.__location, False, True, False)
        append(d, 'organisation', self.__organisation, False, True, False)
        append(d, 'reference', self.__reference, False, False, False)
        append(d, 'role', self.__role, False, True, False)
        append(d, 'title', self.__title, False, True, False)
        append(d, 'type', self.__type, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = Citation()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('shared.Citation', e)
