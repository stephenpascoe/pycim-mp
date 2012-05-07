"""
CIM v1.5 software package classes.
"""
# Module exports.
__all__ = ["classes"]


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"




def _component_language():
    """Creates and returns instance of component_language class."""
    return {
        'type' : 'class',
        'name' : 'component_language',
        'base' : None,
        'abstract' : False,
        'doc' : 'Details of the programming language a component is written in. There is an assumption that all EntryPoints use the same ComponentLanguage.',
        'properties' : [
            ('name', 'str', '1.1', 'The name of the language.'),
            ('properties', 'software.component_language_property', '0.N', None),
        ],
        'decodings' : [

        ]
    }


def _component_language_property():
    """Creates and returns instance of component_language_property class."""
    return {
        'type' : 'class',
        'name' : 'component_language_property',
        'base' : 'shared.property',
        'abstract' : False,
        'doc' : 'This provides a place to include language-specific information. Every property is basically a name/value pair, where the names are things like: moduleName, reservedUnits, reservedNames (these are all examples of Fortran-specific properties).',
        'properties' : [

        ],
        'decodings' : [

        ]
    }


def _component_property():
    """Creates and returns instance of _component_property class."""
    return {
        'type' : 'class',
        'name' : 'component_property',
        'base' : 'shared.data_source',
        'abstract' : False,
        'doc' : 'ComponentProperties include things that a component simulates (ie: pressure, humidity) and things that prescribe that simulation (ie: gravity, choice of advection scheme). Note that this is a specialisation of shared::DataSource. data::DataObject is also a specialisation of shared::DataSource. This allows software::Connections and/or activity::Conformance to refer to either ComponentProperties or DataObjects.',
        'properties' : [
            ('component_properties', 'software.component_property', '0.N', None),
            ('citations', 'shared.citation', '0.N', None),
            ('description', 'str', '0.1', None),
            # TODO define type
            ('grid', 'str', '0.1', 'A reference to the grid that is used by this component.'),
            ('intent', 'software.component_property_intent_type', '0.1', 'The direction that this property is intended to be coupled: in, out, or inout.'),
            ('is_represented', 'bool', '1.1', 'When set to false, means that this property is not used by the component. Covers the case when, for instance, a modeler chooses not to represent some property in their model. (But still allows meaningful comparisons between components which _do_ model this property.)'),
            ('long_name', 'str', '0.1', None),
            ('short_name', 'str', '1.1', None),
            # TODO define type
            ('standard_names', 'str', '0.N', None),
            ('units', 'shared.unit_type', '0.1', 'The standard name that this property is known as (for example, its CF name).'),
            # TODO clarify confusion with values collection
            ('value', 'str', '0.1', None),
            ('values', 'str', '0.N', 'The value of the property (not applicable to fields).'),
        ],
        'decodings' : [
            ('component_properties', 'child::cim:componentProperty'),
            ('citations', 'child::cim:citation'),
            ('description', 'child::cim:description/text()'),
            ('grid', None),
            ('intent', 'self::cim:componentProperty/@intent'),
            ('is_represented', 'self::cim:componentProperty/@represented'),
            ('long_name', 'child::cim:longName/text()'),
            ('short_name', 'child::cim:shortName/text()'),
            ('standard_names', 'child::cim:standardName/@value'),
            ('units', 'child::cim:units/@value'),
            # TODO clarify.
            ('value', 'child::cim:value/text()'),
            ('values', None),
        ]
    }


def _composition():
    """Creates and returns instance of composition class."""
    return {
        'type' : 'class',
        'name' : 'composition',
        'base' : None,
        'abstract' : False,
        'doc' : 'The set of Couplings used by a Component. Couplings can only occur between child components. That is, a composition must belong to an ancestor component of the components whose fields are being connected.',
        'properties' : [
            ('couplings', 'str', '0.N', None),
            ('description', 'str', '0.1', None),
        ],
        'decodings' : [

        ]
    }


