"""A class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.764286.
"""

# Module imports.
import datetime
import simplejson
import types
import uuid



# Module exports.
__all__ = ['Deployment']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.764286$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Deployment(object):
    """A class within the cim v1.5 type system.

    Gives information about the technical properties of a component: what machine it was run on, which compilers were used, how it was parallised, etc. A deployment basically associates a deploymentDate with a Platform. A deployment only exists if something has been deployed. A platform, in contrast, can exist independently, waiting to be used in deployments.
    """
    def __init__(self):
        """Constructor"""
        super(Deployment, self).__init__()

        self.__deployment_date = None                               # type = datetime.datetime
        self.__description = None                                   # type = str
        self.__executable_argument = []                             # type = str
        self.__executable_name = None                               # type = str
        self.__parallelisation = None                               # type = str
        self.__platform = None                                      # type = str


    @property
    def deployment_date(self):
        """Gets value of {class-name} deployment_date property."""
        return self.__deployment_date

    @deployment_date.setter
    def deployment_date(self, value):
        if value is not None and not isinstance(value, datetime.datetime):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} deployment_date property."""
        self.__deployment_date = value

    @deployment_date.deleter
    def deployment_date(self, value):
        """Deletes {class-name} deployment_date property."""
        raise TypeError("Cannot delete {class-name} deployment_date property.")


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
    def executable_argument(self):
        """Gets value of {class-name} executable_argument property."""
        return list(self.__executable_argument)

    @executable_argument.setter
    def executable_argument(self, value):
        """Sets value of {class-name} executable_argument property."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__executable_argument = []
        for i in value:
            self.append_to_executable_argument(i)

    @executable_argument.deleter
    def executable_argument(self, value):
        """Deletes {class-name} executable_argument property."""
        raise TypeError("Cannot delete {class-name} executable_argument property.")

    def append_to_executable_argument(self, item):
        """Appends an item to the managed {class-name} executable_argument collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__executable_argument.append(item)

    def remove_from_executable_argument(self, item):
        """Removes an item from the managed {class-name} executable_argument collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__executable_argument.remove(item)


    @property
    def executable_name(self):
        """Gets value of {class-name} executable_name property."""
        return self.__executable_name

    @executable_name.setter
    def executable_name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} executable_name property."""
        self.__executable_name = value

    @executable_name.deleter
    def executable_name(self, value):
        """Deletes {class-name} executable_name property."""
        raise TypeError("Cannot delete {class-name} executable_name property.")


    @property
    def parallelisation(self):
        """Gets value of {class-name} parallelisation property."""
        return self.__parallelisation

    @parallelisation.setter
    def parallelisation(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} parallelisation property."""
        self.__parallelisation = value

    @parallelisation.deleter
    def parallelisation(self, value):
        """Deletes {class-name} parallelisation property."""
        raise TypeError("Cannot delete {class-name} parallelisation property.")


    @property
    def platform(self):
        """Gets value of {class-name} platform property.

        The platform that this deployment has been run on. It is optional to allow for "unconfigured" models, that nonetheless specify their parallelisation constraints (a feature needed by OASIS)."""
        return self.__platform

    @platform.setter
    def platform(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Invalid value type  : VALUE = {0}.".format(value))
        """Sets value of {class-name} platform property."""
        self.__platform = value

    @platform.deleter
    def platform(self, value):
        """Deletes {class-name} platform property."""
        raise TypeError("Cannot delete {class-name} platform property.")



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
        append(d, 'deployment_date', self.__deployment_date, False, True, False)
        append(d, 'description', self.__description, False, True, False)
        append(d, 'executable_argument', self.__executable_argument, True, True, False)
        append(d, 'executable_name', self.__executable_name, False, True, False)
        append(d, 'parallelisation', self.__parallelisation, False, True, False)
        append(d, 'platform', self.__platform, False, True, False)
        return d




# Command line entry point.
if __name__ == "__main__":
    try:
        i = Deployment()
    except Exception as e:
        print "CIM INSTANTIATION EXCEPTION !!! :: TYPE = {0} : ERROR = {1}.".format('software.Deployment', e)
