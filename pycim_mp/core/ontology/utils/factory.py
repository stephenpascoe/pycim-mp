"""A set of CIM meta-programming ontology factory functions.

"""
# Module level imports.
from pycim_mp.core.ontology.decoding_info import DecodingInfo
from pycim_mp.core.cim_exception import CIMException
from pycim_mp.core.ontology.utils.validate import validate as validate_ontology_config


# Module level exports.
__all__ = ['create']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"


# Set of supported simple types.
_simples = set(['bool', 'date', 'datetime', 'float', 'int', 'str', 'uri', 'uuid', ])


def _validate_config(o_cfg):
    """Validates ontology configuration.

    Keyword Arguments:
    o_cfg - ontology configuration.

    """
    cfg_errors = validate_ontology_config(o_cfg)
    if len(cfg_errors) > 0:
        raise CIMException("Ontology configuration is invalid.")


def _validate(o):
    """Validates ontology.

    Keyword Arguments:
    o - ontology being instantiated.

    """
    pass


def _create(o_cfg):
    """Factory method to instantiate an ontology instance from configuration.

    Keyword Arguments:
    o_cfg - ontology configuration.

    """
    from pycim_mp.core.ontology import ClassInfo
    from pycim_mp.core.ontology import EnumInfo
    from pycim_mp.core.ontology import EnumMemberInfo
    from pycim_mp.core.ontology import OntologyInfo
    from pycim_mp.core.ontology import PackageInfo
    from pycim_mp.core.ontology import PropertyInfo

    o_packages = []
    for p_cfg in o_cfg['packages']:
        # ... package classes
        p_classes = []
        for c_cfg in p_cfg['classes']:
            # ... class properties
            c_properties = []
            for cp_cfg in c_cfg['properties']:
                c_properties.append(PropertyInfo(cp_cfg[0], cp_cfg[3], cp_cfg[1], cp_cfg[2]))

            # ... class decodings
            c_decodings = []
            for d_cfg in c_cfg['decodings']:
                c_decoding = cp_name = cp_decoding = cp_type = None
                if len(d_cfg) == 2:
                    cp_name, cp_decoding = d_cfg
                elif len(d_cfg) == 3:
                    cp_name, cp_decoding, cp_type = d_cfg
                c_decoding = DecodingInfo(cp_name, cp_decoding, cp_type)
                c_decodings.append(c_decoding)

            # ... class
            c = ClassInfo(c_cfg['name'], c_cfg['base'], c_cfg['abstract'], c_cfg['doc'], c_properties, c_decodings)
            p_classes.append(c)

        # ... package enums
        p_enums = []
        for e_cfg in p_cfg['enums']:
            # ... enum members
            e_members = []
            for em_cfg in e_cfg['members']:
                em_name = em_cfg[0]
                em_doc = em_cfg[1]
                e_members.append(EnumMemberInfo(em_name, em_doc))

            # ... enum
            p_enums.append(EnumInfo(e_cfg['name'], e_cfg['is_open'], e_cfg['doc'], e_members))

        # ... package
        o_packages.append(PackageInfo(p_cfg['name'], p_cfg['doc'], p_classes, p_enums))

    return OntologyInfo(o_cfg['name'], o_cfg['version'], o_cfg['doc'], o_packages)

    
def create(o_cfg):
    """Factory method to instantiate an ontology instance from configuration.

    Keyword Arguments:
    o_cfg - ontology configuration.
    
    """
    # Validate config.
    _validate_config(o_cfg)

    # Create, initialise & validate ontology.
    o = _create(o_cfg)
    _validate(o)
    
    return o


# Command line entry point.
if __name__ == "__main__":
    from pycim_mp.v1_5 import ontology as o_cfg
    o = create(o_cfg)
    print o, o.packages


