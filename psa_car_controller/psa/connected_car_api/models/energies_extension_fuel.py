# coding: utf-8
import pprint
import re  # noqa: F401

import six


class EnergiesExtensionFuel(object):
    swagger_types = {
        'consumptions': 'EnergiesExtensionFuelConsumptions'
    }

    attribute_map = {
        'consumptions': 'consumptions'
    }

    def __init__(self, consumptions=None):  # noqa: E501
        """EnergyBattery - a model defined in Swagger"""  # noqa: E501

        self._consumptions = None
        self.discriminator = None

        if consumptions is not None:
            self.consumptions = consumptions

    @property
    def consumptions(self):
        return self._consumptions

    @consumptions.setter
    def consumptions(self, consumptions):
        self._consumptions = consumptions

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
        if issubclass(EnergiesExtensionFuel, dict):
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
        if not isinstance(other, EnergiesExtensionFuel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
