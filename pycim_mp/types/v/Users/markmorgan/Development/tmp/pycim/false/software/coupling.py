"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.762500.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid

from cim.v1_5.types.shared.data_purpose import DataPurpose
from cim.v1_5.types.software.coupling_property import CouplingProperty


# Module exports.
__all__ = ['Coupling']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.762500$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Coupling(object):
    """A class within the cim v1.5 type system.

    A coupling represents a set of Connections between a source and target component. Couplings can be complete or incomplete. If they are complete then they must include all Connections between model properties. If they are incomplete then the connections can be underspecified or not listed at all.
    """
    def __init__(self):
        """Constructor"""
        super(Coupling, self).__init__()

        self.__connections = []                                     # type = str
        self.__coupling_properties = []                             # type = software.CouplingProperty
        self.__coupling_source = []                                 # type = str
        self.__coupling_target = str()                              # type = str
        self.__description = None                                   # type = str
        self.__is_fully_specified = bool()                          # type = bool
        self.__priming = None                                       # type = str
        self.__purpose = shared.data_purpose()                      # type = shared.DataPurpose
        self.__spatial_regridding = []                              # type = str
        self.__time_lag = None                                      # type = str
        self.__time_profile = None                                  # type = str
        self.__time_transformation = None                           # type = str
        self.__transformers = []                                    # type = str
        self.__type = None                                          # type = str


    @property
    def connections(self):
        """Gets value of {class-name} connections property."""
        return list(self.__connections)

    @connections.setter
    def connections(self, value):
        """Sets value of {class-name} connections property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__connections = []
        for i in value:
            self.append_to_connections(i)

    @connections.deleter
    def connections(self, value):
        """Deletes {class-name} connections property."""
        raise TypeError("Cannot delete {class-name} connections property.")

    def append_to_connections(self, item):
        """Appends an item to the managed {class-name} connections collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__connections.append(item)

    def remove_from_connections(self, item):
        """Removes an item from the managed {class-name} connections collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__connections.remove(item)


    @property
    def coupling_properties(self):
        """Gets value of {class-name} coupling_properties property."""
        return list(self.__coupling_properties)

    @coupling_properties.setter
    def coupling_properties(self, value):
        """Sets value of {class-name} coupling_properties property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__coupling_properties = []
        for i in value:
            self.append_to_coupling_properties(i)

    @coupling_properties.deleter
    def coupling_properties(self, value):
        """Deletes {class-name} coupling_properties property."""
        raise TypeError("Cannot delete {class-name} coupling_properties property.")

    def append_to_coupling_properties(self, item):
        """Appends an item to the managed {class-name} coupling_properties collection."""
        if not isinstance(item, CouplingProperty):
            raise TypeError("item is of incorrect type.")
        self.__coupling_properties.append(item)

    def remove_from_coupling_properties(self, item):
        """Removes an item from the managed {class-name} coupling_properties collection."""
        if not isinstance(item, CouplingProperty):
            raise TypeError("item is of incorrect type.")
        self.__coupling_properties.remove(item)


    @property
    def coupling_source(self):
        """Gets value of {class-name} coupling_source property.

        The source component of the coupling. (note that there can be multiple sources)."""
        return list(self.__coupling_source)

    @coupling_source.setter
    def coupling_source(self, value):
        """Sets value of {class-name} coupling_source property.

        The source component of the coupling. (note that there can be multiple sources)."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__coupling_source = []
        for i in value:
            self.append_to_coupling_source(i)

    @coupling_source.deleter
    def coupling_source(self, value):
        """Deletes {class-name} coupling_source property."""
        raise TypeError("Cannot delete {class-name} coupling_source property.")

    def append_to_coupling_source(self, item):
        """Appends an item to the managed {class-name} coupling_source collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__coupling_source.append(item)

    def remove_from_coupling_source(self, item):
        """Removes an item from the managed {class-name} coupling_source collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__coupling_source.remove(item)


    @property
    def coupling_target(self):
        """Gets value of coupling coupling_target property.

        The target component of the coupling."""
        return self.__coupling_target

    @coupling_target.setter
    def coupling_target(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, str):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of coupling coupling_target property."""
        self.__coupling_target = value

    @coupling_target.deleter
    def coupling_target(self, value):
        """Deletes coupling coupling_target property."""
        raise TypeError("Cannot delete coupling coupling_target property.")


    @property
    def description(self):
        """Gets value of {class-name} description property.

        A free-text description of the coupling."""
        return self.__description

    @description.setter
    def description(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} description property."""
        self.__description = value

    @description.deleter
    def description(self, value):
        """Deletes {class-name} description property."""
        raise TypeError("Cannot delete {class-name} description property.")


    @property
    def is_fully_specified(self):
        """Gets value of coupling is_fully_specified property."""
        return self.__is_fully_specified

    @is_fully_specified.setter
    def is_fully_specified(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, bool):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of coupling is_fully_specified property."""
        self.__is_fully_specified = value

    @is_fully_specified.deleter
    def is_fully_specified(self, value):
        """Deletes coupling is_fully_specified property."""
        raise TypeError("Cannot delete coupling is_fully_specified property.")


    @property
    def priming(self):
        """Gets value of {class-name} priming property.

        A priming source is one that is active on the first available timestep only (before "proper" coupling can ocurr). It can either be described here explicitly, or else a separate coupling/connection with a timing profile that is active on only the first timestep can be created."""
        return self.__priming

    @priming.setter
    def priming(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} priming property."""
        self.__priming = value

    @priming.deleter
    def priming(self, value):
        """Deletes {class-name} priming property."""
        raise TypeError("Cannot delete {class-name} priming property.")


    @property
    def purpose(self):
        """Gets value of coupling purpose property."""
        return self.__purpose

    @purpose.setter
    def purpose(self, value):
        if value is None:
            raise TypeError("Value cannot be null.")
        elif not isinstance(value, DataPurpose):
            raise TypeError("Invalid value type : VALUE = {0}.".format(value))
        """Sets value of coupling purpose property."""
        self.__purpose = value

    @purpose.deleter
    def purpose(self, value):
        """Deletes coupling purpose property."""
        raise TypeError("Cannot delete coupling purpose property.")


    @property
    def spatial_regridding(self):
        """Gets value of {class-name} spatial_regridding property.

        Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid)."""
        return list(self.__spatial_regridding)

    @spatial_regridding.setter
    def spatial_regridding(self, value):
        """Sets value of {class-name} spatial_regridding property.

        Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid)."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__spatial_regridding = []
        for i in value:
            self.append_to_spatial_regridding(i)

    @spatial_regridding.deleter
    def spatial_regridding(self, value):
        """Deletes {class-name} spatial_regridding property."""
        raise TypeError("Cannot delete {class-name} spatial_regridding property.")

    def append_to_spatial_regridding(self, item):
        """Appends an item to the managed {class-name} spatial_regridding collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__spatial_regridding.append(item)

    def remove_from_spatial_regridding(self, item):
        """Removes an item from the managed {class-name} spatial_regridding collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__spatial_regridding.remove(item)


    @property
    def time_lag(self):
        """Gets value of {class-name} time_lag property.

        The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time."""
        return self.__time_lag

    @time_lag.setter
    def time_lag(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} time_lag property."""
        self.__time_lag = value

    @time_lag.deleter
    def time_lag(self, value):
        """Deletes {class-name} time_lag property."""
        raise TypeError("Cannot delete {class-name} time_lag property.")


    @property
    def time_profile(self):
        """Gets value of {class-name} time_profile property.

        Describes how often the coupling takes place."""
        return self.__time_profile

    @time_profile.setter
    def time_profile(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} time_profile property."""
        self.__time_profile = value

    @time_profile.deleter
    def time_profile(self, value):
        """Deletes {class-name} time_profile property."""
        raise TypeError("Cannot delete {class-name} time_profile property.")


    @property
    def time_transformation(self):
        """Gets value of {class-name} time_transformation property.

        Temporal transformation performed on the coupling field before or after regridding onto the target grid."""
        return self.__time_transformation

    @time_transformation.setter
    def time_transformation(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} time_transformation property."""
        self.__time_transformation = value

    @time_transformation.deleter
    def time_transformation(self, value):
        """Deletes {class-name} time_transformation property."""
        raise TypeError("Cannot delete {class-name} time_transformation property.")


    @property
    def transformers(self):
        """Gets value of {class-name} transformers property.

        An "in-line" transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here."""
        return list(self.__transformers)

    @transformers.setter
    def transformers(self, value):
        """Sets value of {class-name} transformers property.

        An "in-line" transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__transformers = []
        for i in value:
            self.append_to_transformers(i)

    @transformers.deleter
    def transformers(self, value):
        """Deletes {class-name} transformers property."""
        raise TypeError("Cannot delete {class-name} transformers property.")

    def append_to_transformers(self, item):
        """Appends an item to the managed {class-name} transformers collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__transformers.append(item)

    def remove_from_transformers(self, item):
        """Removes an item from the managed {class-name} transformers collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__transformers.remove(item)


    @property
    def type(self):
        """Gets value of {class-name} type property.

        Describes the method of coupling."""
        return self.__type

    @type.setter
    def type(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} type property."""
        self.__type = value

    @type.deleter
    def type(self, value):
        """Deletes {class-name} type property."""
        raise TypeError("Cannot delete {class-name} type property.")



    def as_dict(self):
        """Gets dictionary representation of self used to create other representations such as json, xml ...etc.

        """
        def append(d, key, value, is_iterative, is_primitive, is_enum):
            if value is None:
                if is_iterative:
                    value = []
            elif is_primitive == False and is_enum == False:
                if is_iterative:
                    value = map(lambda i : i.as_dict(), value)
                else:
                    value = value.as_dict()
            d[key] = value

        # Populate a deep dictionary.
        d = dict()
        append(d, 'connections', self.__connections, True, True, False)
        append(d, 'coupling_properties', self.__coupling_properties, True, False, False)
        append(d, 'coupling_source', self.__coupling_source, True, True, False)
        append(d, 'coupling_target', self.__coupling_target, False, True, False)
        append(d, 'description', self.__description, False, True, False)
        append(d, 'is_fully_specified', self.__is_fully_specified, False, True, False)
        append(d, 'priming', self.__priming, False, True, False)
        append(d, 'purpose', self.__purpose, False, False, False)
        append(d, 'spatial_regridding', self.__spatial_regridding, True, True, False)
        append(d, 'time_lag', self.__time_lag, False, True, False)
        append(d, 'time_profile', self.__time_profile, False, True, False)
        append(d, 'time_transformation', self.__time_transformation, False, True, False)
        append(d, 'transformers', self.__transformers, True, True, False)
        append(d, 'type', self.__type, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = Coupling()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('software.Coupling', e)
