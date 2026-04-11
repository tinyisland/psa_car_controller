# coding: utf-8

import pprint
import re  # noqa: F401

import six


class EnergiesExtensionElectricBattery(object):
    swagger_types = {
        'health': 'EnergiesExtensionElectricBatteryHealth',
        'load': 'EnergiesExtensionElectricBatteryLoad'
    }

    attribute_map = {
        'health': 'health',
        'load': 'load'
    }

    def __init__(self, health=None, load=None):  # noqa: E501

        self._health = None
        self._load = None
        self.discriminator = None

        if health is not None:
            self.health = health
        if load is not None:
            self.load = load

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

    @property
    def load(self):
        return self._load

    @load.setter
    def load(self, load):
        self._load = load

    def to_dict(self):
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
        if issubclass(EnergiesExtensionElectricBattery, dict):
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
        if not isinstance(other, EnergiesExtensionElectricBattery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
