"""
CIM v1.5 software package enums.
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


def _component_property_intent_type():
    """Creates and returns instance of component_property_intent_type enum."""
    return {
        'name' : 'component_property_intent_type',
        'is_open' : False,
        'doc' : 'The direction that the associated component property is intended to be coupled: in, out, or inout..',
        'members' : [
            ('in', None),
            ('out', None),
            ('inout', None),
        ],
    }


def _connection_type():
    """Creates and returns instance of connection_type enum."""
    return {
        'name' : 'connection_type',
        'is_open' : True,
        'doc' : 'The ConnectionType enumeration describes the mechanism of transport for a connection.',
        'members' : [ ],
    }


def _coupling_framework_type():
    """Creates and returns instance of coupling_framework_type enum."""
    return {
        'name' : 'coupling_framework_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('BFG', None),
            ('ESMF', None),
            ('OASIS', None),
        ],
    }


def _model_component_type():
    """Creates and returns instance of model_component_type enum."""
    return {
        'name' : 'model_component_type',
        'is_open' : True,
        'doc' : 'An enumeration of types of ModelComponent. This includes things like atmosphere & ocean models, radiation schemes, etc. CIM best-practice is to describe every component for which there is a named ComponentType as a separate component, even if it is not a separate unit of software (ie: even if it is embedded), instead of as a (set of) ModelParameters. This codelist is synonomous with "realm" for the purposes of CMIP5.',
        'members' : [ ],
    }


def _spatial_regridding_dimension_type():
    """Creates and returns instance of spatial_regridding_dimension_type enum."""
    return {
        'name' : 'spatial_regridding_dimension_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('1D', None),
            ('2D', None),
            ('3D', None),
        ],
    }


def _spatial_regridding_standard_method_type():
    """Creates and returns instance of spatial_regridding_standard_method_type enum."""
    return {
        'name' : 'spatial_regridding_standard_method_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('linear', None),
            ('near-neighbour', None),
            ('cubic', None),
            ('conservative-first-order', None),
            ('conservative-second-order', None),
            ('conservative', None),
            ('non-conservative', None),
        ],
    }


def _time_mapping_type():
    """Creates and returns instance of time_mapping_type enum."""
    return {
        'name' : 'time_mapping_type',
        'is_open' : True,
        'doc' : 'Enumerates the different ways that time can be mapped when transforming from one field to another.',
        'members' : [ ],
    }
    

def _timing_units():
    """Creates and returns instance of timing_units enum."""
    return {
        'name' : 'timing_units',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('seconds', None),
            ('minutes', None),
            ('hours', None),
            ('days', None),
            ('months', None),
            ('years', None),
            ('decades', None),
            ('centuries', None),
        ],
    }



# Set of package enums.
enums = [
    _component_property_intent_type(),
    _connection_type(),
    _coupling_framework_type(),
    _model_component_type(),
    _spatial_regridding_dimension_type(),
    _spatial_regridding_standard_method_type(),
    _time_mapping_type(),
    _timing_units(),
]

