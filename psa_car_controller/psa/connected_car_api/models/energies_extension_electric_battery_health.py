# coding: utf-8

import pprint
import re  # noqa: F401

import six


class EnergiesExtensionElectricBatteryHealth(object):
    swagger_types = {
        'created_at': 'datetime',
        'capacity': 'float',
        'resistance': 'float'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'capacity': 'capacity',
        'resistance': 'resistance'
    }

    def __init__(self, created_at=None, capacity=None, resistance=None):  # noqa: E501

        self._created_at = None
        self._capacity = None
        self._resistance = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if capacity is not None:
            self.capacity = capacity
        if resistance is not None:
            self.resistance = resistance

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):

        self._created_at = created_at

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def resistance(self):
        return self._resistance

    @resistance.setter
    def resistance(self, resistance):
        self._resistance = resistance

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
        if issubclass(EnergiesExtensionElectricBatteryHealth, dict):
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
        if not isinstance(other, EnergiesExtensionElectricBatteryHealth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
