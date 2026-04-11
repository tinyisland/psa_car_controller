# coding: utf-8


import pprint
import logging
import re  # noqa: F401

import six

logger = logging.getLogger(__name__)


class Energies(object):
    swagger_types = {
        'created_at': 'datetime',
        'type': 'str',
        'subtype': 'str',
        'extension': 'EnergiesExtension'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'type': 'type',
        'subtype': 'subType',
        'extension': 'extension'
    }

    def __init__(self, created_at=None, type=None, subtype=None, extension=None):  # noqa: E501
        self._created_at = None
        self._type = None
        self._subtype = None
        self._extension = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if type is not None:
            self.type = type
        if subtype is not None:
            self.subtype = subtype
        if extension is not None:
            self.extension = extension


    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        allowed_values = ["Fuel", "Electric"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def subtype(self):
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        self._subtype = subtype

    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, extension):
        self._extension = extension

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Energies, dict):
            for key, value in self.items():
                result[key] = value
                
        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Energies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
