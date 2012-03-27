"""
CIM v1.5 activity package classes.
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


def _activity():
    """Creates and returns instance of numerical_experiment class."""
    return {
        'type' : 'class',
        'name' : 'activity',
        'base' : None,
        'abstract' : True,
        'doc' : 'An abstract class used as the parent of MeasurementCampaigns, Projects, Experiments, and NumericalActivities.',
        'properties' : [
            ('funding_sources', 'str', '0.N', 'The entities that funded this activity.'),
            ('projects', 'activity.project_type', '0.N', 'The project(s) that this activity is associated with (ie: CMIP5, AMIP, etc).'),
            ('rationales', 'str', '0.N', 'For what purpose is this activity being performed?'),
            ('responsible_parties', 'shared.responsible_party', '0.N', 'The point of contact(s) for this activity.This includes, among others, the principle investigator.'),
        ],
        'decodings' : [
            ('funding_sources', 'child::cim:fundingSource/text()'),
            ('projects', 'child::cim:project/@value'),
            ('rationales', 'child::cim:rationale/text()'),
            ('responsible_parties', 'child::cim:responsibleParty'),
        ]
    }


def _conformance():
    """Creates and returns instance of conformance class."""
    return {
        'type' : 'class',
        'name' : 'conformance',
        'base' : None,
        'abstract' : False,
        'doc' : 'A conformance class maps how a configured model component met a specific numerical requirement.  For example, for a double CO2 boundary condition, a model component might read a CO2 dataset in which CO2 has been doubled, or it might modify a parameterisation (presumably with a factor of two somewhere).  So, the conformance links a requirement to a DataSource (which can be either an actual DataObject or a property of a model component).  In some cases a model/simulation may _naturally_ conform to a requirement.  In this case there would be no reference to a DataSource but the conformant attribute would be true.  If something is purpopsefully non-conformant then the conformant attribute would be false.',
        'properties' : [
            ('description', 'str', '0.1', None),
            ('frequency', 'activity.frequency_type', '0.1', None),
            ('is_conformant', 'bool', '1.1', 'Records whether or not this conformance satisfies the requirement.  A simulation should have at least one conformance mapping to every experimental requirement.  If a simulation satisfies the requirement - the usual case - then conformant should have a value of true.  If conformant is true but there is no reference to a source for the conformance, then we can assume that the simulation conforms to the requirement _naturally_, that is without having to modify code or inputs. If a simulation does not conform to a requirement then conformant should be set to false.'),
            ('requirements', 'activity.numerical_requirement', '0.N', 'Points to the NumericalRequirement that the simulation in question is conforming to.'),
            ('requirements_references', 'shared.cim_reference', '0.N', None),
            ('sources', 'shared.data_source', '0.N', 'Points to the DataSource used to conform to a particular Requirement.   This may be part of an activity::simulation or a software::component.  It can be either a DataObject or a SoftwareComponent or a ComponentProperty.  It could also be by using particular attributes of, say, a SoftwareComponent, but in that case the recommended practise is to reference the component and add appropriate text in the conformance description attribute.'),
            ('sources_references', 'shared.cim_reference', '0.N', None),
            ('type', 'activity.conformance_type', '0.1', 'Describes the method that this simulation conforms to an experimental requirement (in case it is not specified by the change property of the reference to the source of this conformance)'),
        ],
        'decodings' : [
            ('description', 'child::cim:description/text()'),
            ('frequency', 'child::cim:frequency'),
            ('is_conformant', '@conformant'),
            ('requirements', 'child::cim:requirement/cim:requirement/cim:initialCondition', 'activity.initial_condition'),
            ('requirements', 'child::cim:requirement/cim:requirement/cim:boundaryCondition', 'activity.boundary_condition'),
            ('requirements', 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint', 'activity.spatio_temporal_constraint'),
            ('requirements', 'child::cim:requirement/cim:requirement/cim:outputRequirement', 'activity.output_requirement'),
            ('requirements_references', 'child::cim:requirement/cim:reference'),
            ('sources', 'child::cim:source/cim:source/cim:dataObject', 'data.data_object'),
            ('sources', 'child::cim:source/cim:source/cim:dataContent', 'data.data_content'),
            ('sources', 'child::cim:source/cim:source/cim:componentProperty', 'software.component_property'),
            ('sources', 'child::cim:source/cim:source/cim:softwareComponent', 'software.model_component'),
            ('sources', 'child::cim:source/cim:source/cim:softwareComponent', 'software.processor_component'),
            ('sources_references', 'child::cim:source/cim:reference'),
            ('type', '@type'),
        ]
    }
    

def _ensemble():
    """Creates and returns instance of ensemble class."""
    return {
        'type' : 'class',
        'name' : 'ensemble',
        'base' : 'activity.numerical_activity',
        'abstract' : False,
        'doc' : 'An ensemble is made up of two or more simulations which are to be compared against each other to create ensemble statistics. Ensemble members can differ in terms of initial conditions, physical parameterisation and the model used. An ensemble bundles together sets of ensembleMembers, all of which reference the same Simulation(Run) and include one or more changes.',
        'properties' : [
            ('cim_info', 'shared.cim_info', '1.1', None),
        ],
        'decodings' : [
            ('cim_info', 'self::cim:ensemble'),
        ]
    }


def _ensemble_member():
    """Creates and returns instance of ensemble_member class."""
    return {
        'type' : 'class',
        'name' : 'ensemble_member',
        'base' : 'activity.numerical_activity',
        'abstract' : False,
        'doc' : 'A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a "simulation composite".  The "parent" simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.',
        'properties' : [

        ],
        'decodings' : [

        ]
    }

    
def _experiment():
    """Creates and returns instance of experiment class."""
    return {
        'type' : 'class',
        'name' : 'experiment',
        'base' : 'activity.activity',
        'abstract' : True,
        'doc' : 'An experiment might be an activity which is both observational and numerical in focus, for example, a measurement campaign and numerical experiments for an alpine experiment.  It is a place for the scientific description of the reason why an experiment was made.',
        'properties' : [
            ('measurement_campaigns', 'activity.measurement_campaign', '0.N', None),
            ('requires', 'activity.numerical_activity', '0.N', None),
            ('requires_references', 'shared.cim_reference', '0.N', None),
            ('generates', 'str', '0.N', None),
            ('supports', 'str', '1.N', None),
#            ('generates', 'activity.numerical_experiment', '0.N', None),
#            ('supports', 'activity.experiment', '1.N', None),
            ('supports_references', 'shared.cim_reference', '0.N', None),
        ],
        'decodings' : [

        ]
    }


def _experiment_relationship():
    """Creates and returns instance of experiment_relationship class."""
    return {
        'type' : 'class',
        'name' : 'experiment_relationship',
        'base' : 'shared.cim_relationship',
        'abstract' : False,
        'doc' : 'Contains a set of relationship types specific to a experiment document that can be used to describe its genealogy.',
        'properties' : [
            ('target', 'activity.experiment_relationship_target', '1.1', None),
            ('type', 'activity.experiment_relationship_type', '1.1', None),
        ],
        'decodings' : [

        ]
    }


def _experiment_relationship_target():
    """Creates and returns instance of experiment_relationship_target class."""
    return {
        'type' : 'class',
        'name' : 'experiment_relationship_target',
        'base' : None,
        'abstract' : False,
        'doc' : None,
        'properties' : [
            ('reference', 'shared.cim_reference', '0.1', None),
            ('numerical_experiment', 'activity.numerical_experiment', '0.1', None),
        ],
        'decodings' : [

        ]
    }


def _measurement_campaign():
    """Creates and returns instance of measurement_campaign class."""
    return {
        'type' : 'class',
        'name' : 'measurement_campaign',
        'base' : 'activity.activity',
        'abstract' : False,
        'doc' : None,
        'properties' : [
            # todo - clarify type
            ('duration', 'int', '1.1', None),
            # todo - resolve circular dependencies.
            #('experiments', 'activity.experiment', '1.N', None),
        ],
        'decodings' : [

        ]
    }


def _numerical_activity():
    """Creates and returns instance of numerical_activity class."""
    return {
        'type' : 'class',
        'name' : 'numerical_activity',
        'base' : 'activity.activity',
        'abstract' : True,
        'doc' : '',
        'properties' : [
            ('description', 'str', '0.1', 'A free-text description of the experiment.'),
            ('long_name', 'str', '0.1', 'The name of the experiment (that is recognized externally).'),
            ('short_name', 'str', '1.1', 'The name of the experiment (that is used internally).'),
            ('supports', 'activity.experiment', '1.N', None),
            ('supports_references', 'shared.cim_reference', '1.N', None),
        ],
        'decodings' : [
            ('description', 'child::cim:description/text()'),
            ('long_name', 'child::cim:longName/text()'),
            ('short_name', 'child::cim:shortName/text()'),
            ('supports', 'child::cim:supports/cim:experiment'),
            ('supports_references', 'child::cim:supports/cim:reference'),
        ]
    }


def _numerical_experiment():
    """Creates and returns instance of numerical_experiment class."""
    return {
        'type' : 'class',
        'name' : 'numerical_experiment',
        'base' : 'activity.experiment',
        'abstract' : False,
        'doc' : 'A numerical experiment may be generated by an experiment, in which case it is inSupportOf the experiment. But a numerical experiment may also exist as an activity in its own right (as it might be if it were needed for a MIP). Examples: AR4 individual experiments, AR5 individual experiments, RAPID THC experiments etc.',
        'properties' : [
            ('cim_info', 'shared.cim_info', '1.1', None),
            ('description', 'str', '0.1', 'A free-text description of the experiment.'),
            ('experiment_id', 'str', '0.1', 'An experiment ID takes the form <number>.<number>[-<letter>].'),
            ('long_name', 'str', '0.1', 'The name of the experiment (that is recognized externally).'),
            ('requirements', 'activity.numerical_requirement', '0.N', 'The name of the experiment (that is used internally).'),
            ('short_name', 'str', '1.1', 'The name of the experiment (that is used internally).'),
        ],
        'decodings' : [
            ('cim_info', 'self::cim:numericalExperiment'),
            ('description', 'child::cim:description/text()'),
            ('experiment_id', 'child::cim:experimentID/text()'),
            ('long_name', 'child::cim:longName/text()'),
            ('requirements', 'child::cim:numericalRequirement/cim:initialCondition', 'activity.initial_condition'),
            ('requirements', 'child::cim:numericalRequirement/cim:boundaryCondition', 'activity.boundary_condition'),
            ('requirements', 'child::cim:numericalRequirement/cim:spatioTemporalConstraint', 'activity.spatio_temporal_constraint'),
            ('requirements', 'child::cim:numericalRequirement/cim:outputRequirement', 'activity.output_requirement'),
            ('short_name', 'child::cim:shortName/text()'),
        ]
    }


def _numerical_requirement():
    """Creates and returns instance of numerical_requirement class."""
    return {
        'type' : 'class',
        'name' : 'numerical_requirement',
        'base' : None,
        'abstract' : True,
        'doc' : 'A description of the requirements of particular experiments.  Numerical Requirements can be initial conditions, boundary conditions, or physical modificiations.',
        'properties' : [
            ('description', 'str', '0.1', None),
            ('id', 'str', '0.1', None),
            ('name', 'str', '1.1', None),
            ('options', 'activity.requirement_option', '0.N', None),
        ],
        'decodings' : [
            ('description', 'child::cim:description/text()'),
            ('id', 'child::cim:id/text()'),
            ('name', 'child::cim:name/text()'),
            ('options', 'child::cim:requirementOption'),
        ]
    }
    

def _boundary_condition():
    """Creates and returns instance of boundary_condition class."""
    return {
        'type' : 'class',
        'name' : 'boundary_condition',
        'base' : 'activity.numerical_requirement',
        'abstract' : False,
        'doc' : 'A boundary condition is a numerical requirement which looks like a variable imposed on the model evolution (i.e. it might - or might not - evolve with time, but is seen by the model at various times during its evolution) as opposed to an initial condition (at model time zero).',
        'properties' : [

        ],
        'decodings' : [

        ]
    }


def _initial_condition():
    """Creates and returns instance of initial_condition class."""
    return {
        'type' : 'class',
        'name' : 'initial_condition',
        'base' : 'activity.numerical_requirement',
        'abstract' : False,
        'doc' : 'An initial condition is a numerical requirement on a model prognostic variable value at time zero.',
        'properties' : [

        ],
        'decodings' : [

        ]
    }


def _spatio_temporal_constraint():
    """Creates and returns instance of spatio_temporal_constraint class."""
    return {
        'type' : 'class',
        'name' : 'spatio_temporal_constraint',
        'base' : 'activity.numerical_requirement',
        'abstract' : False,
        'doc' : 'Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.',
        'properties' : [
            ('date_range', 'shared.date_range', '0.1', None),
            ('spatial_resolution', 'activity.resolution_type', '0.1', None),
        ],
        'decodings' : [
            ('date_range', 'child::cim:requiredDuration/cim:closedDateRange', 'shared.closed_date_range'),
            ('date_range', 'child::cim:requiredDuration/cim:openDateRange', 'shared.open_date_range'),
            ('spatial_resolution', 'child::cim:spatialResolution/text()'),
        ]
    }


def _output_requirement():
    """Creates and returns instance of output_requirement class."""
    return {
        'type' : 'class',
        'name' : 'output_requirement',
        'base' : 'activity.numerical_requirement',
        'abstract' : False,
        'doc' : 'Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.',
        'properties' : [

        ],
        'decodings' : [

        ]
    }


def _physical_modification():
    """Creates and returns instance of physical_modification class."""
    return {
        'type' : 'class',
        'name' : 'physical_modification',
        'base' : 'activity.conformance',
        'abstract' : False,
        'doc' : 'Physical modification is the implementation of a boundary condition numerical requirement that is achieved within the model code rather than from some external source file. It  might include, for example,  a specific rate constant within a chemical reaction, or coefficient value(s) in a parameterisation.  For example, one might require a numerical experiment where specific chemical reactions were turned off - e.g. no heterogeneous chemistry.',
        'properties' : [

        ],
        'decodings' : [

        ]
    }


def _requirement_option():
    """Creates and returns instance of requirement_option class."""
    return {
        'type' : 'class',
        'name' : 'requirement_option',
        'base' : None,
        'abstract' : False,
        'doc' : 'A NumericalRequirement that is being used as a set of related requirements; For example if a requirement is to use 1 of 3 boundary conditions, then that "parent" requirement would have three "child" RequirmentOptions (each of one with the XOR optionRelationship).',
        'properties' : [
            ('requirement', 'activity.numerical_requirement', '0.1', 'The requirement being specified by this option'),
            ('relationship', 'str', '0.1', 'Describes how this optional (child) requirement is related to its sibling requirements.  For example, a NumericalRequirement could consist of a set of optional requirements each with an "OR" relationship meaning use this boundary condition _or_ that one.'),
        ],
        'decodings' : [
            ('requirement', 'child::cim:requirement/cim:requirement/cim:initialCondition', 'activity.initial_condition'),
            ('requirement', 'child::cim:requirement/cim:requirement/cim:spatioTemporalConstraint', 'activity.output_requirement'),
            ('requirement', 'child::cim:requirement/cim:requirement/cim:outputRequirement', 'activity.spatio_temporal_constraint'),
            ('requirement', 'child::cim:requirement/cim:requirement/cim:boundaryCondition', 'activity.boundary_condition'),
            ('relationship', 'self::cim:requirementOption/@optionRelationship'),
        ]
    }


def _simulation():
    """Creates and returns instance of simulation class."""
    return {
        'type' : 'class',
        'name' : 'simulation',
        'base' : 'activity.numerical_activity',
        'abstract' : True,
        'doc' : 'A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.',
        'properties' : [
            ('authors', 'str', '0.1', 'List of associated authors.'),
            # TODO implement : Daily-360 | RealCalendar | PerpetualPeriod
            ('calendar', 'shared.calendar', '1.1', None),
            ('control_simulation', 'activity.simulation', '0.1', 'Points to a simulation being used as the basis (control) run.  Note that only "derived" simulations can describe something as being control; a simulation should not know if it is being used itself as the control of some other run.'),
            ('control_simulation_reference', 'shared.cim_reference', '0.1', None),
            # TODO implement: Conformance | PhysicalModification
            ('conformances', 'activity.conformance', '0.N', None),
            ('deployments', 'software.deployment', '0.N', None),
            # TODO implement: Coupling
            ('inputs', 'software.coupling', '0.N', 'Implemented as a mapping from a source to target; can be a forcing file, a boundary condition, etc.'),
            ('outputs', 'data.data_object', '0.N', None),
            ('output_references', 'shared.cim_reference', '0.N', None),
            ('restarts', 'data.data_object', '0.N', None),
            ('restart_references', 'shared.cim_reference', '0.N', None),
            ('simulation_id', 'str', '0.1', None),
            ('spinup_date_range', 'shared.closed_date_range', '0.1', 'The date range that a simulation is engaged in spinup.'),
            ('spinup_simulation', 'activity.simulation', '0.1', 'The (external) simulation used during "spinup."  Note that this element can be used in conjuntion with spinupDateRange.  If a simulation has the latter but not the former, then one can assume that the simulation is performing its own spinup.'),
            ('spinup_simulation_reference', 'shared.cim_reference', '0.1', None),
        ],
        'decodings' : [
            ('calendar', 'child::cim:calendar/cim:daily-360', 'shared.daily_360'),
            ('calendar', 'child::cim:calendar/cim:perpetualPeriod', 'shared.perpetual_period'),
            ('calendar', 'child::cim:calendar/cim:realCalendar', 'shared.real_calendar'),
            ('authors', 'child::cim:authorsList/cim:list/text()'),
            ('conformances', 'child::cim:conformance/cim:conformance', 'activity.conformance'),
            ('conformances', 'child::cim:conformance/cim:physicalModification', 'activity.physical_modification'),
            ('control_simulation', 'child::cim:controlSimulation/cim:controlSimulation'),
            ('control_simulation_reference', 'child::cim:controlSimulation/cim:reference'),
            ('deployments', 'child::cim:deployment'),
            ('inputs', 'child::cim:input'),
            ('simulation_id', 'child::cim:simulationID/text()'),
        ]
    }


def _simulation_composite():
    """Creates and returns instance of simulation_composite class."""
    return {
        'type' : 'class',
        'name' : 'simulation_composite',
        'base' : 'activity.simulation',
        'abstract' : False,
        'doc' : 'A SimulationComposite is an aggregation of Simulations. With the aggreation connector between Simulation and SimulationComposite(SC) the SC can be made up of both SimulationRuns and SCs. The SimulationComposite is the new name for the concept of SimulationCollection: A simulation can be made up of "child" simulations aggregated together to form a "simulation composite".  The "parent" simulation can be made up of whole or partial child simulations and the SimulationComposite attributes need to be able to capture this.',
        'properties' : [
            ('cim_info', 'shared.cim_info', '1.1', None),
            ('child', 'activity.simulation', '0.N', None),
            ('date_range', 'shared.date_range', '1.1', None),
            ('rank', 'int', '1.1', 'Position of a simulation in the SimulationComposite timeline. eg:  Is this the first (rank = 1) or second (rank = 2) simulation'),
        ],
        'decodings' : [
            ('cim_info', 'self::cim:simulationRun'),
            ('child', 'child::cim:child', 'activity.simulation_run'),
            ('child', 'child::cim:child', 'activity.simulation_composite'),
            ('date_range', 'child::cim:dateRange/cim:closedDateRange', 'shared.closed_date_range'),
            ('date_range', 'child::cim:dateRange/cim:openDateRange', 'shared.open_date_range'),
            ('rank', 'child::cim:rank/text()'),
        ]
    }


def _simulation_relationship():
    """Creates and returns instance of simulation_relationship class."""
    return {
        'type' : 'class',
        'name' : 'simulation_relationship',
        'base' : 'shared.cim_relationship',
        'abstract' : False,
        'doc' : 'Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.',
        'properties' : [
            ('target', 'activity.simulation_relationship_target', '1.1', None),
            ('type', 'activity.simulation_relationship_type', '1.1', None),
        ],
        'decodings' : [

        ]
    }


def _simulation_relationship_target():
    """Creates and returns instance of simulation_relationship_target class."""
    return {
        'type' : 'class',
        'name' : 'simulation_relationship_target',
        'base' : None,
        'abstract' : False,
        'doc' : None,
        'properties' : [
            ('reference', 'shared.cim_reference', '0.1', None),
            ('target', 'activity.simulation_type', '0.1', None),
        ],
        'decodings' : [

        ]
    }


def _simulation_run():
    """Creates and returns instance of simulation_run class."""
    return {
        'type' : 'class',
        'name' : 'simulation_run',
        'base' : 'activity.simulation',
        'abstract' : False,
        'doc' : 'A SimulationRun is, as the name implies, one single model run. A SimulationRun is a Simulation. There is a one to one association between SimulationRun and (a top-level) SoftwarePackage::ModelComponent.',
        'properties' : [
            ('cim_info', 'shared.cim_info', '1.1', None),
            ('date_range', 'shared.date_range', '1.1', None),            
            ('model', 'software.model_component', '0.1', None),
            ('model_reference', 'shared.cim_reference', '0.1', None),
        ],
        'decodings' : [
            ('cim_info', 'self::cim:simulationRun'),
            ('date_range', 'child::cim:dateRange/cim:closedDateRange', 'shared.closed_date_range'),
            ('date_range', 'child::cim:dateRange/cim:openDateRange', 'shared.open_date_range'),
            ('model', 'child::cim:model/cim:modelComponent'),
            ('model_reference', 'child::cim:model/cim:reference'),
        ]
    }


# Set of package classes.
classes = [
    _activity(),
    _boundary_condition(),
    _conformance(),
    _ensemble(),
    _ensemble_member(),
    _experiment(),
    _experiment_relationship(),
    _experiment_relationship_target(),
    _initial_condition(),
    _measurement_campaign(),
    _numerical_activity(),
    _numerical_experiment(),
    _numerical_requirement(),
    _output_requirement(),
    _physical_modification(),
    _requirement_option(),
    _simulation(),
    _simulation_composite(),
    _simulation_relationship(),
    _simulation_relationship_target(),
    _simulation_run(),
    _spatio_temporal_constraint(),
]
