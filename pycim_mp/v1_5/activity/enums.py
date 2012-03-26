"""
CIM v1.5 activity package enums.
"""
# Module exports.
__all__ = ["enums"]


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"


def _conformance_type():
    """Creates and returns instance of conformance_type enum."""
    return {
        'type' : 'enum',
        'name' : 'conformance_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('not conformant', 'Describes a simulation that is purpefully non-conformant to an experimental requirement.'),
            ('standard config', 'Describes a simulation that is "naturally" conformant to an experimental requirement.'),
            ('via inputs', 'Describes a simulation that conforms to an experimental requirement by using particular inputs.'),
            ('via model mods', 'Describes a simulation that conforms to an experimental requirement by changing the configuration of the software model implementing that simulation.'),
            ('combination', 'Describes a simulation that conforms to an experimental requirement by using more than one method.'),
        ],
    }


def _ensemble_type():
    """Creates and returns instance of ensemble_type enum."""
    return {
        'type' : 'enum',
        'name' : 'ensemble_type',
        'is_open' : True,
        'doc' : None,
        'members' : [

        ],
    }


def _experiment_relationship_type():
    """Creates and returns instance of experiment_relationship_type enum."""
    return {
        'name' : 'experiment_relationship_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('previousRealisation', None),
            ('continuationOf', None),
            ('controlExperiment', None),
            ('higherResolutionVersionOf', None),
            ('lowerResolutionVersionOf', None),
            ('increaseEnsembleOf', None),
            ('modifiedInputMethodOf', None),
            ('shorterVersionOf', None),
            ('extensionOf', None),
        ],
    }


def _frequency_type():
    """Creates and returns instance of frequency_type enum."""
    return {
        'type' : 'enum',
        'name' : 'frequency_type',
        'is_open' : True,
        'doc' : None,
        'members' : [

        ],
    }


def _project_type():
    """Creates and returns instance of project_type enum."""
    return {
        'type' : 'enum',
        'name' : 'project_type',
        'is_open' : True,
        'doc' : None,
        'members' : [],
    }


def _resolution_type():
    """Creates and returns instance of resolution_type enum."""
    return {
        'type' : 'enum',
        'name' : 'resolution_type',
        'is_open' : True,
        'doc' : None,
        'members' : [],
    }    


def _simulation_relationship_type():
    """Creates and returns instance of simulation_relationship_type enum."""
    return {
        'name' : 'simulation_relationship_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('extensionOf', None),
            ('responseTo', None),
            ('continuationOf', None),
            ('previousSimulation', None),
            ('higherResolutionVersionOf', None),
            ('lowerResolutionVersionOf', None),
            ('fixedVersionOf', None),
            ('followingSimulation', None),
        ],
    }


def _simulation_type():
    """Creates and returns instance of simulation_type enum."""
    return {
        'type' : 'enum',
        'name' : 'simulation_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('simulationRun', None),
            ('assimilation', None),
            ('simulationComposite', None),
        ],
    }



# Set of package enums.
enums = [
    _conformance_type(),
    _ensemble_type(),
    _experiment_relationship_type(),
    _frequency_type(),
    _project_type(),
    _resolution_type(),
    _simulation_relationship_type(),
    _simulation_type(),
]

