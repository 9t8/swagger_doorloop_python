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

class LeaseTransactionLine(object):
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
        'id': 'MongoId',
        'amount': 'object',
        'account': 'object',
        'memo': 'object',
        'balance': 'object'
    }

    attribute_map = {
        'id': 'id',
        'amount': 'amount',
        'account': 'account',
        'memo': 'memo',
        'balance': 'balance'
    }

    def __init__(self, id=None, amount=None, account=None, memo=None, balance=None):  # noqa: E501
        """LeaseTransactionLine - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._amount = None
        self._account = None
        self._memo = None
        self._balance = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.amount = amount
        self.account = account
        if memo is not None:
            self.memo = memo
        if balance is not None:
            self.balance = balance

    @property
    def id(self):
        """Gets the id of this LeaseTransactionLine.  # noqa: E501


        :return: The id of this LeaseTransactionLine.  # noqa: E501
        :rtype: MongoId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LeaseTransactionLine.


        :param id: The id of this LeaseTransactionLine.  # noqa: E501
        :type: MongoId
        """

        self._id = id

    @property
    def amount(self):
        """Gets the amount of this LeaseTransactionLine.  # noqa: E501


        :return: The amount of this LeaseTransactionLine.  # noqa: E501
        :rtype: object
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this LeaseTransactionLine.


        :param amount: The amount of this LeaseTransactionLine.  # noqa: E501
        :type: object
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def account(self):
        """Gets the account of this LeaseTransactionLine.  # noqa: E501

        References the Account Id for this line.  # noqa: E501

        :return: The account of this LeaseTransactionLine.  # noqa: E501
        :rtype: object
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this LeaseTransactionLine.

        References the Account Id for this line.  # noqa: E501

        :param account: The account of this LeaseTransactionLine.  # noqa: E501
        :type: object
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account

    @property
    def memo(self):
        """Gets the memo of this LeaseTransactionLine.  # noqa: E501


        :return: The memo of this LeaseTransactionLine.  # noqa: E501
        :rtype: object
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this LeaseTransactionLine.


        :param memo: The memo of this LeaseTransactionLine.  # noqa: E501
        :type: object
        """

        self._memo = memo

    @property
    def balance(self):
        """Gets the balance of this LeaseTransactionLine.  # noqa: E501

        Read Only.  # noqa: E501

        :return: The balance of this LeaseTransactionLine.  # noqa: E501
        :rtype: object
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this LeaseTransactionLine.

        Read Only.  # noqa: E501

        :param balance: The balance of this LeaseTransactionLine.  # noqa: E501
        :type: object
        """

        self._balance = balance

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
        if issubclass(LeaseTransactionLine, dict):
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
        if not isinstance(other, LeaseTransactionLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
