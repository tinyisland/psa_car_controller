# coding: utf-8


import pprint
import re  # noqa: F401

import six


class Engines(object):
    swagger_types = {
        'created_at': 'datetime',
        'extension': 'EnginesExtension',
        'type': 'str',
        'speed': 'float'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'extension': 'extension',
        'type': 'type',
        'speed': 'speed'
    }

    def __init__(self, created_at=None, extension=None, type=None, speed=None):  # noqa: E501
        """Engine - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._extension = None
        self._type = None
        self._speed = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if extension is not None:
            self.extension = extension
        if type is not None:
            self.type = type
        if speed is not None:
            self.speed = speed

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, extension):
        self._extension = extension

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed


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
        if issubclass(Engines, dict):
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
        if not isinstance(other, Engines):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
