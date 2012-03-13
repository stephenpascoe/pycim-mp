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


def _project_type():
    """Creates and returns instance of project_type enum."""
    return {
        'type' : 'enum',
        'name' : 'project_type',
        'is_open' : True,
        'doc' : None,
        'members' : [],
    }


def _project_type():
    """Creates and returns instance of resolution_type enum."""
    return {
        'type' : 'enum',
        'name' : 'resolution_type',
        'is_open' : True,
        'doc' : None,
        'members' : [],
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

#    return EnumInfo('simulation_type', False, None,
#        [
#            EnumMemberInfo('simulationRun', None),
#            EnumMemberInfo('assimilation', None),
#            EnumMemberInfo('simulationComposite', None),
#        ]
#    )


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

#    return EnumInfo('simulation_relationship_type', False, None,
#        [
#            EnumMemberInfo('extensionOf', None),
#            EnumMemberInfo('responseTo', None),
#            EnumMemberInfo('continuationOf', None),
#            EnumMemberInfo('previousSimulation', None),
#            EnumMemberInfo('higherResolutionVersionOf', None),
#            EnumMemberInfo('lowerResolutionVersionOf', None),
#            EnumMemberInfo('fixedVersionOf', None),
#            EnumMemberInfo('followingSimulation', None),
#        ]
#    )


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
#
#    return EnumInfo('experiment_relationship_type', False, None,
#        [
#            EnumMemberInfo('previousRealisation', None),
#            EnumMemberInfo('continuationOf', None),
#            EnumMemberInfo('controlExperiment', None),
#            EnumMemberInfo('higherResolutionVersionOf', None),
#            EnumMemberInfo('lowerResolutionVersionOf', None),
#            EnumMemberInfo('increaseEnsembleOf', None),
#            EnumMemberInfo('modifiedInputMethodOf', None),
#            EnumMemberInfo('shorterVersionOf', None),
#            EnumMemberInfo('extensionOf', None),
#        ]
#    )



# Set of package enums.
enums = [
    _project_type(),
    _simulation_type(),
    _simulation_relationship_type(),
    _experiment_relationship_type(),
]

