"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.754344.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.shared.responsible_party_contact_info import ResponsiblePartyContactInfo


# Module exports.
__all__ = ['ResponsibleParty']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.754344$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class ResponsibleParty(object):
    """A class within the cim v1.5 type system.

    A person/organsiation responsible for some aspect of a climate science artefact
    """
    def __init__(self):
        """Constructor"""
        super(ResponsibleParty, self).__init__()

        self.__abbreviation = None                                  # type = str
        self.__contact_info = None                                  # type = shared.ResponsiblePartyContactInfo
        self.__individual_name = None                               # type = str
        self.__organisation_name = None                             # type = str
        self.__role = None                                          # type = str


    @property
    def abbreviation(self):
        """Gets value of {class-name} abbreviation property."""
        return self.__abbreviation

    @abbreviation.setter
    def abbreviation(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} abbreviation property."""
        self.__abbreviation = value

    @abbreviation.deleter
    def abbreviation(self, value):
        """Deletes {class-name} abbreviation property."""
        raise TypeError("Cannot delete {class-name} abbreviation property.")


    @property
    def contact_info(self):
        """Gets value of {class-name} contact_info property."""
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, value):
        if value is not None and not isinstance(value, ResponsiblePartyContactInfo):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} contact_info property."""
        self.__contact_info = value

    @contact_info.deleter
    def contact_info(self, value):
        """Deletes {class-name} contact_info property."""
        raise TypeError("Cannot delete {class-name} contact_info property.")


    @property
    def individual_name(self):
        """Gets value of {class-name} individual_name property."""
        return self.__individual_name

    @individual_name.setter
    def individual_name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} individual_name property."""
        self.__individual_name = value

    @individual_name.deleter
    def individual_name(self, value):
        """Deletes {class-name} individual_name property."""
        raise TypeError("Cannot delete {class-name} individual_name property.")


    @property
    def organisation_name(self):
        """Gets value of {class-name} organisation_name property."""
        return self.__organisation_name

    @organisation_name.setter
    def organisation_name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} organisation_name property."""
        self.__organisation_name = value

    @organisation_name.deleter
    def organisation_name(self, value):
        """Deletes {class-name} organisation_name property."""
        raise TypeError("Cannot delete {class-name} organisation_name property.")


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
        append(d, 'abbreviation', self.__abbreviation, False, True, False)
        append(d, 'contact_info', self.__contact_info, False, False, False)
        append(d, 'individual_name', self.__individual_name, False, True, False)
        append(d, 'organisation_name', self.__organisation_name, False, True, False)
        append(d, 'role', self.__role, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = ResponsibleParty()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('shared.ResponsibleParty', e)
