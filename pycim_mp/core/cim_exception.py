"""A CIM meta-programming exception class.

"""

# Module exports.
__all__ = ['CIMException']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"


class CIMException(Exception):
    """A CIM meta-programming exception class.
    
    """

    def __init__(self, message):
        """Contructor.

        Keyword Arguments:
        self -- pointer to this object.

        """
        self.message = message


    def __str__(self):
        """Contructor.

        Keyword Arguments:
        self -- pointer to this object.

        """
        return "CIM CODE-GEN :: !!! EXCEPTION !!! : {0}".format(repr(self.message))
