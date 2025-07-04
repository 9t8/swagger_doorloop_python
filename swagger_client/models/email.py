# coding: utf-8

"""
    DoorLoop API Reference

    It does some pretty cool stuff and gives you complete access to DoorLoop's data  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@doorloop.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Email(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'object',
        'address': 'object'
    }

    attribute_map = {
        'type': 'type',
        'address': 'address'
    }

    def __init__(self, type=None, address=None):  # noqa: E501
        """Email - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._address = None
        self.discriminator = None
        self.type = type
        self.address = address

    @property
    def type(self):
        """Gets the type of this Email.  # noqa: E501


        :return: The type of this Email.  # noqa: E501
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Email.


        :param type: The type of this Email.  # noqa: E501
        :type: object
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def address(self):
        """Gets the address of this Email.  # noqa: E501


        :return: The address of this Email.  # noqa: E501
        :rtype: object
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Email.


        :param address: The address of this Email.  # noqa: E501
        :type: object
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

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
        if issubclass(Email, dict):
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
        if not isinstance(other, Email):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
