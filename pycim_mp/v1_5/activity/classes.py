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
            ('responsible_parties', 'shared.responsible_party', '0.N', 'The point of contact(s) for this activity.This includes, among others, the principle investigator.'),
            ('funding_sources', 'str', '0.N', 'The entities that funded this activity.'),
            ('rationales', 'str', '0.N', 'For what purpose is this activity being performed?'),
            ('projects', 'activity.project_type', '0.N', 'The project(s) that this activity is associated with (ie: CMIP5, AMIP, etc).'),
        ],
        'decodings' : [
            ('rationales', 'child::cim:rationale/text()'),
        ]
    }
    

def _experiment():
    """Creates and returns instance of experiment class."""
    return {
        'type' : 'class',
        'name' : 'experiment',
        'base' : 'activity.activity',
        'abstract' : True,
        'doc' : 'An abstract class used as the parent of MeasurementCampaigns, Projects, Experiments, and NumericalActivities.',
        'properties' : [
            ('measurement_campaigns', 'activity.measurement_campaign', '0.N', None),
            ('requires', 'activity.measurement_campaign', '0.N', None),
            ('generates', 'activity.measurement_campaign', '0.N', None),
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



# Set of package classes.
classes = [
    _activity(),
    _boundary_condition(),
    _experiment(),
    _experiment_relationship(),
    _experiment_relationship_target(),
    _initial_condition(),
    _measurement_campaign(),
    _numerical_experiment(),
    _numerical_requirement(),
    _output_requirement(),
    _requirement_option(),
    _simulation_relationship(),
    _simulation_relationship_target(),
    _spatio_temporal_constraint(),
]
