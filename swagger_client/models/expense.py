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

class Expense(object):
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
        'pay_from_account': 'object',
        'payment_method': 'object',
        'pay_to_resource_type': 'object',
        'pay_to_resource_id': 'object',
        'lines': 'object',
        'memo': 'object',
        'reference': 'object',
        '_date': 'object',
        'batch': 'object',
        'total_amount': 'object'
    }

    attribute_map = {
        'id': 'id',
        'pay_from_account': 'payFromAccount',
        'payment_method': 'paymentMethod',
        'pay_to_resource_type': 'payToResourceType',
        'pay_to_resource_id': 'payToResourceId',
        'lines': 'lines',
        'memo': 'memo',
        'reference': 'reference',
        '_date': 'date',
        'batch': 'batch',
        'total_amount': 'totalAmount'
    }

    def __init__(self, id=None, pay_from_account=None, payment_method=None, pay_to_resource_type=None, pay_to_resource_id=None, lines=None, memo=None, reference=None, _date=None, batch=None, total_amount=None):  # noqa: E501
        """Expense - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._pay_from_account = None
        self._payment_method = None
        self._pay_to_resource_type = None
        self._pay_to_resource_id = None
        self._lines = None
        self._memo = None
        self._reference = None
        self.__date = None
        self._batch = None
        self._total_amount = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.pay_from_account = pay_from_account
        self.payment_method = payment_method
        if pay_to_resource_type is not None:
            self.pay_to_resource_type = pay_to_resource_type
        if pay_to_resource_id is not None:
            self.pay_to_resource_id = pay_to_resource_id
        self.lines = lines
        if memo is not None:
            self.memo = memo
        if reference is not None:
            self.reference = reference
        self._date = _date
        if batch is not None:
            self.batch = batch
        if total_amount is not None:
            self.total_amount = total_amount

    @property
    def id(self):
        """Gets the id of this Expense.  # noqa: E501


        :return: The id of this Expense.  # noqa: E501
        :rtype: MongoId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Expense.


        :param id: The id of this Expense.  # noqa: E501
        :type: MongoId
        """

        self._id = id

    @property
    def pay_from_account(self):
        """Gets the pay_from_account of this Expense.  # noqa: E501


        :return: The pay_from_account of this Expense.  # noqa: E501
        :rtype: object
        """
        return self._pay_from_account

    @pay_from_account.setter
    def pay_from_account(self, pay_from_account):
        """Sets the pay_from_account of this Expense.


        :param pay_from_account: The pay_from_account of this Expense.  # noqa: E501
        :type: object
        """
        if pay_from_account is None:
            raise ValueError("Invalid value for `pay_from_account`, must not be `None`")  # noqa: E501

        self._pay_from_account = pay_from_account

    @property
    def payment_method(self):
        """Gets the payment_method of this Expense.  # noqa: E501


        :return: The payment_method of this Expense.  # noqa: E501
        :rtype: object
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this Expense.


        :param payment_method: The payment_method of this Expense.  # noqa: E501
        :type: object
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501

        self._payment_method = payment_method

    @property
    def pay_to_resource_type(self):
        """Gets the pay_to_resource_type of this Expense.  # noqa: E501


        :return: The pay_to_resource_type of this Expense.  # noqa: E501
        :rtype: object
        """
        return self._pay_to_resource_type

    @pay_to_resource_type.setter
    def pay_to_resource_type(self, pay_to_resource_type):
        """Sets the pay_to_resource_type of this Expense.


        :param pay_to_resource_type: The pay_to_resource_type of this Expense.  # noqa: E501
        :type: object
        """

        self._pay_to_resource_type = pay_to_resource_type

    @property
    def pay_to_resource_id(self):
        """Gets the pay_to_resource_id of this Expense.  # noqa: E501


        :return: The pay_to_resource_id of this Expense.  # noqa: E501
        :rtype: object
        """
        return self._pay_to_resource_id

    @pay_to_resource_id.setter
    def pay_to_resource_id(self, pay_to_resource_id):
        """Sets the pay_to_resource_id of this Expense.


        :param pay_to_resource_id: The pay_to_resource_id of this Expense.  # noqa: E501
        :type: object
        """

        self._pay_to_resource_id = pay_to_resource_id

    @property
    def lines(self):
        """Gets the lines of this Expense.  # noqa: E501


        :return: The lines of this Expense.  # noqa: E501
        :rtype: object
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this Expense.


        :param lines: The lines of this Expense.  # noqa: E501
        :type: object
        """
        if lines is None:
            raise ValueError("Invalid value for `lines`, must not be `None`")  # noqa: E501

        self._lines = lines

    @property
    def memo(self):
        """Gets the memo of this Expense.  # noqa: E501


        :return: The memo of this Expense.  # noqa: E501
        :rtype: object
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this Expense.


        :param memo: The memo of this Expense.  # noqa: E501
        :type: object
        """

        self._memo = memo

    @property
    def reference(self):
        """Gets the reference of this Expense.  # noqa: E501

        If not provided will be generated automatically by the server.  # noqa: E501

        :return: The reference of this Expense.  # noqa: E501
        :rtype: object
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Expense.

        If not provided will be generated automatically by the server.  # noqa: E501

        :param reference: The reference of this Expense.  # noqa: E501
        :type: object
        """

        self._reference = reference

    @property
    def _date(self):
        """Gets the _date of this Expense.  # noqa: E501

        Format: YYYY-MM-DD  # noqa: E501

        :return: The _date of this Expense.  # noqa: E501
        :rtype: object
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Expense.

        Format: YYYY-MM-DD  # noqa: E501

        :param _date: The _date of this Expense.  # noqa: E501
        :type: object
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def batch(self):
        """Gets the batch of this Expense.  # noqa: E501


        :return: The batch of this Expense.  # noqa: E501
        :rtype: object
        """
        return self._batch

    @batch.setter
    def batch(self, batch):
        """Sets the batch of this Expense.


        :param batch: The batch of this Expense.  # noqa: E501
        :type: object
        """

        self._batch = batch

    @property
    def total_amount(self):
        """Gets the total_amount of this Expense.  # noqa: E501

        Read Only. Calculated as sum of lines.amount.  # noqa: E501

        :return: The total_amount of this Expense.  # noqa: E501
        :rtype: object
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this Expense.

        Read Only. Calculated as sum of lines.amount.  # noqa: E501

        :param total_amount: The total_amount of this Expense.  # noqa: E501
        :type: object
        """

        self._total_amount = total_amount

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
        if issubclass(Expense, dict):
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
        if not isinstance(other, Expense):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
