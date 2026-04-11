# coding: utf-8

import pprint
import re  # noqa: F401

import six


class EnergiesExtensionElectricBatteryLoad(object):
    swagger_types = {
        'created_at': 'datetime',
        'residual': 'int'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'residual': 'residual'
    }

    def __init__(self, created_at=None, residual=None):  # noqa: E501

        self._created_at = None
        self._residual = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if residual is not None:
            self.residual = residual

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):

        self._created_at = created_at

    @property
    def residual(self):
        return self._residual

    @residual.setter
    def residual(self, residual):

        self._residual = residual

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
        if issubclass(EnergiesExtensionElectricBatteryLoad, dict):
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
        if not isinstance(other, EnergiesExtensionElectricBatteryLoad):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
