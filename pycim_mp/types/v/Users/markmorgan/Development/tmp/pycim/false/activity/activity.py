"""An abstract class within cim v1.5 type system.

CIM CODE GENERATOR :: Code generated @ 2012-03-09 12:06:12.705698.
"""

# Module imports.
import abc
from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty
import datetime
import types
import uuid

from cim.v1_5.types.activity.project_type import ProjectType
from cim.v1_5.types.shared.responsible_party import ResponsibleParty


# Module exports.
__all__ = ['Activity']


# Module provenance info.
__author__="Mark Morgan"
__copyright__ = "Copyright 2012 - Institut Pierre Simon Laplace."
__date__ ="$2012-03-09 12:06:12.705698$"
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Mark Morgan"
__email__ = "momipsl@ipsl.jussieu.fr"
__status__ = "Production"



class Activity(object):
    """An abstract class within the cim v1.5 type system.

    An abstract class used as the parent of MeasurementCampaigns, Projects, Experiments, and NumericalActivities.
    """
    # Abstract Base Class module - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def __init__(self):
        """Constructor"""
        super(Activity, self).__init__()

        self.__funding_sources = []                                 # type = str
        self.__projects = []                                        # type = activity.ProjectType
        self.__rationale = []                                       # type = str
        self.__responsible_parties = []                             # type = shared.ResponsibleParty


    @property
    def funding_sources(self):
        """Gets value of {class-name} funding_sources property.

        The entities that funded this activity."""
        return list(self.__funding_sources)

    @funding_sources.setter
    def funding_sources(self, value):
        """Sets value of {class-name} funding_sources property.

        The entities that funded this activity."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__funding_sources = []
        for i in value:
            self.append_to_funding_sources(i)

    @funding_sources.deleter
    def funding_sources(self, value):
        """Deletes {class-name} funding_sources property."""
        raise TypeError("Cannot delete {class-name} funding_sources property.")

    def append_to_funding_sources(self, item):
        """Appends an item to the managed {class-name} funding_sources collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__funding_sources.append(item)

    def remove_from_funding_sources(self, item):
        """Removes an item from the managed {class-name} funding_sources collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__funding_sources.remove(item)


    @property
    def projects(self):
        """Gets value of {class-name} projects property.

        The project(s) that this activity is associated with (ie: CMIP5, AMIP, etc)."""
        return list(self.__projects)

    @projects.setter
    def projects(self, value):
        """Sets value of {class-name} projects property.

        The project(s) that this activity is associated with (ie: CMIP5, AMIP, etc)."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__projects = []
        for i in value:
            self.append_to_projects(i)

    @projects.deleter
    def projects(self, value):
        """Deletes {class-name} projects property."""
        raise TypeError("Cannot delete {class-name} projects property.")

    def append_to_projects(self, item):
        """Appends an item to the managed {class-name} projects collection."""
        if not isinstance(item, ProjectType):
            raise TypeError("item is of incorrect type.")
        self.__projects.append(item)

    def remove_from_projects(self, item):
        """Removes an item from the managed {class-name} projects collection."""
        if not isinstance(item, ProjectType):
            raise TypeError("item is of incorrect type.")
        self.__projects.remove(item)


    @property
    def rationale(self):
        """Gets value of {class-name} rationale property.

        For what purpose is this activity being performed?"""
        return list(self.__rationale)

    @rationale.setter
    def rationale(self, value):
        """Sets value of {class-name} rationale property.

        For what purpose is this activity being performed?"""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__rationale = []
        for i in value:
            self.append_to_rationale(i)

    @rationale.deleter
    def rationale(self, value):
        """Deletes {class-name} rationale property."""
        raise TypeError("Cannot delete {class-name} rationale property.")

    def append_to_rationale(self, item):
        """Appends an item to the managed {class-name} rationale collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__rationale.append(item)

    def remove_from_rationale(self, item):
        """Removes an item from the managed {class-name} rationale collection."""
        if not isinstance(item, str):
            raise TypeError("item is of incorrect type.")
        self.__rationale.remove(item)


    @property
    def responsible_parties(self):
        """Gets value of {class-name} responsible_parties property.

        The point of contact(s) for this activity.This includes, among others, the principle investigator."""
        return list(self.__responsible_parties)

    @responsible_parties.setter
    def responsible_parties(self, value):
        """Sets value of {class-name} responsible_parties property.

        The point of contact(s) for this activity.This includes, among others, the principle investigator."""
        if not isinstance(value, types.ListType):
            raise TypeError("value must be an iterable type.")
        self.__responsible_parties = []
        for i in value:
            self.append_to_responsible_parties(i)

    @responsible_parties.deleter
    def responsible_parties(self, value):
        """Deletes {class-name} responsible_parties property."""
        raise TypeError("Cannot delete {class-name} responsible_parties property.")

    def append_to_responsible_parties(self, item):
        """Appends an item to the managed {class-name} responsible_parties collection."""
        if not isinstance(item, ResponsibleParty):
            raise TypeError("item is of incorrect type.")
        self.__responsible_parties.append(item)

    def remove_from_responsible_parties(self, item):
        """Removes an item from the managed {class-name} responsible_parties collection."""
        if not isinstance(item, ResponsibleParty):
            raise TypeError("item is of incorrect type.")
        self.__responsible_parties.remove(item)



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
        append(d, 'funding_sources', self.__funding_sources, True, True, False)
        append(d, 'projects', self.__projects, True, False, False)
        append(d, 'rationale', self.__rationale, True, True, False)
        append(d, 'responsible_parties', self.__responsible_parties, True, False, False)
        return d





