"""
CIM v1.5 data package classes.
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



def _data_content():
    """Creates and returns instance of data_content class."""
    return {
        'type' : 'class',
        'name' : 'data_content',
        'base' : 'shared.data_source',
        'abstract' : False,
        'doc' : 'The contents of the data object; like ISO: MD_ContentInformation.',
        'properties' : [
            ('aggregation', 'str', '0.1', 'Describes how the content has been aggregated together: sum, min, mean, max, ...'),
            ('frequency', 'str', '0.1', 'Describes the frequency of the data content: daily, hourly, ...'),
            ('topic', 'data.data_topic', '1.1', None),
        ],
        'decodings' : [
            ('aggregation', 'child::cim:aggregation/text()'),
            ('frequency', 'child::cim:frequency/@value'),
            ('topic', 'child::cim:topic'),
        ]
    }


def _data_distribution():
    """Creates and returns instance of data_distribution class."""
    return {
        'type' : 'class',
        'name' : 'data_distribution',
        'base' : None,
        'abstract' : False,
        'doc' : 'Describes how a DataObject is distributed.',
        'properties' : [
            ('access', 'str', '0.1', None),
            ('fee', 'str', '0.1', None),
            ('format', 'str', '0.1', None),
            ('responsible_party', 'shared.responsible_party', '0.1', None),
        ],
        'decodings' : [
            ('access', '@distributionAccess'),
            ('format', 'child::cim:distributionFormat/@value'),
            ('responsible_party', 'child::cim:responsibleParty'),
        ]
    }


def _data_extent():
    """Creates and returns instance of data_extent class."""

    return {
        'type' : 'class',
        'name' : 'data_extent',
        'base' : None,
        'abstract' : False,
        'doc' : 'A data object extent represents the geographical and temporal coverage associated with a data object.',
        'properties' : [
            ('temporal', 'data.data_extent_temporal', '1.1', None),
            ('geographical', 'data.data_extent_geographical', '1.1', None),
        ],
        'decodings' : [
            ('geographical', 'child::gmd:geographicElement'),
            ('temporal', 'child::gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/gml:TimePeriod'),
        ]
    }


def _data_extent_geographical():
    """Creates and returns instance of data_extent_geographical class."""
    return {
        'type' : 'class',
        'name' : 'data_extent_geographical',
        'base' : None,
        'abstract' : False,
        'doc' : 'A data object geographical extent represents the geographical coverage associated with a data object.',
        'properties' : [
            ('east', 'float', '0.1', None),
            ('south', 'float', '0.1', None),
            ('west', 'float', '0.1', None),
            ('north', 'float', '0.1', None),
        ],
        'decodings' : [
            ('east', 'child::gmd:EX_GeographicBoundingBox/gmd:eastBoundLongitude/gco:Decimal/text()'),
            ('south', 'child::gmd:EX_GeographicBoundingBox/gmd:southBoundLatitude/gco:Decimal/text()'),
            ('west', 'child::gmd:EX_GeographicBoundingBox/gmd:westBoundLongitude/gco:Decimal/text()'),
            ('north', 'child::gmd:EX_GeographicBoundingBox/gmd:northBoundLatitude/gco:Decimal/text()'),
        ]
    }


def _data_extent_temporal():
    """Creates and returns instance of data_extent_temporal class."""
    return {
        'type' : 'class',
        'name' : 'data_extent_temporal',
        'base' : None,
        'abstract' : False,
        'doc' : 'A data object temporal extent represents the temporal coverage associated with a data object.',
        'properties' : [
            ('begin', 'date', '0.1', None),
            ('end', 'date', '0.1', None),
            ('time_interval', 'data.data_extent_time_interval', '0.1', None),
        ],
        'decodings' : [
            ('begin', 'child::gml:beginPosition/text()'),
            ('end', 'child::gml:endPosition/text()'),
            ('time_interval', 'child::gml:timeInterval'),
        ]
    }


def _data_extent_time_interval():
    """Creates and returns instance of data_extent_time_interval class."""
    return {
        'type' : 'class',
        'name' : 'data_extent_time_interval',
        'base' : None,
        'abstract' : False,
        'doc' : 'A data object temporal extent represents the temporal coverage associated with a data object.',
        'properties' : [
            ('unit', 'str', '0.1', None),
            ('factor', 'int', '0.1', None),
            ('radix', 'int', '0.1', None),
        ],
        'decodings' : [
            ('factor', '@factor'),
            ('radix', '@radix'),
            ('unit', '@unit'),
        ]
    }


def _data_hierarchy_level():
    """Creates and returns instance of data_hierarchy_level class."""
    return {
        'type' : 'class',
        'name' : 'data_hierarchy_level',
        'base' : None,
        'abstract' : False,
        'doc' : 'The type of data object that is grouped together into a particular hierarchy.  Currently, this is made up of terms describing how the Met Office splits up archived data and how THREDDS categorises variables.',
        'properties' : [
            ('name', 'data.data_hierarchy_type', '0.1', 'What level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject.'),
            # TODO - sink to to shared.property_value
            ('is_open', 'bool', '0.1', None),
            # TODO - resolve property type to shared.property_value
            ('value', 'str', '0.1', 'What is the name of the specific HierarchyLevel this DataObject is being organised at (ie: if the HierarchyLevel is "run" then the name might be the runid).'),
        ],
        'decodings' : [
            ('is_open', 'child::cim:hierarchyLevelName/@open'),
            ('name', 'child::cim:hierarchyLevelName/@value'),
            ('value', 'child::cim:hierarchyLevelValue/text()'),
        ]
    }


def _data_object():
    """Creates and returns instance of data_object class."""
    return {
        'type' : 'class',
        'name' : 'data_object',
        'base' : 'shared.data_source',
        'abstract' : False,
        'doc' : 'A DataObject describes a unit of data.  DataObjects can be grouped hierarchically.  The attributes hierarchyLevelName and hierarchyLevelValue describe how objects are grouped.',
        'properties' : [
            ('cim_info', 'shared.cim_info', '1.1', None),
            ('acronym', 'str', '0.1', None),
            ('child_object', 'data.data_object', '0.N', None),
            ('citations', 'shared.citation', '0.N', None),
            ('content', 'data.data_content', '0.N', 'The content of a DataObject corresponds to a variable (in THREDDS, ...etc.)'),
            ('data_property', 'data.data_property', '0.N', None),
            ('data_status', 'data.data_status_type', '0.1', None),
            ('description', 'str', '0.1', None),
            ('distribution', 'data.data_distribution', '0.1', None),
            ('extent', 'data.data_extent', '0.1', None),
            ('hierarchy_level', 'data.data_hierarchy_level', '0.1', None),
            ('keyword', 'str', '0.1', None),
            # TODO - define type
            ('geometry_model', 'str', '0.1', None),
            ('parent_object', 'data.data_object', '0.1', None),
            ('parent_object_reference', 'shared.cim_reference', '0.1', None),
            ('restriction', 'data.data_restriction', '0.N', None),
            # TODO - define type
            ('source_simulation', 'str', '0.1', None),
            ('storage', 'data.data_storage', '0.N', None),
        ],
        'decodings' : [
            ('acronym', 'child::cim:acronym/text()'),
            ('cim_info', 'self::cim:dataObject'),
            ('citations', '//cim:citation[not(cim:citation)]'),
            ('content', 'child::cim:content'),
            ('data_property', 'child::cim:dataProperty/cim:dataProperty'),
            ('data_status', 'self::cim:dataObject/@dataStatus'),
            ('description', 'child::cim:description/text()'),
            ('distribution', 'child::cim:distribution'),
            ('extent', 'child::cim:extent'),
            ('hierarchy_level', 'self::cim:dataObject'),
            ('keyword', 'child::cim:keyword/text()'),
            ('purpose', 'self::cim:dataObject/@purpose'),
        ]
    }


def _data_property():
    """Creates and returns instance of data_property class."""
    return {
        'type' : 'class',
        'name' : 'data_property',
        'base' : 'shared.property',
        'abstract' : False,
        'doc' : 'A property of a DataObject. Currently this is intended to be used to record CF specific information (like packing, scaling, etc.) for OASIS4.',
        'properties' : [
            ('description', 'str', '0.1', None),
        ],
        'decodings' : [
            ('description', 'child::cim:description/text()'),
        ]
    }


def _data_restriction():
    """Creates and returns instance of data_restriction class."""
    return {
        'type' : 'class',
        'name' : 'data_restriction',
        'base' : None,
        'abstract' : False,
        'doc' : 'An access or use restriction on some element of the DataObject\'s actual data.',
        'properties' : [
            ('scope', 'str', '0.1', 'The thing (data or metadata, access or use) that this restriction is applied to.'),
            ('restriction', 'str', '0.1', 'The thing (data or metadata, access or use) that this restriction is applied to.'),
            ('license', 'shared.license', '0.1', 'The thing (data or metadata, access or use) that this restriction is applied to.'),
        ],
        'decodings' : [

        ]
    }


def _data_storage():
    """Creates and returns instance of data_storage class."""
    return {
        'type' : 'class',
        'name' : 'data_storage',
        'base' : None,
        'abstract' : True,
        'doc' : 'Describes the method that the DataObject is stored. An abstract class with specific child classes for each supported method.',
        'properties' : [
            ('size', 'int', '0.1', None),
            ('format', 'str', '0.1', None),
            ('modification_date', 'datetime', '0.1', None),
            ('location', 'str', '0.1', None),
        ],
        'decodings' : [

        ]
    }


def _data_storage_db():
    """Creates and returns instance of data_storage_db class."""
    return {
        'type' : 'class',
        'name' : 'data_storage_db',
        'base' : 'data.data_storage',
        'abstract' : False,
        'doc' : 'Contains attributes to describe a DataObject stored as a database file.',
        'properties' : [
            ('access_string', 'str', '0.1', None),
            ('name', 'str', '0.1', None),
            ('owner', 'str', '0.1', None),
            ('table', 'str', '0.1', None),
        ],
        'decodings' : [

        ]
    }


def _data_storage_file():
    """Creates and returns instance of data_storage_file class."""
    return {
        'type' : 'class',
        'name' : 'data_storage_file',
        'base' : 'data.data_storage',
        'abstract' : False,
        'doc' : 'Contains attributes to describe a DataObject stored as a single file.',
        'properties' : [
            ('file_system', 'str', '0.1', None),
            ('path', 'str', '0.1', None),
            ('file_name', 'str', '0.1', None),
        ],
        'decodings' : [

        ]
    }


def _data_storage_ip():
    """Creates and returns instance of data_storage_ip class."""
    return {
        'type' : 'class',
        'name' : 'data_storage_ip',
        'base' : 'data.data_storage',
        'abstract' : False,
        'doc' : 'Contains attributes to describe a DataObject stored as a database file.',
        'properties' : [
            ('protocol', 'str', '0.1', None),
            ('host', 'str', '0.1', None),
            ('path', 'str', '0.1', None),
            ('file_name', 'str', '0.1', None),
        ],
        'decodings' : [

        ]
    }


def _data_topic():
    """Creates and returns instance of data_topic class."""
    return {
        'type' : 'class',
        'name' : 'data_topic',
        'base' : None,
        'abstract' : False,
        'doc' : 'Describes the content  of a data object; the variable\'s name, units, etc.',
        'properties' : [
            ('name', 'str', '0.1', None),
            ('description', 'str', '0.1', None),
            ('unit', 'str', '0.1', None),
        ],
        'decodings' : [
            ('description', 'child::cim:description/text()'),
            ('name', 'child::cim:name/text()'),
            ('unit', 'child::cim:unit/@value'),
        ]
    }



# Set of package classes.
classes = [
    _data_content(),
    _data_distribution(),
    _data_extent(),
    _data_extent_geographical(),
    _data_extent_temporal(),
    _data_extent_time_interval(),
    _data_hierarchy_level(),
    _data_object(),
    _data_property(),
    _data_restriction(),
    _data_storage(),
    _data_storage_db(),
    _data_storage_file(),
    _data_storage_ip(),
    _data_topic()
]