def _connection():
    """Creates and returns instance of connection class."""
    return {
        'type' : 'class',
        'name' : 'connection',
        'base' : None,
        'abstract' : False,
        'doc' : 'A Connection represents a link from a source DataSource to a target DataSource.  These can either be ComponentProperties (ie: the values come from an internal component) or DataObjects (ie: the values come from an external file).   It can be associated with another software component (a transformer).  If present, the rate, lag, timeTransformation, and spatialRegridding override that of the parent coupling.  Note that there is the potential for multiple connectionSource & connectionTarget and multiple couplingSources & couplingTargets.  This may lead users to wonder how to match up a connection source (a ComponentProperty) with its coupling source (a SoftwareComponent). Clever logic is not required though; because the sources and targets are listed by reference, they can be found in a CIM document and the parent can be navigated to from there - there is no need to consult the source or target of the coupling.',
        'properties' : [
            ('properties', 'software.connection_property', '0.N', None),
            ('sources', 'software.connection_endpoint', '0.N', 'The source property being connected.  (note that there can be multiple sources)  This is optional; the file/component source may have already been specified by the couplingSource.'),
            ('target', 'software.connection_endpoint', '0.1', 'The target property being connected.  This is optional to support the way that input is handled in the CMIP5 questionnaire.'),
            ('description', 'str', '0.1', None),
            ('priming', 'shared.data_source', '0.1', 'A priming source is one that is active on the first available timestep only (before "proper" coupling can ocurr). It can either be described here explicitly, or else a separate coupling/connection with a timing profile that is active on only the first timestep can be created.'),
            ('priming_reference', 'shared.cim_reference', '0.1', None),
            ('spatial_regridding', 'software.spatial_regridding', '0.N', 'Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid)'),
            ('time_lag', 'str', '0.1', 'The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time.'),
            ('time_profile', 'software.timing', '0.1', 'All information having to do with the rate of this connection; the times that it is active.  This overrides any rate of a Coupling.'),
            ('time_transformation', 'software.time_transformation', '0.1', 'Temporal transformation performed on the coupling field before or after regridding onto the target grid.'),
            ('transformers', 'software.processor_component', '0.N', 'An "in-line" transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here.'),
            ('transformers_references', 'shared.cim_reference', '0.N', None),
            ('type', 'software.connection_type', '0.1', 'The type of Connection'),
        ],
        'decodings' : [
            ('properties', 'child::cim:connectionProperty'),
            ('sources', 'child::cim:connectionSource'),
            ('target', 'child::cim:connectionTarget'),
            ('description', 'child::cim:description/text()'),
            ('priming', 'child::cim:priming/cim:priming/cim:dataObject', 'data.data_object'),
            ('priming', 'child::cim:priming/cim:priming/cim:dataContent', 'data.data_content'),
            ('priming', 'child::cim:priming/cim:priming/cim:componentProperty', 'software.component_property'),
            ('priming', 'child::cim:priming/cim:priming/cim:softwareComponent', 'software.model_component'),
            ('priming', 'child::cim:priming/cim:priming/cim:softwareComponent', 'software.processor_component'),
            ('priming_reference', 'child::cim:priming/cim:reference'),
            ('spatial_regridding', 'child::cim:spatialRegridding'),
            ('time_lag', 'child::cim:timeLag'),
            ('time_profile', 'child::cim:timeProfile'),
            ('time_transformation', 'child::cim:timeTransformation'),
            ('transformers', 'child::cim:transformer/cim:processorComponent'),
            ('transformers_references', 'child::cim:transformer/cim:reference'),
            ('type', 'child::cim:type/@value'),
        ]
    }


