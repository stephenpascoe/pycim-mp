"""A set of cim 1.5 decodings.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.690970.
"""

# Module imports.
from cim.core.decoding.cim_decoder_xml_utils import *
from cim.v1_5.decoding.decoder_for_shared_package import decode_cim_info
from cim.v1_5.decoding.decoder_for_shared_package import decode_cim_reference
from cim.v1_5.decoding.decoder_for_shared_package import decode_cim_reference
from cim.v1_5.decoding.decoder_for_shared_package import decode_responsible_party
from cim.v1_5.types.activity.activity import Activity
from cim.v1_5.types.activity.experiment import Experiment
from cim.v1_5.types.activity.experiment_relationship import ExperimentRelationship
from cim.v1_5.types.activity.experiment_relationship_target import ExperimentRelationshipTarget
from cim.v1_5.types.activity.measurement_campaign import MeasurementCampaign
from cim.v1_5.types.activity.numerical_experiment import NumericalExperiment
from cim.v1_5.types.activity.simulation_relationship import SimulationRelationship
from cim.v1_5.types.activity.simulation_relationship_target import SimulationRelationshipTarget


# Module exports.
__all__ = [
    'decode_activity', 
    'decode_experiment', 
    'decode_experiment_relationship', 
    'decode_experiment_relationship_target', 
    'decode_measurement_campaign', 
    'decode_numerical_experiment', 
    'decode_simulation_relationship', 
    'decode_simulation_relationship_target'
]


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="2012-03-09 12:06:12.690970"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"


def decode_activity(xml, nsmap):
    """Decodes a activity instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(Activity(), xml, nsmap, decodings)


def decode_experiment(xml, nsmap):
    """Decodes a experiment instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(Experiment(), xml, nsmap, decodings)


def decode_experiment_relationship(xml, nsmap):
    """Decodes a experiment relationship instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(ExperimentRelationship(), xml, nsmap, decodings)


def decode_experiment_relationship_target(xml, nsmap):
    """Decodes a experiment relationship target instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(ExperimentRelationshipTarget(), xml, nsmap, decodings)


def decode_measurement_campaign(xml, nsmap):
    """Decodes a measurement campaign instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(MeasurementCampaign(), xml, nsmap, decodings)


def decode_numerical_experiment(xml, nsmap):
    """Decodes a numerical experiment instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(NumericalExperiment(), xml, nsmap, decodings)


def decode_simulation_relationship(xml, nsmap):
    """Decodes a simulation relationship instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(SimulationRelationship(), xml, nsmap, decodings)


def decode_simulation_relationship_target(xml, nsmap):
    """Decodes a simulation relationship target instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(SimulationRelationshipTarget(), xml, nsmap, decodings)


