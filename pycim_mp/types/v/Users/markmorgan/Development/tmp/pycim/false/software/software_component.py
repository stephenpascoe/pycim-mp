"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.773703.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.shared.citation import Citation
from cim.v1_5.types.shared.data_source import DataSource
from cim.v1_5.types.shared.license import License
from cim.v1_5.types.shared.responsible_party import ResponsibleParty
from cim.v1_5.types.software.component_language import ComponentLanguage
from cim.v1_5.types.software.component_property import ComponentProperty
from cim.v1_5.types.software.composition import Composition
from cim.v1_5.types.software.coupling_framework_type import CouplingFrameworkType
from cim.v1_5.types.software.deployment import Deployment
from cim.v1_5.types.software.entry_point import EntryPoint


# Module exports.
__all__ = ['SoftwareComponent']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.773703$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class SoftwareComponent(DataSource):
    """A class within the cim v1.5 type system.

    A SofwareCompnent is an abstract component from which all other components derive. It represents an element that takes input data and generates output data. A SoftwareCompnent can include nested "child" components. Every component can have "componentProperties" which describe the scientific properties that a component simulates (for example, temperature, pressure, etc.) and the numerical properties that influence how a component performs its simulation (for example, the force of gravity). A SoftwareComponent can also have a Deployment, which describes how software is deployed onto computing resources. And a SoftwareComponent can have a composition, which describes how ComponentProperties are coupled together either to/from other SoftwareComponents or external data files. The properties specified by a component's composition must be owned by that component or a child of that component; child components cannot couple together their parents' properties.
    """
    def __init__(self):
        """Constructor"""
        super(SoftwareComponent, self).__init__()

        self.__child_components = []                                # type = software.SoftwareComponent
        self.__citations = []                                       # type = shared.Citation
        self.__component_language = None                            # type = software.ComponentLanguage
        self.__component_properties = []                            # type = software.ComponentProperty
        self.__composition = None                                   # type = software.Composition
        self.__coupling_framework = None                            # type = software.CouplingFrameworkType
        self.__dependencies = []                                    # type = software.EntryPoint
        self.__deployments = []                                     # type = software.Deployment
        self.__description = None                                   # type = str
        self.__funding_sources = []                                 # type = str
        self.__grid = None                                          # type = str
        self.__is_embedded = None                                   # type = bool
        self.__license = None                                       # type = shared.License
        self.__long_name = None                                     # type = str
        self.__numerical_properties = []                            # type = software.ComponentProperty
        self.__online_resource = None                               # type = str
        self.__parent_component = None                              # type = software.SoftwareComponent
        self.__previous_version = None                              # type = str
        self.__release_date = None                                  # type = datetime.datetime
        self.__responsible_parties = []                             # type = shared.ResponsibleParty
        self.__scientific_properties = []                           # type = software.ComponentProperty
        self.__short_name = str()                                   # type = str


    @property
    def child_components(self):
        """Gets value of {class-name} child_components property."""
        return list(self.__child_components)

    @child_components.setter
    def child_components(self, value):
        """Sets value of {class-name} child_components property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__child_components = []
        for i in value:
            self.append_to_child_components(i)

    @child_components.deleter
    def child_components(self, value):
        """Deletes {class-name} child_components property."""
        raise TypeError("Cannot delete {class-name} child_components property.")

    def append_to_child_components(self, item):
        """Appends an item to the managed {class-name} child_components collection."""
        if not isinstance(item, SoftwareComponent):
            raise TypeError("item is of incorrect type.")
        self.__child_components.append(item)

    def remove_from_child_components(self, item):
        """Removes an item from the managed {class-name} child_components collection."""
        if not isinstance(item, SoftwareComponent):
            raise TypeError("item is of incorrect type.")
        self.__child_components.remove(item)


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
    def component_language(self):
        """Gets value of {class-name} component_language property."""
        return self.__component_language

    @component_language.setter
    def component_language(self, value):
        if value is not None and not isinstance(value, ComponentLanguage):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} component_language property."""
        self.__component_language = value

    @component_language.deleter
    def component_language(self, value):
        """Deletes {class-name} component_language property."""
        raise TypeError("Cannot delete {class-name} component_language property.")


    @property
    def component_properties(self):
        """Gets value of {class-name} component_properties property.

        The properties that this model simulates and/or couples."""
        return list(self.__component_properties)

    @component_properties.setter
    def component_properties(self, value):
        """Sets value of {class-name} component_properties property.

        The properties that this model simulates and/or couples."""
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
    def composition(self):
        """Gets value of {class-name} composition property."""
        return self.__composition

    @composition.setter
    def composition(self, value):
        if value is not None and not isinstance(value, Composition):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} composition property."""
        self.__composition = value

    @composition.deleter
    def composition(self, value):
        """Deletes {class-name} composition property."""
        raise TypeError("Cannot delete {class-name} composition property.")


    @property
    def coupling_framework(self):
        """Gets value of {class-name} coupling_framework property.

        The coupling framework that this entire component conforms to."""
        return self.__coupling_framework

    @coupling_framework.setter
    def coupling_framework(self, value):
        if value is not None and not isinstance(value, CouplingFrameworkType):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} coupling_framework property."""
        self.__coupling_framework = value

    @coupling_framework.deleter
    def coupling_framework(self, value):
        """Deletes {class-name} coupling_framework property."""
        raise TypeError("Cannot delete {class-name} coupling_framework property.")


    @property
    def dependencies(self):
        """Gets value of {class-name} dependencies property."""
        return list(self.__dependencies)

    @dependencies.setter
    def dependencies(self, value):
        """Sets value of {class-name} dependencies property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__dependencies = []
        for i in value:
            self.append_to_dependencies(i)

    @dependencies.deleter
    def dependencies(self, value):
        """Deletes {class-name} dependencies property."""
        raise TypeError("Cannot delete {class-name} dependencies property.")

    def append_to_dependencies(self, item):
        """Appends an item to the managed {class-name} dependencies collection."""
        if not isinstance(item, EntryPoint):
            raise TypeError("item is of incorrect type.")
        self.__dependencies.append(item)

    def remove_from_dependencies(self, item):
        """Removes an item from the managed {class-name} dependencies collection."""
        if not isinstance(item, EntryPoint):
            raise TypeError("item is of incorrect type.")
        self.__dependencies.remove(item)


    @property
    def deployments(self):
        """Gets value of {class-name} deployments property."""
        return list(self.__deployments)

    @deployments.setter
    def deployments(self, value):
        """Sets value of {class-name} deployments property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__deployments = []
        for i in value:
            self.append_to_deployments(i)

    @deployments.deleter
    def deployments(self, value):
        """Deletes {class-name} deployments property."""
        raise TypeError("Cannot delete {class-name} deployments property.")

    def append_to_deployments(self, item):
        """Appends an item to the managed {class-name} deployments collection."""
        if not isinstance(item, Deployment):
            raise TypeError("item is of incorrect type.")
        self.__deployments.append(item)

    def remove_from_deployments(self, item):
        """Removes an item from the managed {class-name} deployments collection."""
        if not isinstance(item, Deployment):
            raise TypeError("item is of incorrect type.")
        self.__deployments.remove(item)


    @property
    def description(self):
        """Gets value of {class-name} description property.

        A free-text description of the component."""
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
    def funding_sources(self):
        """Gets value of {class-name} funding_sources property.

        The entities that funded this software component."""
        return list(self.__funding_sources)

    @funding_sources.setter
    def funding_sources(self, value):
        """Sets value of {class-name} funding_sources property.

        The entities that funded this software component."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__funding_sources = []
        for i in value:
            self.append_to_funding_sources(i)

    @funding_sources.deleter
    def funding_sources(self, value):
        """Deletes {class-name} funding_sources property."""
        raise TypeError("Cannot delete {class-name} funding_sources property.")

    def append_to_funding_sources(self, item):
        """Appends an item to the managed {class-name} funding_sources collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__funding_sources.append(item)

    def remove_from_funding_sources(self, item):
        """Removes an item from the managed {class-name} funding_sources collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__funding_sources.remove(item)


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
    def is_embedded(self):
        """Gets value of {class-name} is_embedded property.

        An embedded component cannot exist on its own as an atomic piece of software; instead it is embedded within another (parent) component. When embedded equals "true", the SoftwareComponent has a corresponding piece of software (otherwise it is acting as a "virtual" component which may be inexorably nested within a piece of software along with several other virtual components)."""
        return self.__is_embedded

    @is_embedded.setter
    def is_embedded(self, value):
        if value is not None and not isinstance(value, bool):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} is_embedded property."""
        self.__is_embedded = value

    @is_embedded.deleter
    def is_embedded(self, value):
        """Deletes {class-name} is_embedded property."""
        raise TypeError("Cannot delete {class-name} is_embedded property.")


    @property
    def license(self):
        """Gets value of {class-name} license property.

        The license held by this piece of software."""
        return self.__license

    @license.setter
    def license(self, value):
        if value is not None and not isinstance(value, License):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} license property."""
        self.__license = value

    @license.deleter
    def license(self, value):
        """Deletes {class-name} license property."""
        raise TypeError("Cannot delete {class-name} license property.")


    @property
    def long_name(self):
        """Gets value of {class-name} long_name property.

        The name of the model (that is recognized externally)."""
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
    def numerical_properties(self):
        """Gets value of {class-name} numerical_properties property.

        The properties that this model simulates and/or couples. NumericalProperties contain those properties that describe _what_ a model simulates. (Although, the distinction between numerical and scientific may be unused - all properties can be stored under the generic "ComponentProperties" attribute)."""
        return list(self.__numerical_properties)

    @numerical_properties.setter
    def numerical_properties(self, value):
        """Sets value of {class-name} numerical_properties property.

        The properties that this model simulates and/or couples. NumericalProperties contain those properties that describe _what_ a model simulates. (Although, the distinction between numerical and scientific may be unused - all properties can be stored under the generic "ComponentProperties" attribute)."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__numerical_properties = []
        for i in value:
            self.append_to_numerical_properties(i)

    @numerical_properties.deleter
    def numerical_properties(self, value):
        """Deletes {class-name} numerical_properties property."""
        raise TypeError("Cannot delete {class-name} numerical_properties property.")

    def append_to_numerical_properties(self, item):
        """Appends an item to the managed {class-name} numerical_properties collection."""
        if not isinstance(item, ComponentProperty):
            raise TypeError("item is of incorrect type.")
        self.__numerical_properties.append(item)

    def remove_from_numerical_properties(self, item):
        """Removes an item from the managed {class-name} numerical_properties collection."""
        if not isinstance(item, ComponentProperty):
            raise TypeError("item is of incorrect type.")
        self.__numerical_properties.remove(item)


    @property
    def online_resource(self):
        """Gets value of {class-name} online_resource property.

        Provides a URL location for this model."""
        return self.__online_resource

    @online_resource.setter
    def online_resource(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} online_resource property."""
        self.__online_resource = value

    @online_resource.deleter
    def online_resource(self, value):
        """Deletes {class-name} online_resource property."""
        raise TypeError("Cannot delete {class-name} online_resource property.")


    @property
    def parent_component(self):
        """Gets value of {class-name} parent_component property."""
        return self.__parent_component

    @parent_component.setter
    def parent_component(self, value):
        if value is not None and not isinstance(value, SoftwareComponent):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} parent_component property."""
        self.__parent_component = value

    @parent_component.deleter
    def parent_component(self, value):
        """Deletes {class-name} parent_component property."""
        raise TypeError("Cannot delete {class-name} parent_component property.")


    @property
    def previous_version(self):
        """Gets value of {class-name} previous_version property."""
        return self.__previous_version

    @previous_version.setter
    def previous_version(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} previous_version property."""
        self.__previous_version = value

    @previous_version.deleter
    def previous_version(self, value):
        """Deletes {class-name} previous_version property."""
        raise TypeError("Cannot delete {class-name} previous_version property.")


    @property
    def release_date(self):
        """Gets value of {class-name} release_date property.

        The date of publication of the software component code (as opposed to the date of publication of the metadata document, or the date of deployment of the model)"""
        return self.__release_date

    @release_date.setter
    def release_date(self, value):
        if value is not None and not isinstance(value, datetime.datetime):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} release_date property."""
        self.__release_date = value

    @release_date.deleter
    def release_date(self, value):
        """Deletes {class-name} release_date property."""
        raise TypeError("Cannot delete {class-name} release_date property.")


    @property
    def responsible_parties(self):
        """Gets value of {class-name} responsible_parties property."""
        return list(self.__responsible_parties)

    @responsible_parties.setter
    def responsible_parties(self, value):
        """Sets value of {class-name} responsible_parties property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__responsible_parties = []
        for i in value:
            self.append_to_responsible_parties(i)

    @responsible_parties.deleter
    def responsible_parties(self, value):
        """Deletes {class-name} responsible_parties property."""
        raise TypeError("Cannot delete {class-name} responsible_parties property.")

    def append_to_responsible_parties(self, item):
        """Appends an item to the managed {class-name} responsible_parties collection."""
        if not isinstance(item, ResponsibleParty):
            raise TypeError("item is of incorrect type.")
        self.__responsible_parties.append(item)

    def remove_from_responsible_parties(self, item):
        """Removes an item from the managed {class-name} responsible_parties collection."""
        if not isinstance(item, ResponsibleParty):
            raise TypeError("item is of incorrect type.")
        self.__responsible_parties.remove(item)


    @property
    def scientific_properties(self):
        """Gets value of {class-name} scientific_properties property.

        The properties that this model simulates and/or couples. ScientificProperties contain those properties that describe _how_ a model simulates. (Although, the distinction between numerical and scientific may be unused - all properties can be stored under the generic "ComponentProperties" attribute)."""
        return list(self.__scientific_properties)

    @scientific_properties.setter
    def scientific_properties(self, value):
        """Sets value of {class-name} scientific_properties property.

        The properties that this model simulates and/or couples. ScientificProperties contain those properties that describe _how_ a model simulates. (Although, the distinction between numerical and scientific may be unused - all properties can be stored under the generic "ComponentProperties" attribute)."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__scientific_properties = []
        for i in value:
            self.append_to_scientific_properties(i)

    @scientific_properties.deleter
    def scientific_properties(self, value):
        """Deletes {class-name} scientific_properties property."""
        raise TypeError("Cannot delete {class-name} scientific_properties property.")

    def append_to_scientific_properties(self, item):
        """Appends an item to the managed {class-name} scientific_properties collection."""
        if not isinstance(item, ComponentProperty):
            raise TypeError("item is of incorrect type.")
        self.__scientific_properties.append(item)

    def remove_from_scientific_properties(self, item):
        """Removes an item from the managed {class-name} scientific_properties collection."""
        if not isinstance(item, ComponentProperty):
            raise TypeError("item is of incorrect type.")
        self.__scientific_properties.remove(item)


    @property
    def short_name(self):
        """Gets value of software component short_name property.

        The name of the model (that is used internally)."""
        return self.__short_name

    @short_name.setter
    def short_name(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of software component short_name property."""
        self.__short_name = value

    @short_name.deleter
    def short_name(self, value):
        """Deletes software component short_name property."""
        raise TypeError("Cannot delete software component short_name property.")



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
        d = dict(super(SoftwareComponent, self).as_dict())
        append(d, 'child_components', self.__child_components, True, False, False)
        append(d, 'citations', self.__citations, True, False, False)
        append(d, 'component_language', self.__component_language, False, False, False)
        append(d, 'component_properties', self.__component_properties, True, False, False)
        append(d, 'composition', self.__composition, False, False, False)
        append(d, 'coupling_framework', self.__coupling_framework, False, False, False)
        append(d, 'dependencies', self.__dependencies, True, False, False)
        append(d, 'deployments', self.__deployments, True, False, False)
        append(d, 'description', self.__description, False, True, False)
        append(d, 'funding_sources', self.__funding_sources, True, True, False)
        append(d, 'grid', self.__grid, False, True, False)
        append(d, 'is_embedded', self.__is_embedded, False, True, False)
        append(d, 'license', self.__license, False, False, False)
        append(d, 'long_name', self.__long_name, False, True, False)
        append(d, 'numerical_properties', self.__numerical_properties, True, False, False)
        append(d, 'online_resource', self.__online_resource, False, True, False)
        append(d, 'parent_component', self.__parent_component, False, False, False)
        append(d, 'previous_version', self.__previous_version, False, True, False)
        append(d, 'release_date', self.__release_date, False, True, False)
        append(d, 'responsible_parties', self.__responsible_parties, True, False, False)
        append(d, 'scientific_properties', self.__scientific_properties, True, False, False)
        append(d, 'short_name', self.__short_name, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = SoftwareComponent()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('software.SoftwareComponent', e)
