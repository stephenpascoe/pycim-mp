"""A CIM meta-programming ontology decoding information.

"""

# Module imports.


# Module exports.
__all__ = ['DecodingInfo']


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"


class DecodingInfo(object):
    """Represents information used for decoding.

    """

    def __init__(self, property_name, decoding, type):
        """Constructor.

        Keyword Arguments:
        config - decoding configuration.

        """
        # Set attributes.
        self.__property_name = property_name
        self.__decoding = decoding
        self.__type = type


    @property
    def property_name(self):
        """Gets name of class property that decoding applies to."""
        return self.__property_name


    @property
    def decoding(self):
        """Gets decoding."""
        return self.__decoding


    @property
    def type(self):
        """Gets sub type that decoding should be deserialized to."""
        return self.__type
