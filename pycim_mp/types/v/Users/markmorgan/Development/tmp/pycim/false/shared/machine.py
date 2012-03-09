"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.748981.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid



# Module exports.
__all__ = ['Machine']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.748981$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Machine(object):
    """A class within the cim v1.5 type system.

    A description of a machine used by a particular platform
    """
    def __init__(self):
        """Constructor"""
        super(Machine, self).__init__()

        self.__cores_per_processor = None                           # type = int
        self.__description = None                                   # type = str
        self.__interconnect = None                                  # type = str
        self.__libraries = []                                       # type = str
        self.__location = None                                      # type = str
        self.__maximum_processors = None                            # type = int
        self.__name = None                                          # type = str
        self.__operating_system = None                              # type = str
        self.__processor_type = None                                # type = str
        self.__system = None                                        # type = str
        self.__type = None                                          # type = str
        self.__vendor = None                                        # type = str


    @property
    def cores_per_processor(self):
        """Gets value of {class-name} cores_per_processor property."""
        return self.__cores_per_processor

    @cores_per_processor.setter
    def cores_per_processor(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} cores_per_processor property."""
        self.__cores_per_processor = value

    @cores_per_processor.deleter
    def cores_per_processor(self, value):
        """Deletes {class-name} cores_per_processor property."""
        raise TypeError("Cannot delete {class-name} cores_per_processor property.")


    @property
    def description(self):
        """Gets value of {class-name} description property."""
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
    def interconnect(self):
        """Gets value of {class-name} interconnect property."""
        return self.__interconnect

    @interconnect.setter
    def interconnect(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} interconnect property."""
        self.__interconnect = value

    @interconnect.deleter
    def interconnect(self, value):
        """Deletes {class-name} interconnect property."""
        raise TypeError("Cannot delete {class-name} interconnect property.")


    @property
    def libraries(self):
        """Gets value of {class-name} libraries property.

        The libraries residing on this machine."""
        return list(self.__libraries)

    @libraries.setter
    def libraries(self, value):
        """Sets value of {class-name} libraries property.

        The libraries residing on this machine."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__libraries = []
        for i in value:
            self.append_to_libraries(i)

    @libraries.deleter
    def libraries(self, value):
        """Deletes {class-name} libraries property."""
        raise TypeError("Cannot delete {class-name} libraries property.")

    def append_to_libraries(self, item):
        """Appends an item to the managed {class-name} libraries collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__libraries.append(item)

    def remove_from_libraries(self, item):
        """Removes an item from the managed {class-name} libraries collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__libraries.remove(item)


    @property
    def location(self):
        """Gets value of {class-name} location property."""
        return self.__location

    @location.setter
    def location(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} location property."""
        self.__location = value

    @location.deleter
    def location(self, value):
        """Deletes {class-name} location property."""
        raise TypeError("Cannot delete {class-name} location property.")


    @property
    def maximum_processors(self):
        """Gets value of {class-name} maximum_processors property."""
        return self.__maximum_processors

    @maximum_processors.setter
    def maximum_processors(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} maximum_processors property."""
        self.__maximum_processors = value

    @maximum_processors.deleter
    def maximum_processors(self, value):
        """Deletes {class-name} maximum_processors property."""
        raise TypeError("Cannot delete {class-name} maximum_processors property.")


    @property
    def name(self):
        """Gets value of {class-name} name property."""
        return self.__name

    @name.setter
    def name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} name property."""
        self.__name = value

    @name.deleter
    def name(self, value):
        """Deletes {class-name} name property."""
        raise TypeError("Cannot delete {class-name} name property.")


    @property
    def operating_system(self):
        """Gets value of {class-name} operating_system property."""
        return self.__operating_system

    @operating_system.setter
    def operating_system(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} operating_system property."""
        self.__operating_system = value

    @operating_system.deleter
    def operating_system(self, value):
        """Deletes {class-name} operating_system property."""
        raise TypeError("Cannot delete {class-name} operating_system property.")


    @property
    def processor_type(self):
        """Gets value of {class-name} processor_type property."""
        return self.__processor_type

    @processor_type.setter
    def processor_type(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} processor_type property."""
        self.__processor_type = value

    @processor_type.deleter
    def processor_type(self, value):
        """Deletes {class-name} processor_type property."""
        raise TypeError("Cannot delete {class-name} processor_type property.")


    @property
    def system(self):
        """Gets value of {class-name} system property."""
        return self.__system

    @system.setter
    def system(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} system property."""
        self.__system = value

    @system.deleter
    def system(self, value):
        """Deletes {class-name} system property."""
        raise TypeError("Cannot delete {class-name} system property.")


    @property
    def type(self):
        """Gets value of {class-name} type property."""
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


    @property
    def vendor(self):
        """Gets value of {class-name} vendor property."""
        return self.__vendor

    @vendor.setter
    def vendor(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} vendor property."""
        self.__vendor = value

    @vendor.deleter
    def vendor(self, value):
        """Deletes {class-name} vendor property."""
        raise TypeError("Cannot delete {class-name} vendor property.")



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
        append(d, 'cores_per_processor', self.__cores_per_processor, False, True, False)
        append(d, 'description', self.__description, False, True, False)
        append(d, 'interconnect', self.__interconnect, False, True, False)
        append(d, 'libraries', self.__libraries, True, True, False)
        append(d, 'location', self.__location, False, True, False)
        append(d, 'maximum_processors', self.__maximum_processors, False, True, False)
        append(d, 'name', self.__name, False, True, False)
        append(d, 'operating_system', self.__operating_system, False, True, False)
        append(d, 'processor_type', self.__processor_type, False, True, False)
        append(d, 'system', self.__system, False, True, False)
        append(d, 'type', self.__type, False, True, False)
        append(d, 'vendor', self.__vendor, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = Machine()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('shared.Machine', e)
