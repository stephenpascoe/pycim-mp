"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.738307.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.shared.cim_genealogy import CimGenealogy
from cim.v1_5.types.shared.cim_type_info import CimTypeInfo
from cim.v1_5.types.shared.document_status_type import DocumentStatusType
from cim.v1_5.types.shared.responsible_party import ResponsibleParty
from cim.v1_5.types.shared.standard_name import StandardName


# Module exports.
__all__ = ['CimInfo']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.738307$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class CimInfo(object):
    """A class within the cim v1.5 type system.

    Encapsulates common cim information.
    """
    def __init__(self):
        """Constructor"""
        super(CimInfo, self).__init__()

        self.__author = None                                        # type = shared.ResponsibleParty
        self.__create_date = datetime.datetime.now()                # type = datetime.datetime
        self.__external_id = []                                     # type = shared.StandardName
        self.__genealogy = None                                     # type = shared.CimGenealogy
        self.__id = uuid.uuid4()                                    # type = uuid.UUID
        self.__metadata_id = None                                   # type = str
        self.__metadata_version = None                              # type = str
        self.__quality = []                                         # type = str
        self.__status = None                                        # type = shared.DocumentStatusType
        self.__type_info = None                                     # type = shared.CimTypeInfo
        self.__version = str()                                      # type = str


    @property
    def author(self):
        """Gets value of {class-name} author property.

        Universally identifies the CIM instance"""
        return self.__author

    @author.setter
    def author(self, value):
        if value is not None and not isinstance(value, ResponsibleParty):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} author property."""
        self.__author = value

    @author.deleter
    def author(self, value):
        """Deletes {class-name} author property."""
        raise TypeError("Cannot delete {class-name} author property.")


    @property
    def create_date(self):
        """Gets value of cim info create_date property.

        The date the instance was created"""
        return self.__create_date

    @create_date.setter
    def create_date(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, datetime.datetime):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of cim info create_date property."""
        self.__create_date = value

    @create_date.deleter
    def create_date(self, value):
        """Deletes cim info create_date property."""
        raise TypeError("Cannot delete cim info create_date property.")


    @property
    def external_id(self):
        """Gets value of {class-name} external_id property.

        The id of this instance as referenced by an external body (ie: DOI, or even IPSL)"""
        return list(self.__external_id)

    @external_id.setter
    def external_id(self, value):
        """Sets value of {class-name} external_id property.

        The id of this instance as referenced by an external body (ie: DOI, or even IPSL)"""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__external_id = []
        for i in value:
            self.append_to_external_id(i)

    @external_id.deleter
    def external_id(self, value):
        """Deletes {class-name} external_id property."""
        raise TypeError("Cannot delete {class-name} external_id property.")

    def append_to_external_id(self, item):
        """Appends an item to the managed {class-name} external_id collection."""
        if not isinstance(item, StandardName):
            raise TypeError("item is of incorrect type.")
        self.__external_id.append(item)

    def remove_from_external_id(self, item):
        """Removes an item from the managed {class-name} external_id collection."""
        if not isinstance(item, StandardName):
            raise TypeError("item is of incorrect type.")
        self.__external_id.remove(item)


    @property
    def genealogy(self):
        """Gets value of {class-name} genealogy property.

        Specifies the relationship of this document with another document. Various relationship types (depending on the type of document; ie: simulation, component, etc.) are supported."""
        return self.__genealogy

    @genealogy.setter
    def genealogy(self, value):
        if value is not None and not isinstance(value, CimGenealogy):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} genealogy property."""
        self.__genealogy = value

    @genealogy.deleter
    def genealogy(self, value):
        """Deletes {class-name} genealogy property."""
        raise TypeError("Cannot delete {class-name} genealogy property.")


    @property
    def id(self):
        """Gets value of cim info id property.

        Universally identifies the instance."""
        return self.__id

    @id.setter
    def id(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, uuid.UUID):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of cim info id property."""
        self.__id = value

    @id.deleter
    def id(self, value):
        """Deletes cim info id property."""
        raise TypeError("Cannot delete cim info id property.")


    @property
    def metadata_id(self):
        """Gets value of {class-name} metadata_id property."""
        return self.__metadata_id

    @metadata_id.setter
    def metadata_id(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} metadata_id property."""
        self.__metadata_id = value

    @metadata_id.deleter
    def metadata_id(self, value):
        """Deletes {class-name} metadata_id property."""
        raise TypeError("Cannot delete {class-name} metadata_id property.")


    @property
    def metadata_version(self):
        """Gets value of {class-name} metadata_version property."""
        return self.__metadata_version

    @metadata_version.setter
    def metadata_version(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} metadata_version property."""
        self.__metadata_version = value

    @metadata_version.deleter
    def metadata_version(self, value):
        """Deletes {class-name} metadata_version property."""
        raise TypeError("Cannot delete {class-name} metadata_version property.")


    @property
    def quality(self):
        """Gets value of {class-name} quality property.

        A (set of) quality record(s) for this document.."""
        return list(self.__quality)

    @quality.setter
    def quality(self, value):
        """Sets value of {class-name} quality property.

        A (set of) quality record(s) for this document.."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__quality = []
        for i in value:
            self.append_to_quality(i)

    @quality.deleter
    def quality(self, value):
        """Deletes {class-name} quality property."""
        raise TypeError("Cannot delete {class-name} quality property.")

    def append_to_quality(self, item):
        """Appends an item to the managed {class-name} quality collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__quality.append(item)

    def remove_from_quality(self, item):
        """Removes an item from the managed {class-name} quality collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__quality.remove(item)


    @property
    def status(self):
        """Gets value of {class-name} status property."""
        return self.__status

    @status.setter
    def status(self, value):
        if value is not None and not isinstance(value, DocumentStatusType):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} status property."""
        self.__status = value

    @status.deleter
    def status(self, value):
        """Deletes {class-name} status property."""
        raise TypeError("Cannot delete {class-name} status property.")


    @property
    def type_info(self):
        """Gets value of {class-name} type_info property.

        Type information used to a priori identify type."""
        return self.__type_info

    @type_info.setter
    def type_info(self, value):
        if value is not None and not isinstance(value, CimTypeInfo):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} type_info property."""
        self.__type_info = value

    @type_info.deleter
    def type_info(self, value):
        """Deletes {class-name} type_info property."""
        raise TypeError("Cannot delete {class-name} type_info property.")


    @property
    def version(self):
        """Gets value of cim info version property.

        Universally identifies the instance version."""
        return self.__version

    @version.setter
    def version(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of cim info version property."""
        self.__version = value

    @version.deleter
    def version(self, value):
        """Deletes cim info version property."""
        raise TypeError("Cannot delete cim info version property.")



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
        append(d, 'author', self.__author, False, False, False)
        append(d, 'create_date', self.__create_date, False, True, False)
        append(d, 'external_id', self.__external_id, True, False, False)
        append(d, 'genealogy', self.__genealogy, False, False, False)
        append(d, 'id', self.__id, False, True, False)
        append(d, 'metadata_id', self.__metadata_id, False, True, False)
        append(d, 'metadata_version', self.__metadata_version, False, True, False)
        append(d, 'quality', self.__quality, True, True, False)
        append(d, 'status', self.__status, False, False, False)
        append(d, 'type_info', self.__type_info, False, False, False)
        append(d, 'version', self.__version, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = CimInfo()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('shared.CimInfo', e)
