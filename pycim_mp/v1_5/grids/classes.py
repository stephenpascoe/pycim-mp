"""
CIM v1.5 grids package classes.
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


def _grid_mosaic():
    """Creates and returns instance of grid_mosaic class."""
    return {
        'type' : 'class',
        'name' : 'grid_mosaic',
        'base' : None,
        'abstract' : False,
        'doc' : 'The GridMosaic class is used to define the geometry properties of an earth system model grid or an exchange grid. Such a grid definition may then be referenced by any number of earth system models. A GridMosaic object consists either of 1 or more child GridMosaics, or one or more child GridTiles, but not both. In the latter case the isLeaf property should be set to true, indicating that the mosaic is a leaf mosaic.',
        'properties' : [
            ('description', 'str', '0.1', 'A free-text description of a grid mosaic.'),
            ('long_name', 'str', '0.1', 'Specifies the long name associated with a grid mosaic. The long name will typically be a human-readable string, with acronyms expanded, used for labelling purposes.'),
            ('short_name', 'str', '1.1', 'Specifies the short name associated with a grid mosaic. The short name will typically be a convenient abbreviation used to refer to a grid mosaic, e.g. \'UM ATM N96\'.'),
        ],
        'decodings' : [
            ('description', 'child::cim:description/text()'),
            ('long_name', 'child::cim:longName/text()'),
            ('short_name', 'child::cim:shortName/text()'),
        ]
    }


def _grid_spec():
    """Creates and returns instance of data_object class."""
    return {
        'type' : 'class',
        'name' : 'grid_spec',
        'base' : None,
        'abstract' : False,
        'doc' : 'This is a container class for GridSpec objects. A GridSpec object can contain one or more esmModelGrid objects, and one or more esmExchangeGrid objects. These objects may be serialised to one or possibly several files according to taste. Since GridSpec is sub-typed from GML\'s AbstractGeometryType it can, and should, be identified using a gml:id attribute.',
        'properties' : [
            ('cim_info', 'shared.cim_info', '1.1', None),
            ('esm_model_grids', 'grids.grid_mosaic', '0.N', None),
            ('esm_exchange_grids', 'grids.grid_mosaic', '0.N', None),
        ],
        'decodings' : [
            ('cim_info', 'self::cim:dataObject'),
            ('esm_model_grids', 'child::cim:esmModelGrid'),
            ('esm_exchange_grids', 'child::cim:esmExchangeGrid'),
        ]
    }

    

# Set of package classes.
classes = [
    _grid_mosaic(),
    _grid_spec(),
]
