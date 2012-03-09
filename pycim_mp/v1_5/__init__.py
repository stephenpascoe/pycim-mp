"""The cim v1.5 ontology.

"""

# Module imports.
from pycim_mp.v1_5.activity import package as activity_package
from pycim_mp.v1_5.data import package as data_package
from pycim_mp.v1_5.grids import package as grids_package
from pycim_mp.v1_5.quality import package as quality_package
from pycim_mp.v1_5.shared import package as shared_package
from pycim_mp.v1_5.software import package as software_package


# Module exports.
__all__ = ["ontology"]


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"

# Ontology :: CIM v1.5.
ontology = {
    'name' : 'cim',
    'version' : '1.5',
    'doc' : 'CIM ontology - version 1.5',
    'packages' : [
        activity_package,
        data_package,
        grids_package,
        quality_package,
        shared_package,
        software_package
    ]
}