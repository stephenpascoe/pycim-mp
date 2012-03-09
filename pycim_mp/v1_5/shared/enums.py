"""
CIM v1.5 shared package enums.
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


def _cim_document_relationship_type():
    """Creates and returns instance of document_relationship_type enum."""
    return {
        'type' : 'enum',
        'name' : 'cim_document_relationship_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('similarTo', None),
            ('other', None),
            ('laterVersionOf', None),
            ('previousVersionOf', None),
            ('fixedVersionOf', None),
        ],
    }


def _cim_document_type():
    """Creates and returns instance of cim_document_type enum."""
    return {
        'type' : 'enum',
        'name' : 'cim_document_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('simulationRun', None),
            ('assimilation', None),
            ('simulationComposite', None),
            ('numericalExperiment', None),
            ('dataProcessing', None),
            ('ensemble', None),
            ('dataObject', None),
            ('gridSpec', None),
            ('cimQuality', None),
            ('platform', None),
            ('processorComponent', None),
            ('modelComponent', None),
        ],
    }


def _cim_relationship_direction_type():
    """Creates and returns instance of relationship_direction_type enum."""
    return {
        'type' : 'enum',
        'name' : 'cim_relationship_direction_type',
        'is_open' : False,
        'doc' : None,
        'members' : [
            ('toTarget', None),
            ('fromTarget', None),
        ],
    }


def _compiler_type():
    """Creates and returns instance of compiler_type enum."""
    return {
        'type' : 'enum',
        'name' : 'compiler_type',
        'is_open' : True,
        'doc' : 'A list of known compilers.',
        'members' : [ ],
    }


def _data_purpose():
    """Creates and returns instance of data_purpose enum."""
    return {
        'type' : 'enum',
        'name' : 'data_purpose',
        'is_open' : False,
        'doc' : 'Purpose of the data - i.e. ancillaryFile, boundaryCondition or initialCondition.',
        'members' : [
            ('ancillaryFile', None),
            ('boundaryCondition', None),
            ('initialCondition', None),
        ],
    }


def _document_status_type():
    """Creates and returns instance of document_status_type enum."""
    return {
        'type' : 'enum',
        'name' : 'document_status_type',
        'is_open' : False,
        'doc' : 'Status of cim document.',
        'members' : [
            ('complete', None),
            ('incomplete', None),
            ('in-progress', None),
        ],
    }


def _interconnect_type():
    """Creates and returns instance of interconnect_type enum."""
    return {
        'type' : 'enum',
        'name' : 'interconnect_type',
        'is_open' : True,
        'doc' : "A list of connectors between machines.",
        'members' : [ ],
    }


def _machine_type():
    """Creates and returns instance of machine_type enum."""
    return {
        'type' : 'enum',
        'name' : 'machine_type',
        'is_open' : False,
        'doc' : 'A list of known machines.',
        'members' : [
            ('Parallel', None),
            ('Vector', None),
            ('Beowulf', None),
        ],
    }


def _machine_vendor_type():
    """Creates and returns instance of machine_vendor_type enum."""
    return {
        'type' : 'enum',
        'name' : 'machine_vendor_type',
        'is_open' : True,
        'doc' : 'A list of organisations that create machines.',
        'members' : [ ],
    }


def _operating_system_type():
    """Creates and returns instance of operating_system_type enum."""
    return {
        'type' : 'enum',
        'name' : 'operating_system_type',
        'is_open' : True,
        'doc' : 'A list of common operating systems.',
        'members' : [ ],
    }


def _standard_name():
    """Creates and returns instance of standard_name enum."""
    return {
        'type' : 'enum',
        'name' : 'standard_name',
        'is_open' : True,
        'doc' : 'Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be "CF" and the name might be "atmospheric_pressure".',
        'members' : [ ],
    }


def _processor_type():
    """Creates and returns instance of processor_type enum."""
    return {
        'type' : 'enum',
        'name' : 'processor_type',
        'is_open' : True,
        'doc' : "A list of known cpu's.",
        'members' : [ ],
    }


def _unit_type():
    """Creates and returns instance of unit_type enum."""
    return {
        'type' : 'enum',
        'name' : 'unit_type',
        'is_open' : True,
        'doc' : "A list of scientific units.",
        'members' : [ ],
    }


# Set of package enums.
enums = [
    _cim_document_type(),
    _cim_document_relationship_type(),
    _cim_relationship_direction_type(),
    _compiler_type(),
    _data_purpose(),
    _document_status_type(),
    _interconnect_type(),
    _machine_type(),
    _machine_vendor_type(),
    _operating_system_type(),
    _processor_type(),
    _standard_name(),
    _unit_type(),
]


