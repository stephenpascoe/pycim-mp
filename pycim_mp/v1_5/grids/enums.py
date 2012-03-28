"""
CIM v1.5 grids package enums.
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


def _arc_type_enum():
    """Creates and returns instance of arc_type_enum enum."""
    return {
        'name' : 'arc_type_enum',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('geodesic', None),
            ('great_circle', None),
            ('small_circle', None),
            ('complex', None),
        ],
    }


def _discretization_enum():
    """Creates and returns instance of discretization_enum enum."""
    return {
        'name' : 'discretization_enum',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('logically_rectangular', None),
            ('structured_triangular', None),
            ('unstructured_triangular', None),
            ('pixel-based_catchment', None),
            ('unstructured_polygonal', None),
            ('spherical_harmonics', None),
            ('other', None),
        ],
    }


def _feature_type_enum():
    """Creates and returns instance of feature_type_enum enum."""
    return {
        'name' : 'feature_type_enum',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('point', None),
            ('edge', None),
        ],
    }


def _geometry_type_enum():
    """Creates and returns instance of geometry_type_enum enum."""
    return {
        'name' : 'geometry_type_enum',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('ellipsoid', None),
            ('plane', None),
            ('sphere', None),
        ],
    }


def _grid_node_position_enum():
    """Creates and returns instance of grid_node_position_enum enum."""
    return {
        'name' : 'grid_node_position_enum',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('centre', None),
            ('plane', None),
            ('sphere', None),
        ],
    }


def _grid_type_enum():
    """Creates and returns instance of grid_type_enum enum."""
    return {
        'name' : 'grid_type_enum',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('cubed_sphere', None),
            ('displaced_pole', None),
            ('icosahedral_geodesic', None),
            ('reduced_gaussian', None),
            ('regular_lat_lon', None),
            ('spectral_gaussian', None),
            ('tripolar', None),
            ('yin_yang', None),
            ('composite', None),
            ('other', None),
        ],
    }


def _horizontal_cs_enum():
    """Creates and returns instance of horizontal_cs_enum enum."""
    return {
        'name' : 'horizontal_cs_enum',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('cartesian', None),
            ('ellipsoidal', None),
            ('polar', None),
            ('spherical', None),
        ],
    }


def _refinement_type_enum():
    """Creates and returns instance of refinement_type_enum enum."""
    return {
        'name' : 'refinement_type_enum',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('none', 'Tile boundaries have no refinement when the grid lines meeting at the tile boundary are continuous.'),
            ('integer', 'The refinement is integer when grid lines from the coarser grid are continuous on the finer grid, but not vice versa.'),
            ('rational','The refinement is rational when the adjacent or overlapping grid tiles have grid line counts that are coprime (i.e. no common factor other than 1).'),
        ],
    }


def _vertical_cs_enum():
    """Creates and returns instance of vertical_cs_enum enum."""
    return {
        'name' : 'vertical_cs_enum',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('mass-based', None),
            ('space-based', None),
        ],
    }

    
# Set of package enums.
enums = [
    _discretization_enum(),
    _feature_type_enum(),
    _geometry_type_enum(),
    _grid_type_enum(),
    _horizontal_cs_enum(),
    _refinement_type_enum(),
    _vertical_cs_enum(),
]

