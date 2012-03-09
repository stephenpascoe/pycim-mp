"""
CIM v1.5 data package enums.
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


def _data_hierarchy_type():
    """Creates and returns instance of data_status_type enum."""
    return {
        'name' : 'data_hierarchy_type',
        'is_open' : True,
        'doc' : 'What level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject.',
        'members' : [ ],
    }

#    return EnumInfo('data_hierarchy_type', True, 'What level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject.')


def _data_status_type():
    """Creates and returns instance of data_status_type enum."""
    return {
        'name' : 'data_status_type',
        'is_open' : False,
        'doc' : 'Status of the data.',
        'members' : [
            ('complete', 'This DataObject is complete.'),
            ('metadataOnly', 'This DataObject is incomplete - it is described in metadata but the actual data has not yet been linked to it.'),
            ('continuouslySupplemented', 'This DataObject\'s actual data is continuously updated.'),
        ],
    }

#    return EnumInfo('data_status_type', False, 'Status of the data.',
#        [
#            EnumMemberInfo('complete', 'This DataObject is complete.'),
#            EnumMemberInfo('metadataOnly', 'This DataObject is incomplete - it is described in metadata but the actual data has not yet been linked to it.'),
#            EnumMemberInfo('continuouslySupplemented', 'This DataObject\'s actual data is continuously updated.'),
#        ]
#    )



# Set of package enums.
enums = [
    _data_hierarchy_type(),
    _data_status_type(),
]

