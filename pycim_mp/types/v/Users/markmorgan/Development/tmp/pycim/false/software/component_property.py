"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.758936.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.shared.citation import Citation
from cim.v1_5.types.shared.data_source import DataSource
from cim.v1_5.types.shared.unit_type import UnitType
from cim.v1_5.types.software.component_property_intent_type import ComponentPropertyIntentType


# Module exports.
__all__ = ['ComponentProperty']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.758936$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class ComponentProperty(DataSource):
    """A class within the cim v1.5 type system.

    ComponentProperties include things that a component simulates (ie: pressure, humidity) and things that prescribe that simulation (ie: gravity, choice of advection scheme). Note that this is a specialisation of shared::DataSource. data::DataObject is also a specialisation of shared::DataSource. This allows software::Connections and/or activity::Conformance to refer to either ComponentProperties or DataObjects.
    """
    def __init__(self):
        """Constructor"""
        super(ComponentProperty, self).__init__()

        self.__citations = []                                       # type = shared.Citation
        self.__component_properties = []                            # type = software.ComponentProperty
        self.__description = None                                   # type = str
        self.__grid = None                                          # type = str
        self.__intent = None                                        # type = software.ComponentPropertyIntentType
        self.__is_represented = bool()                              # type = bool
        self.__long_name = None                                     # type = str
        self.__short_name = str()                                   # type = str
        self.__standard_names = []                                  # type = str
        self.__units = None                                         # type = shared.UnitType
        self.__value = None                                         # type = str
        self.__values = []                                          # type = str


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
    def component_properties(self):
        """Gets value of {class-name} component_properties property."""
        return list(self.__component_properties)

    @component_properties.setter
    def component_properties(self, value):
        """Sets value of {class-name} component_properties property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__component_properties = []
        for i in value:
            self.append_to_component_properties(i)

    @component_properties.deleter
    def component_properties(self, value):
        """Deletes {class-name} component_properties property."""
        raise TypeError("Cannot delete {class-name} component_properties property.")

    def append_to_component_properties(self, item):
        """Appends an item to the managed {class-name} component_properties collection."""
        if not isinstance(item, ComponentProperty):
            raise TypeError("item is of incorrect type.")
        self.__component_properties.append(item)

    def remove_from_component_properties(self, item):
        """Removes an item from the managed {class-name} component_properties collection."""
        if not isinstance(item, ComponentProperty):
            raise TypeError("item is of incorrect type.")
        self.__component_properties.remove(item)


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
    def grid(self):
        """Gets value of {class-name} grid property.

        A reference to the grid that is used by this component."""
        return self.__grid

    @grid.setter
    def grid(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} grid property."""
        self.__grid = value

    @grid.deleter
    def grid(self, value):
        """Deletes {class-name} grid property."""
        raise TypeError("Cannot delete {class-name} grid property.")


    @property
    def intent(self):
        """Gets value of {class-name} intent property.

        The direction that this property is intended to be coupled: in, out, or inout."""
        return self.__intent

    @intent.setter
    def intent(self, value):
        if value is not None and not isinstance(value, ComponentPropertyIntentType):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} intent property."""
        self.__intent = value

    @intent.deleter
    def intent(self, value):
        """Deletes {class-name} intent property."""
        raise TypeError("Cannot delete {class-name} intent property.")


    @property
    def is_represented(self):
        """Gets value of component property is_represented property.

        When set to false, means that this property is not used by the component. Covers the case when, for instance, a modeler chooses not to represent some property in their model. (But still allows meaningful comparisons between components which _do_ model this property.)"""
        return self.__is_represented

    @is_represented.setter
    def is_represented(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, bool):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of component property is_represented property."""
        self.__is_represented = value

    @is_represented.deleter
    def is_represented(self, value):
        """Deletes component property is_represented property."""
        raise TypeError("Cannot delete component property is_represented property.")


    @property
    def long_name(self):
        """Gets value of {class-name} long_name property."""
        return self.__long_name

    @long_name.setter
    def long_name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} long_name property."""
        self.__long_name = value

    @long_name.deleter
    def long_name(self, value):
        """Deletes {class-name} long_name property."""
        raise TypeError("Cannot delete {class-name} long_name property.")


    @property
    def short_name(self):
        """Gets value of component property short_name property."""
        return self.__short_name

    @short_name.setter
    def short_name(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of component property short_name property."""
        self.__short_name = value

    @short_name.deleter
    def short_name(self, value):
        """Deletes component property short_name property."""
        raise TypeError("Cannot delete component property short_name property.")


    @property
    def standard_names(self):
        """Gets value of {class-name} standard_names property."""
        return list(self.__standard_names)

    @standard_names.setter
    def standard_names(self, value):
        """Sets value of {class-name} standard_names property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__standard_names = []
        for i in value:
            self.append_to_standard_names(i)

    @standard_names.deleter
    def standard_names(self, value):
        """Deletes {class-name} standard_names property."""
        raise TypeError("Cannot delete {class-name} standard_names property.")

    def append_to_standard_names(self, item):
        """Appends an item to the managed {class-name} standard_names collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__standard_names.append(item)

    def remove_from_standard_names(self, item):
        """Removes an item from the managed {class-name} standard_names collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__standard_names.remove(item)


    @property
    def units(self):
        """Gets value of {class-name} units property.

        The standard name that this property is known as (for example, its CF name)."""
        return self.__units

    @units.setter
    def units(self, value):
        if value is not None and not isinstance(value, UnitType):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} units property."""
        self.__units = value

    @units.deleter
    def units(self, value):
        """Deletes {class-name} units property."""
        raise TypeError("Cannot delete {class-name} units property.")


    @property
    def value(self):
        """Gets value of {class-name} value property."""
        return self.__value

    @value.setter
    def value(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} value property."""
        self.__value = value

    @value.deleter
    def value(self, value):
        """Deletes {class-name} value property."""
        raise TypeError("Cannot delete {class-name} value property.")


    @property
    def values(self):
        """Gets value of {class-name} values property.

        The value of the property (not applicable to fields)."""
        return list(self.__values)

    @values.setter
    def values(self, value):
        """Sets value of {class-name} values property.

        The value of the property (not applicable to fields)."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__values = []
        for i in value:
            self.append_to_values(i)

    @values.deleter
    def values(self, value):
        """Deletes {class-name} values property."""
        raise TypeError("Cannot delete {class-name} values property.")

    def append_to_values(self, item):
        """Appends an item to the managed {class-name} values collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__values.append(item)

    def remove_from_values(self, item):
        """Removes an item from the managed {class-name} values collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__values.remove(item)



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
        d = dict(super(ComponentProperty, self).as_dict())
        append(d, 'citations', self.__citations, True, False, False)
        append(d, 'component_properties', self.__component_properties, True, False, False)
        append(d, 'description', self.__description, False, True, False)
        append(d, 'grid', self.__grid, False, True, False)
        append(d, 'intent', self.__intent, False, False, False)
        append(d, 'is_represented', self.__is_represented, False, True, False)
        append(d, 'long_name', self.__long_name, False, True, False)
        append(d, 'short_name', self.__short_name, False, True, False)
        append(d, 'standard_names', self.__standard_names, True, True, False)
        append(d, 'units', self.__units, False, False, False)
        append(d, 'value', self.__value, False, True, False)
        append(d, 'values', self.__values, True, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = ComponentProperty()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('software.ComponentProperty', e)