def _connection_endpoint():
    """Creates and returns instance of connection_endpoint class."""
    return {
        'type' : 'class',
        'name' : 'connection_endpoint',
        'base' : None,
        'abstract' : False,
        'doc' : 'The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).',
        'properties' : [
            ('properties', 'software.connection_property', '0.N', 'The place to describe features specific to the source/target of a connection.'),
            ('data_source', 'shared.data_source', '0.1', None),
            ('data_source_reference', 'shared.cim_reference', '0.1', None),
            ('instance_id', 'str', '0.1', 'If the same datasource is used more than once in a coupled model then a method for identifying which particular instance is being referenced is needed (for BFG).'),
        ],
        'decodings' : [
            ('properties', 'child::cim:connectionProperty'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:dataObject', 'data.data_object'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:dataContent', 'data.data_content'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:componentProperty', 'software.component_property'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:softwareComponent', 'software.model_component'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:softwareComponent', 'software.processor_component'),
            ('data_source_reference', 'child::cim:dataSource/cim:reference'),
            ('instance_id', 'child::cim:instanceID'),
        ]
    }


def _connection_property():
    """Creates and returns instance of connection_property class."""
    return {
        'type' : 'class',
        'name' : 'connection_property',
        'base' : 'shared.property',
        'abstract' : False,
        'doc' : 'A ConnectionProperty is a name/value pair used to specify OASIS-specific properties.',
        'properties' : [

        ],
        'decodings' : [

        ]
    }


def _coupling():
    """Creates and returns instance of coupling class."""
    return {
        'type' : 'class',
        'name' : 'coupling',
        'base' : None,
        'abstract' : False,
        'doc' : 'A coupling represents a set of Connections between a source and target component. Couplings can be complete or incomplete. If they are complete then they must include all Connections between model properties. If they are incomplete then the connections can be underspecified or not listed at all.',
        'properties' : [
            ('connections', 'software.connection', '0.N', None),
            ('properties', 'software.coupling_property', '0.N', None),
            ('sources', 'software.coupling_endpoint', '1.N', 'The source component of the coupling. (note that there can be multiple sources).'),
            ('target', 'software.coupling_endpoint', '1.1', 'The target component of the coupling.'),
            ('description', 'str', '0.1', 'A free-text description of the coupling.'),
            ('is_fully_specified', 'bool', '1.1', 'If true then the coupling is fully-specified.  If false then not every Connection has been described within the coupling.'),
            ('purpose', 'shared.data_purpose', '1.1', None),
            ('priming', 'shared.data_source', '0.1', 'A priming source is one that is active on the first available timestep only (before "proper" coupling can ocurr). It can either be described here explicitly, or else a separate coupling/connection with a timing profile that is active on only the first timestep can be created.'),
            ('priming_reference', 'shared.cim_reference', '0.1', None),
            ('spatial_regriddings', 'software.spatial_regridding', '0.N', 'Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).'),
            ('time_profile', 'software.timing', '0.1', 'Describes how often the coupling takes place.'),
            ('time_lag', 'software.time_lag', '0.1', 'The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time.'),
            ('time_transformation', 'software.time_transformation', '0.1', 'Temporal transformation performed on the coupling field before or after regridding onto the target grid.'),
            ('transformers', 'software.processor_component', '0.N', 'An "in-line" transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here.'),
            ('transformers_references', 'shared.cim_reference', '0.N', None),
            ('type', 'software.connection_type', '0.1', 'Describes the method of coupling.'),
        ],
        'decodings' : [
            ('connections', 'child::cim:connection'),
            ('properties', 'child::cim:couplingProperty'),
            ('sources', 'child::cim:couplingSource'),
            ('target', 'child::cim:couplingTarget'),
            ('description', 'child::cim:description/text()'),
            ('is_fully_specified', '@fullySpecified'),
            ('priming', 'child::cim:priming/cim:priming/cim:dataObject', 'data.data_object'),
            ('priming', 'child::cim:priming/cim:priming/cim:dataContent', 'data.data_content'),
            ('priming', 'child::cim:priming/cim:priming/cim:componentProperty', 'software.component_property'),
            ('priming', 'child::cim:priming/cim:priming/cim:softwareComponent', 'software.model_component'),
            ('priming', 'child::cim:priming/cim:priming/cim:softwareComponent', 'software.processor_component'),
            ('priming_reference', 'child::cim:priming/cim:reference'),
            ('purpose', '@purpose'),
            ('spatial_regriddings', 'child::cim:spatialRegridding'),
            ('time_lag', 'child::cim:timeLag'),
            ('time_profile', 'child::cim:timeProfile'),
            ('time_transformation', 'child::cim:timeTransformation'),
            ('transformers', 'child::cim:transformer/cim:processorComponent'),
            ('transformers_references', 'child::cim:transformer/cim:reference'),
            ('type', 'child::cim:type/@value'),
        ]
    }


def _coupling_endpoint():
    """Creates and returns instance of coupling_endpoint class."""
    return {
        'type' : 'class',
        'name' : 'coupling_endpoint',
        'base' : None,
        'abstract' : False,
        'doc' : 'The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).',
        'properties' : [
            ('properties', 'software.coupling_property', '0.N', 'A place to describe features specific to the source/target of a coupling'),
            ('data_source', 'shared.data_source', '0.1', None),
            ('data_source_reference', 'shared.cim_reference', '0.1', None),
            ('instance_id', 'str', '0.1', 'If the same datasource is used more than once in a coupled model then a method for identifying which particular instance is being referenced is needed (for BFG).'),
        ],
        'decodings' : [
            ('properties', 'child::cim:couplingProperty'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:dataObject', 'data.data_object'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:dataContent', 'data.data_content'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:componentProperty', 'software.component_property'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:softwareComponent', 'software.model_component'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:softwareComponent', 'software.processor_component'),
            ('data_source_reference', 'child::cim:dataSource/cim:reference'),
            ('instance_id', 'child::cim:instanceID'),
        ]
    }


def _coupling_property():
    """Creates and returns instance of coupling_property class."""
    return {
        'type' : 'class',
        'name' : 'coupling_property',
        'base' : 'shared.property',
        'abstract' : False,
        'doc' : 'A CouplingProperty is a name/value pair used to specify OASIS-specific properties.',
        'properties' : [

        ],
        'decodings' : [

        ]
    }


def _deployment():
    """Creates and returns instance of deployment class."""
    return {
        'type' : 'class',
        'name' : 'deployment',
        'base' : None,
        'abstract' : False,
        'doc' : 'Gives information about the technical properties of a component: what machine it was run on, which compilers were used, how it was parallised, etc. A deployment basically associates a deploymentDate with a Platform. A deployment only exists if something has been deployed. A platform, in contrast, can exist independently, waiting to be used in deployments.',
        'properties' : [
            ('deployment_date', 'datetime', '0.1', None),
            ('description', 'str', '0.1', None),
            ('parallelisation', 'software.parallelisation', '0.1', None),
            ('platform', 'shared.platform', '0.1', 'The platform that this deployment has been run on. It is optional to allow for "unconfigured" models, that nonetheless specify their parallelisation constraints (a feature needed by OASIS).'),
            ('platform_reference', 'shared.cim_reference', '0.1', None),
            ('executable_name', 'str', '0.1', None),
            ('executable_arguments', 'str', '0.N', None),
        ],
        'decodings' : [
            ('deployment_date', 'child::cim:deploymentDate/text()'),
            ('description', 'child::cim:description/text()'),            
            ('parallelisation', 'child::cim:parallelisation'),
            ('platform', 'child::cim:platform/cim:platform'),
            ('platform_reference', 'child::cim:platform/cim:reference'),
            ('executable_name', 'child::cim:executableName/text()'),
            ('executable_arguments', 'child::cim:executableArgument/text()'),
        ]
    }


def _entry_point():
    """Creates and returns instance of entry_point class."""
    # TODO define
    return {
        'type' : 'class',
        'name' : 'entry_point',
        'base' : None,
        'abstract' : False,
        'doc' : 'Describes a function or subroutine of a SoftwareComponent. BFG will use these EntryPoints to define a schedule of subroutine calls for a coupled model. Currently, a very basic schedule can be approximated by using the "proceeds" and "follows" attributes, however a more complete system is required for full BFG compatibility. Every EntryPoint can have a set of arguments associated with it. These reference (previously defined) ComponentProperties.',
        'properties' : [
            ('name', 'str', '0.1', None),
        ],
        'decodings' : [

        ]
    }


def _model_component():
    """Creates and returns instance of model_component class."""
    return {
        'type' : 'class',
        'name' : 'model_component',
        'base' : 'software.software_component',
        'abstract' : False,
        'doc' : 'A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.',
        'properties' : [
            ('cim_info', 'shared.cim_info', '1.1', None),
            ('types', 'software.model_component_type', '1.N', 'Describes the type of component. There can be multiple types.'),
            ('timing', 'software.timing', '0.1', 'Describes information about how this component simulates time.'),
            ('activity', 'activity.activity', '0.1', None),
        ],
        'decodings' : [
            ('cim_info', 'self::cim:modelComponent'),
            ('types', 'child::cim:type/@value'),
        ]
    }


def _parallelisation():
    """Creates and returns instance of parallelisation class."""
    return {
        'type' : 'class',
        'name' : 'parallelisation',
        'base' : None,
        'abstract' : False,
        'doc' : 'Describes how a deployment has been parallelised across a computing platform.',
        'properties' : [
            ('processes', 'int', '1.1', None),
            ('ranks', 'software.rank', '0.N', None),
        ],
        'decodings' : [
            ('processes', 'child::cim:processes/text()'),
            ('ranks', 'child::cim:rank'),
        ]
    }


def _processor_component():
    """Creates and returns instance of processor_component class."""
    return {
        'type' : 'class',
        'name' : 'processor_component',
        'base' : 'software.software_component',
        'abstract' : False,
        'doc' : 'A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.',
        'properties' : [
            ('cim_info', 'shared.cim_info', '1.1', None),
        ],
        'decodings' : [
            ('cim_info', 'self::cim:modelComponent'),
        ]
    }


def _rank():
    """Creates and returns instance of rank class."""
    return {
        'type' : 'class',
        'name' : 'rank',
        'base' : None,
        'abstract' : False,
        'doc' : None,
        'properties' : [
            ('value', 'int', '0.1', None),
            ('min', 'int', '0.1', None),
            ('max', 'int', '0.1', None),
            ('increment', 'int', '0.1', None),
        ],
        'decodings' : [
            ('value', 'child::cim:rankValue'),
            ('min', 'child::cim:rankMin'),
            ('max', 'child::cim:rankMax'),
            ('increment', 'child::cim:rankIncrement'),
        ]
    }


def _software_component():
    """Creates and returns instance of software_component class."""
    return {
        'type' : 'class',
        'name' : 'software_component',
        'base' : 'shared.data_source',
        'abstract' : False,
        'doc' : 'A SofwareCompnent is an abstract component from which all other components derive. It represents an element that takes input data and generates output data. A SoftwareCompnent can include nested "child" components. Every component can have "componentProperties" which describe the scientific properties that a component simulates (for example, temperature, pressure, etc.) and the numerical properties that influence how a component performs its simulation (for example, the force of gravity). A SoftwareComponent can also have a Deployment, which describes how software is deployed onto computing resources. And a SoftwareComponent can have a composition, which describes how ComponentProperties are coupled together either to/from other SoftwareComponents or external data files. The properties specified by a component\'s composition must be owned by that component or a child of that component; child components cannot couple together their parents\' properties.',
        'properties' : [
            ('short_name', 'str', '1.1', 'The name of the model (that is used internally).'),
            ('long_name', 'str', '0.1', 'The name of the model (that is recognized externally).'),
            ('description', 'str', '0.1', 'A free-text description of the component.'),
            ('license', 'shared.license', '0.1', 'The license held by this piece of software.'),
            ('component_properties', 'software.component_property', '0.N', 'The properties that this model simulates and/or couples.'),
            ('scientific_properties', 'software.component_property', '0.N', 'The properties that this model simulates and/or couples. ScientificProperties contain those properties that describe _how_ a model simulates. (Although, the distinction between numerical and scientific may be unused - all properties can be stored under the generic "ComponentProperties" attribute).'),
            ('numerical_properties', 'software.component_property', '0.N', 'The properties that this model simulates and/or couples. NumericalProperties contain those properties that describe _what_ a model simulates. (Although, the distinction between numerical and scientific may be unused - all properties can be stored under the generic "ComponentProperties" attribute).'),
            ('responsible_parties', 'shared.responsible_party', '0.N', None),
            ('release_date', 'datetime', '0.1', 'The date of publication of the software component code (as opposed to the date of publication of the metadata document, or the date of deployment of the model)'),
            ('previous_version', 'str', '0.1', None),
            ('funding_sources', 'str', '0.N', 'The entities that funded this software component.'),
            ('citations', 'shared.citation', '0.N', None),
            ('online_resource', 'uri', '0.1', 'Provides a URL location for this model.'),
            ('component_language', 'software.component_language', '0.1', None),
            ('grid', 'grids.grid_spec', '0.1', 'A reference to the grid that is used by this component.'),
            ('composition', 'software.composition', '0.1', None),
            ('child_components', 'software.software_component', '0.N', None),
            ('parent_component', 'software.software_component', '0.1', None),
            ('dependencies', 'software.entry_point', '0.N', None),
            ('deployments', 'software.deployment', '0.N', None),
            ('is_embedded', 'bool', '0.1', 'An embedded component cannot exist on its own as an atomic piece of software; instead it is embedded within another (parent) component. When embedded equals "true", the SoftwareComponent has a corresponding piece of software (otherwise it is acting as a "virtual" component which may be inexorably nested within a piece of software along with several other virtual components).'),
            ('coupling_framework', 'software.coupling_framework_type', '0.1', 'The coupling framework that this entire component conforms to.'),
        ],
        'decodings' : [
            ('child_components', 'child::cim:childComponent/cim:modelComponent', 'software.model_component'),
            ('child_components', 'child::cim:childComponent/cim:processorComponent', 'software.processor_component'),
            ('citations', 'child::cim:citation'),
            ('component_properties', 'child::cim:componentProperties/cim:componentProperty'),
            ('description', 'child::cim:description/text()'),
            ('long_name', 'child::cim:longName/text()'),
            ('release_date', 'child::cim:releaseDate/text()'),
            ('responsible_parties', 'child::cim:responsibleParty'),
            ('short_name', 'child::cim:shortName/text()'),
        ]
    }


def _spatial_regridding():
    """Creates and returns instance of spatial_regridding class."""
    return {
        'type' : 'class',
        'name' : 'spatial_regridding',
        'base' : None,
        'abstract' : False,
        'doc' : 'Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.',
        'properties' : [
            ('dimension', 'software.spatial_regridding_dimension_type', '0.1', None),
            ('properties', 'software.spatial_regridding_property', '0.N', None),
            ('standard_method', 'software.spatial_regridding_standard_method_type', '0.1', None),
            ('user_method', 'software.spatial_regridding_user_method', '0.1', None),
        ],
        'decodings' : [
            ('dimension', 'child::cim:spatialRegriddingDimension/text()'),
            ('properties', 'child::cim:spatialRegriddingProperty'),
            ('standard_method', 'child::cim:spatialRegriddingStandardMethod/text()'),
            ('user_method', 'child::cim:spatialRegriddingUserMethod'),
        ]
    }


def _spatial_regridding_property():
    """Creates and returns instance of spatial_regridding_property class."""
    return {
        'type' : 'class',
        'name' : 'spatial_regridding_property',
        'base' : 'shared.property',
        'abstract' : False,
        'doc' : 'Used for OASIS-specific regridding information (ie: masked, order, normalisation, etc.)',
        'properties' : [ ],
        'decodings' : [ ]
    }


def _spatial_regridding_user_method():
    """Creates and returns instance of spatial_regridding_user_method class."""
    return {
        'type' : 'class',
        'name' : 'spatial_regridding_user_method',
        'base' : None,
        'abstract' : False,
        'doc' : 'Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.',
        'properties' : [
            ('file', 'data.data_object', '0.1', None),
            ('file_reference', 'shared.cim_reference', '0.1', None),
            ('name', 'str', '1.1', None),
        ],
        'decodings' : [
            ('file', 'child::cim:file/cim:dataObject'),
            ('file_reference', 'child::cim:file/cim:reference'),
            ('name', 'child::cim:name/text()'),
        ]
    }


def _time_lag():
    """Creates and returns instance of time_lag class."""
    return {
        'type' : 'class',
        'name' : 'time_lag',
        'base' : None,
        'abstract' : False,
        'doc' : 'The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.',
        'properties' : [
            ('value', 'int', '0.1', None),
            ('units', 'software.timing_units', '0.1', None),
        ],
        'decodings' : [
            ('value', 'child::cim:value/text()'),
            ('units', '@units'),
        ]
    }


def _timing():
    """Creates and returns instance of timing class."""
    return {
        'type' : 'class',
        'name' : 'timing',
        'base' : None,
        'abstract' : False,
        'doc' : 'Provides information about the rate of couplings and connections and/or the timing characteristics of individual components - for example, the start and stop times that the component was run for or the units of time that a component is able to model (in a single timestep).',
        'properties' : [
            ('end', 'datetime', '0.1', None),
            ('is_variable_rate', 'bool', '0.1', 'Describes whether or not the model supports a variable timestep. If set to true, then rate should not be specified.'),
            ('rate', 'int', '0.1', None),
            ('start', 'datetime', '0.1', None),
            ('units', 'software.timing_units', '0.1', None),
        ],
        'decodings' : [
            ('end', 'child::cim:end/text()'),
            ('is_variable_rate', '@variableRate'),
            ('rate', 'child::cim:rate/text()'),
            ('start', 'child::cim:start/text()'),
            ('units', '@units'),
        ]
    }

def _time_transformation():
    """Creates and returns instance of time_transformation class."""
    return {
        'type' : 'class',
        'name' : 'time_transformation',
        'base' : None,
        'abstract' : False,
        'doc' : 'The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.',
        'properties' : [
            ('description', 'str', '0.1', None),
            ('mapping_type', 'software.time_mapping_type', '1.1', None),
        ],
        'decodings' : [
            ('description', 'child::cim:description/text()'),
            ('mapping_type', 'child::cim:mappingType/@value'),
        ]
    }
    

# Set of package classes.
classes = [
    _component_language(),
    _component_language_property(),
    _component_property(),
    _composition(),
    _connection(),
    _connection_endpoint(),
    _connection_property(),
    _coupling(),
    _coupling_endpoint(),
    _coupling_property(),
    _deployment(),
    _entry_point(),
    _model_component(),
    _parallelisation(),
    _processor_component(),
    _rank(),
    _software_component(),
    _spatial_regridding(),
    _spatial_regridding_property(),
    _spatial_regridding_user_method(),
    _time_lag(),
    _time_transformation(),
    _timing(),
]
