"""A set of cim 1.5 decodings.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.698621.
"""

# Module imports.
from cim.core.decoding.cim_decoder_xml_utils import *
from cim.v1_5.decoding.decoder_for_shared_package import decode_cim_info
from cim.v1_5.decoding.decoder_for_shared_package import decode_cim_info
from cim.v1_5.decoding.decoder_for_shared_package import decode_citation
from cim.v1_5.decoding.decoder_for_shared_package import decode_citation
from cim.v1_5.decoding.decoder_for_shared_package import decode_data_purpose
from cim.v1_5.decoding.decoder_for_shared_package import decode_license
from cim.v1_5.decoding.decoder_for_shared_package import decode_responsible_party
from cim.v1_5.decoding.decoder_for_shared_package import decode_unit_type
from cim.v1_5.types.software.component_language import ComponentLanguage
from cim.v1_5.types.software.component_language_property import ComponentLanguageProperty
from cim.v1_5.types.software.component_property import ComponentProperty
from cim.v1_5.types.software.composition import Composition
from cim.v1_5.types.software.coupling import Coupling
from cim.v1_5.types.software.coupling_property import CouplingProperty
from cim.v1_5.types.software.deployment import Deployment
from cim.v1_5.types.software.entry_point import EntryPoint
from cim.v1_5.types.software.model_component import ModelComponent
from cim.v1_5.types.software.parallelisation import Parallelisation
from cim.v1_5.types.software.processor_component import ProcessorComponent
from cim.v1_5.types.software.rank import Rank
from cim.v1_5.types.software.software_component import SoftwareComponent
from cim.v1_5.types.software.timing import Timing


# Module exports.
__all__ = [
    'decode_component_language', 
    'decode_component_language_property', 
    'decode_component_property', 
    'decode_composition', 
    'decode_coupling', 
    'decode_coupling_property', 
    'decode_deployment', 
    'decode_entry_point', 
    'decode_model_component', 
    'decode_parallelisation', 
    'decode_processor_component', 
    'decode_rank', 
    'decode_software_component', 
    'decode_timing'
]


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="2012-03-09 12:06:12.698621"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"


def decode_component_language(xml, nsmap):
    """Decodes a component language instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(ComponentLanguage(), xml, nsmap, decodings)


def decode_component_language_property(xml, nsmap):
    """Decodes a component language property instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name/text()'),
        ('value', False, 'str', 'child::cim:value/text()'),
    ]

    return set_attributes(ComponentLanguageProperty(), xml, nsmap, decodings)


def decode_component_property(xml, nsmap):
    """Decodes a component property instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('citations', True, decode_citation, 'child::cim:citation'),
        ('component_properties', True, decode_component_property, 'child::cim:componentProperty'),
        ('description', False, 'str', 'child::cim:description/text()'),
        ('grid', False, 'str', 'None'),
        ('intent', False, decode_component_property_intent_type, 'self::cim:componentProperty/@intent'),
        ('is_represented', False, 'bool', 'self::cim:componentProperty/@represented'),
        ('long_name', False, 'str', 'child::cim:longName/text()'),
        ('short_name', False, 'str', 'child::cim:shortName/text()'),
        ('standard_names', True, 'str', 'child::cim:standardName/@value'),
        ('units', False, decode_unit_type, 'child::cim:units/@value'),
        ('value', False, 'str', 'child::cim:value/text()'),
        ('values', True, 'str', 'None'),
    ]

    return set_attributes(ComponentProperty(), xml, nsmap, decodings)


def decode_composition(xml, nsmap):
    """Decodes a composition instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(Composition(), xml, nsmap, decodings)


def decode_coupling(xml, nsmap):
    """Decodes a coupling instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(Coupling(), xml, nsmap, decodings)


def decode_coupling_property(xml, nsmap):
    """Decodes a coupling property instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name/text()'),
        ('value', False, 'str', 'child::cim:value/text()'),
    ]

    return set_attributes(CouplingProperty(), xml, nsmap, decodings)


def decode_deployment(xml, nsmap):
    """Decodes a deployment instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(Deployment(), xml, nsmap, decodings)


def decode_entry_point(xml, nsmap):
    """Decodes a entry point instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(EntryPoint(), xml, nsmap, decodings)


def decode_model_component(xml, nsmap):
    """Decodes a model component instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('cim_info', False, decode_cim_info, 'self::cim:modelComponent'),
        ('types', True, decode_model_component_type, 'child::cim:type/@value'),
        ('child_components', True, decode_model_component, 'child::cim:childComponent/cim:modelComponent'),
        ('child_components', True, decode_processor_component, 'child::cim:childComponent/cim:processorComponent'),
        ('citations', True, decode_citation, 'child::cim:citation'),
        ('component_properties', True, decode_component_property, 'child::cim:componentProperties/cim:componentProperty'),
        ('description', False, 'str', 'child::cim:description/text()'),
        ('long_name', False, 'str', 'child::cim:longName/text()'),
        ('release_date', False, 'datetime', 'child::cim:releaseDate/text()'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'str', 'child::cim:shortName/text()'),
    ]

    return set_attributes(ModelComponent(), xml, nsmap, decodings)


def decode_parallelisation(xml, nsmap):
    """Decodes a parallelisation instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(Parallelisation(), xml, nsmap, decodings)


def decode_processor_component(xml, nsmap):
    """Decodes a processor component instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('cim_info', False, decode_cim_info, 'self::cim:modelComponent'),
        ('child_components', True, decode_model_component, 'child::cim:childComponent/cim:modelComponent'),
        ('child_components', True, decode_processor_component, 'child::cim:childComponent/cim:processorComponent'),
        ('citations', True, decode_citation, 'child::cim:citation'),
        ('component_properties', True, decode_component_property, 'child::cim:componentProperties/cim:componentProperty'),
        ('description', False, 'str', 'child::cim:description/text()'),
        ('long_name', False, 'str', 'child::cim:longName/text()'),
        ('release_date', False, 'datetime', 'child::cim:releaseDate/text()'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'str', 'child::cim:shortName/text()'),
    ]

    return set_attributes(ProcessorComponent(), xml, nsmap, decodings)


def decode_rank(xml, nsmap):
    """Decodes a rank instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(Rank(), xml, nsmap, decodings)


def decode_software_component(xml, nsmap):
    """Decodes a software component instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
        ('child_components', True, decode_model_component, 'child::cim:childComponent/cim:modelComponent'),
        ('child_components', True, decode_processor_component, 'child::cim:childComponent/cim:processorComponent'),
        ('citations', True, decode_citation, 'child::cim:citation'),
        ('component_properties', True, decode_component_property, 'child::cim:componentProperties/cim:componentProperty'),
        ('description', False, 'str', 'child::cim:description/text()'),
        ('long_name', False, 'str', 'child::cim:longName/text()'),
        ('release_date', False, 'datetime', 'child::cim:releaseDate/text()'),
        ('responsible_parties', True, decode_responsible_party, 'child::cim:responsibleParty'),
        ('short_name', False, 'str', 'child::cim:shortName/text()'),
    ]

    return set_attributes(SoftwareComponent(), xml, nsmap, decodings)


def decode_timing(xml, nsmap):
    """Decodes a timing instance from xml.

    Keyword arguments:
    xml -- etree xml element from which entity is to be decoded.
    nsmap -- set of xml namespace mappings.

    """
    decodings = [
    ]

    return set_attributes(Timing(), xml, nsmap, decodings)


