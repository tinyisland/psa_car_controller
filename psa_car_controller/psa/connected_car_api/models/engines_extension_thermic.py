# coding: utf-8


import pprint
import re  # noqa: F401

import six


class EnginesExtensionThermic(object):
    swagger_types = {
        'air': 'Temperature',
        'coolant': 'TemperatureLevel',
        'oil': 'TemperatureLevel'
    }

    attribute_map = {
        'air': 'air',
        'coolant': 'coolant',
        'oil': 'oil'
    }

    def __init__(self, air=None, coolant=None, oil=None):  # noqa: E501

        self._air = None
        self._coolant = None
        self._oil = None
        self.discriminator = None

        if air is not None:
            self.air = air
        if coolant is not None:
            self.coolant = coolant
        if oil is not None:
            self.oil = oil

    @property
    def air(self):
        return self._air

    @air.setter
    def air(self, air):
        self._air = air

    @property
    def coolant(self):
        return self._coolant

    @coolant.setter
    def coolant(self, coolant):
        self._coolant = coolant

    @property
    def oil(self):
        return self._oil

    @oil.setter
    def oil(self, oil):
        self._oil = oil

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
        if issubclass(EnginesExtensionThermic, dict):
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
        if not isinstance(other, EnginesExtensionThermic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
