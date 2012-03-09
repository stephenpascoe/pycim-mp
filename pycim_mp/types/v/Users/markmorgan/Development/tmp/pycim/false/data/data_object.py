"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.725279.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.data.data_content import DataContent
from cim.v1_5.types.data.data_distribution import DataDistribution
from cim.v1_5.types.data.data_extent import DataExtent
from cim.v1_5.types.data.data_hierarchy_level import DataHierarchyLevel
from cim.v1_5.types.data.data_property import DataProperty
from cim.v1_5.types.data.data_restriction import DataRestriction
from cim.v1_5.types.data.data_status_type import DataStatusType
from cim.v1_5.types.data.data_storage import DataStorage
from cim.v1_5.types.shared.cim_info import CimInfo
from cim.v1_5.types.shared.cim_reference import CimReference
from cim.v1_5.types.shared.citation import Citation
from cim.v1_5.types.shared.data_source import DataSource


# Module exports.
__all__ = ['DataObject']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.725279$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class DataObject(DataSource):
    """A class within the cim v1.5 type system.

    A DataObject describes a unit of data.  DataObjects can be grouped hierarchically.  The attributes hierarchyLevelName and hierarchyLevelValue describe how objects are grouped.
    """
    def __init__(self):
        """Constructor"""
        super(DataObject, self).__init__()

        self.__acronym = None                                       # type = str
        self.__child_object = []                                    # type = data.DataObject
        self.__cim_info = shared.cim_info()                         # type = shared.CimInfo
        self.__citations = []                                       # type = shared.Citation
        self.__content = []                                         # type = data.DataContent
        self.__data_property = []                                   # type = data.DataProperty
        self.__data_status = None                                   # type = data.DataStatusType
        self.__description = None                                   # type = str
        self.__distribution = None                                  # type = data.DataDistribution
        self.__extent = None                                        # type = data.DataExtent
        self.__geometry_model = None                                # type = str
        self.__hierarchy_level = None                               # type = data.DataHierarchyLevel
        self.__keyword = None                                       # type = str
        self.__parent_object = None                                 # type = data.DataObject
        self.__parent_object_reference = None                       # type = shared.CimReference
        self.__restriction = []                                     # type = data.DataRestriction
        self.__source_simulation = None                             # type = str
        self.__storage = []                                         # type = data.DataStorage


    @property
    def acronym(self):
        """Gets value of {class-name} acronym property."""
        return self.__acronym

    @acronym.setter
    def acronym(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} acronym property."""
        self.__acronym = value

    @acronym.deleter
    def acronym(self, value):
        """Deletes {class-name} acronym property."""
        raise TypeError("Cannot delete {class-name} acronym property.")


    @property
    def child_object(self):
        """Gets value of {class-name} child_object property."""
        return list(self.__child_object)

    @child_object.setter
    def child_object(self, value):
        """Sets value of {class-name} child_object property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__child_object = []
        for i in value:
            self.append_to_child_object(i)

    @child_object.deleter
    def child_object(self, value):
        """Deletes {class-name} child_object property."""
        raise TypeError("Cannot delete {class-name} child_object property.")

    def append_to_child_object(self, item):
        """Appends an item to the managed {class-name} child_object collection."""
        if not isinstance(item, DataObject):
            raise TypeError("item is of incorrect type.")
        self.__child_object.append(item)

    def remove_from_child_object(self, item):
        """Removes an item from the managed {class-name} child_object collection."""
        if not isinstance(item, DataObject):
            raise TypeError("item is of incorrect type.")
        self.__child_object.remove(item)


    @property
    def cim_info(self):
        """Gets value of data object cim_info property."""
        return self.__cim_info

    @cim_info.setter
    def cim_info(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, CimInfo):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of data object cim_info property."""
        self.__cim_info = value

    @cim_info.deleter
    def cim_info(self, value):
        """Deletes data object cim_info property."""
        raise TypeError("Cannot delete data object cim_info property.")


    @property
    def citations(self):
        """Gets value of {class-name} citations property."""
        return list(self.__citations)

    @citations.setter
    def citations(self, value):
        """Sets value of {class-name} citations property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__citations = []
        for i in value:
            self.append_to_citations(i)

    @citations.deleter
    def citations(self, value):
        """Deletes {class-name} citations property."""
        raise TypeError("Cannot delete {class-name} citations property.")

    def append_to_citations(self, item):
        """Appends an item to the managed {class-name} citations collection."""
        if not isinstance(item, Citation):
            raise TypeError("item is of incorrect type.")
        self.__citations.append(item)

    def remove_from_citations(self, item):
        """Removes an item from the managed {class-name} citations collection."""
        if not isinstance(item, Citation):
            raise TypeError("item is of incorrect type.")
        self.__citations.remove(item)


    @property
    def content(self):
        """Gets value of {class-name} content property.

        The content of a DataObject corresponds to a variable (in THREDDS, ...etc.)"""
        return list(self.__content)

    @content.setter
    def content(self, value):
        """Sets value of {class-name} content property.

        The content of a DataObject corresponds to a variable (in THREDDS, ...etc.)"""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__content = []
        for i in value:
            self.append_to_content(i)

    @content.deleter
    def content(self, value):
        """Deletes {class-name} content property."""
        raise TypeError("Cannot delete {class-name} content property.")

    def append_to_content(self, item):
        """Appends an item to the managed {class-name} content collection."""
        if not isinstance(item, DataContent):
            raise TypeError("item is of incorrect type.")
        self.__content.append(item)

    def remove_from_content(self, item):
        """Removes an item from the managed {class-name} content collection."""
        if not isinstance(item, DataContent):
            raise TypeError("item is of incorrect type.")
        self.__content.remove(item)


    @property
    def data_property(self):
        """Gets value of {class-name} data_property property."""
        return list(self.__data_property)

    @data_property.setter
    def data_property(self, value):
        """Sets value of {class-name} data_property property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__data_property = []
        for i in value:
            self.append_to_data_property(i)

    @data_property.deleter
    def data_property(self, value):
        """Deletes {class-name} data_property property."""
        raise TypeError("Cannot delete {class-name} data_property property.")

    def append_to_data_property(self, item):
        """Appends an item to the managed {class-name} data_property collection."""
        if not isinstance(item, DataProperty):
            raise TypeError("item is of incorrect type.")
        self.__data_property.append(item)

    def remove_from_data_property(self, item):
        """Removes an item from the managed {class-name} data_property collection."""
        if not isinstance(item, DataProperty):
            raise TypeError("item is of incorrect type.")
        self.__data_property.remove(item)


    @property
    def data_status(self):
        """Gets value of {class-name} data_status property."""
        return self.__data_status

    @data_status.setter
    def data_status(self, value):
        if value is not None and not isinstance(value, DataStatusType):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} data_status property."""
        self.__data_status = value

    @data_status.deleter
    def data_status(self, value):
        """Deletes {class-name} data_status property."""
        raise TypeError("Cannot delete {class-name} data_status property.")


    @property
    def description(self):
        """Gets value of {class-name} description property."""
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
    def distribution(self):
        """Gets value of {class-name} distribution property."""
        return self.__distribution

    @distribution.setter
    def distribution(self, value):
        if value is not None and not isinstance(value, DataDistribution):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} distribution property."""
        self.__distribution = value

    @distribution.deleter
    def distribution(self, value):
        """Deletes {class-name} distribution property."""
        raise TypeError("Cannot delete {class-name} distribution property.")


    @property
    def extent(self):
        """Gets value of {class-name} extent property."""
        return self.__extent

    @extent.setter
    def extent(self, value):
        if value is not None and not isinstance(value, DataExtent):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} extent property."""
        self.__extent = value

    @extent.deleter
    def extent(self, value):
        """Deletes {class-name} extent property."""
        raise TypeError("Cannot delete {class-name} extent property.")


    @property
    def geometry_model(self):
        """Gets value of {class-name} geometry_model property."""
        return self.__geometry_model

    @geometry_model.setter
    def geometry_model(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} geometry_model property."""
        self.__geometry_model = value

    @geometry_model.deleter
    def geometry_model(self, value):
        """Deletes {class-name} geometry_model property."""
        raise TypeError("Cannot delete {class-name} geometry_model property.")


    @property
    def hierarchy_level(self):
        """Gets value of {class-name} hierarchy_level property."""
        return self.__hierarchy_level

    @hierarchy_level.setter
    def hierarchy_level(self, value):
        if value is not None and not isinstance(value, DataHierarchyLevel):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} hierarchy_level property."""
        self.__hierarchy_level = value

    @hierarchy_level.deleter
    def hierarchy_level(self, value):
        """Deletes {class-name} hierarchy_level property."""
        raise TypeError("Cannot delete {class-name} hierarchy_level property.")


    @property
    def keyword(self):
        """Gets value of {class-name} keyword property."""
        return self.__keyword

    @keyword.setter
    def keyword(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} keyword property."""
        self.__keyword = value

    @keyword.deleter
    def keyword(self, value):
        """Deletes {class-name} keyword property."""
        raise TypeError("Cannot delete {class-name} keyword property.")


    @property
    def parent_object(self):
        """Gets value of {class-name} parent_object property."""
        return self.__parent_object

    @parent_object.setter
    def parent_object(self, value):
        if value is not None and not isinstance(value, DataObject):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} parent_object property."""
        self.__parent_object = value

    @parent_object.deleter
    def parent_object(self, value):
        """Deletes {class-name} parent_object property."""
        raise TypeError("Cannot delete {class-name} parent_object property.")


    @property
    def parent_object_reference(self):
        """Gets value of {class-name} parent_object_reference property."""
        return self.__parent_object_reference

    @parent_object_reference.setter
    def parent_object_reference(self, value):
        if value is not None and not isinstance(value, CimReference):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} parent_object_reference property."""
        self.__parent_object_reference = value

    @parent_object_reference.deleter
    def parent_object_reference(self, value):
        """Deletes {class-name} parent_object_reference property."""
        raise TypeError("Cannot delete {class-name} parent_object_reference property.")


    @property
    def restriction(self):
        """Gets value of {class-name} restriction property."""
        return list(self.__restriction)

    @restriction.setter
    def restriction(self, value):
        """Sets value of {class-name} restriction property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__restriction = []
        for i in value:
            self.append_to_restriction(i)

    @restriction.deleter
    def restriction(self, value):
        """Deletes {class-name} restriction property."""
        raise TypeError("Cannot delete {class-name} restriction property.")

    def append_to_restriction(self, item):
        """Appends an item to the managed {class-name} restriction collection."""
        if not isinstance(item, DataRestriction):
            raise TypeError("item is of incorrect type.")
        self.__restriction.append(item)

    def remove_from_restriction(self, item):
        """Removes an item from the managed {class-name} restriction collection."""
        if not isinstance(item, DataRestriction):
            raise TypeError("item is of incorrect type.")
        self.__restriction.remove(item)


    @property
    def source_simulation(self):
        """Gets value of {class-name} source_simulation property."""
        return self.__source_simulation

    @source_simulation.setter
    def source_simulation(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} source_simulation property."""
        self.__source_simulation = value

    @source_simulation.deleter
    def source_simulation(self, value):
        """Deletes {class-name} source_simulation property."""
        raise TypeError("Cannot delete {class-name} source_simulation property.")


    @property
    def storage(self):
        """Gets value of {class-name} storage property."""
        return list(self.__storage)

    @storage.setter
    def storage(self, value):
        """Sets value of {class-name} storage property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__storage = []
        for i in value:
            self.append_to_storage(i)

    @storage.deleter
    def storage(self, value):
        """Deletes {class-name} storage property."""
        raise TypeError("Cannot delete {class-name} storage property.")

    def append_to_storage(self, item):
        """Appends an item to the managed {class-name} storage collection."""
        if not isinstance(item, DataStorage):
            raise TypeError("item is of incorrect type.")
        self.__storage.append(item)

    def remove_from_storage(self, item):
        """Removes an item from the managed {class-name} storage collection."""
        if not isinstance(item, DataStorage):
            raise TypeError("item is of incorrect type.")
        self.__storage.remove(item)



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
        d = dict(super(DataObject, self).as_dict())
        append(d, 'acronym', self.__acronym, False, True, False)
        append(d, 'child_object', self.__child_object, True, False, False)
        append(d, 'cim_info', self.__cim_info, False, False, False)
        append(d, 'citations', self.__citations, True, False, False)
        append(d, 'content', self.__content, True, False, False)
        append(d, 'data_property', self.__data_property, True, False, False)
        append(d, 'data_status', self.__data_status, False, False, False)
        append(d, 'description', self.__description, False, True, False)
        append(d, 'distribution', self.__distribution, False, False, False)
        append(d, 'extent', self.__extent, False, False, False)
        append(d, 'geometry_model', self.__geometry_model, False, True, False)
        append(d, 'hierarchy_level', self.__hierarchy_level, False, False, False)
        append(d, 'keyword', self.__keyword, False, True, False)
        append(d, 'parent_object', self.__parent_object, False, False, False)
        append(d, 'parent_object_reference', self.__parent_object_reference, False, False, False)
        append(d, 'restriction', self.__restriction, True, False, False)
        append(d, 'source_simulation', self.__source_simulation, False, True, False)
        append(d, 'storage', self.__storage, True, False, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = DataObject()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('data.DataObject', e)
