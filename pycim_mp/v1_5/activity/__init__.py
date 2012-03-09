"""
The cim v1.5 ontology - activity package.
"""

# Module imports.
from pycim_mp.v1_5.activity.classes import classes
from pycim_mp.v1_5.activity.enums import enums


# Module exports.
__all__ = ["package"]


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"

# CIM v1.5 - activity package.
package = {
    'name' : 'activity',
    'doc' : 'TODO get package documentation',
    'classes' : classes,
    'enums' : enums,
}
