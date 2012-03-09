"""A set of cim 1.5 decoding packages.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.690128.
"""

# Module imports.
from lxml import etree as et

from cim.core.cim_exception import CIMException
from cim.core.decoding.cim_decoder_xml_utils import get_cim_xml
from cim.core.decoding.cim_decoder_xml_utils import decode_xml
from cim.v1_5.decoding.decoder_for_activity_package import decode_numerical_experiment
from cim.v1_5.decoding.decoder_for_data_package import decode_data_object
from cim.v1_5.decoding.decoder_for_software_package import decode_model_component
from cim.v1_5.decoding.decoder_for_software_package import decode_processor_component

# Module exports.
__all__ = ['decode_numerical_experiment', 'decode_data_object', 'decode_model_component', 'decode_processor_component']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="2012-03-09 12:06:12.690128"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"

