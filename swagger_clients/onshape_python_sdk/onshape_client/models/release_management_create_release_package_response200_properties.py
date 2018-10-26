# coding: utf-8

"""
    Onshape API

    Onshape API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: ekeller@onshape.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ReleaseManagementCreateReleasePackageResponse200Properties(object):
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
        'name': 'str',
        'value_type': 'str',
        'required': 'bool',
        'editable': 'bool',
        'value': 'str',
        'property_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value_type': 'valueType',
        'required': 'required',
        'editable': 'editable',
        'value': 'value',
        'property_id': 'propertyId'
    }

    def __init__(self, name=None, value_type=None, required=None, editable=None, value=None, property_id=None):  # noqa: E501
        """ReleaseManagementCreateReleasePackageResponse200Properties - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._value_type = None
        self._required = None
        self._editable = None
        self._value = None
        self._property_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value_type is not None:
            self.value_type = value_type
        if required is not None:
            self.required = required
        if editable is not None:
            self.editable = editable
        if value is not None:
            self.value = value
        if property_id is not None:
            self.property_id = property_id

    @property
    def name(self):
        """Gets the name of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501

        User friendly name of the property  # noqa: E501

        :return: The name of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReleaseManagementCreateReleasePackageResponse200Properties.

        User friendly name of the property  # noqa: E501

        :param name: The name of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value_type(self):
        """Gets the value_type of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501

        The value type of the property STRING BOOLEAN etc  # noqa: E501

        :return: The value_type of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this ReleaseManagementCreateReleasePackageResponse200Properties.

        The value type of the property STRING BOOLEAN etc  # noqa: E501

        :param value_type: The value_type of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501
        :type: str
        """

        self._value_type = value_type

    @property
    def required(self):
        """Gets the required of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501

        Whether the property is required.  # noqa: E501

        :return: The required of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this ReleaseManagementCreateReleasePackageResponse200Properties.

        Whether the property is required.  # noqa: E501

        :param required: The required of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def editable(self):
        """Gets the editable of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501

        Whether the property is editable  # noqa: E501

        :return: The editable of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this ReleaseManagementCreateReleasePackageResponse200Properties.

        Whether the property is editable  # noqa: E501

        :param editable: The editable of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501
        :type: bool
        """

        self._editable = editable

    @property
    def value(self):
        """Gets the value of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501

        The current value of the property  # noqa: E501

        :return: The value of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ReleaseManagementCreateReleasePackageResponse200Properties.

        The current value of the property  # noqa: E501

        :param value: The value of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def property_id(self):
        """Gets the property_id of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501

        ID of the property to be used when updating  # noqa: E501

        :return: The property_id of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501
        :rtype: str
        """
        return self._property_id

    @property_id.setter
    def property_id(self, property_id):
        """Sets the property_id of this ReleaseManagementCreateReleasePackageResponse200Properties.

        ID of the property to be used when updating  # noqa: E501

        :param property_id: The property_id of this ReleaseManagementCreateReleasePackageResponse200Properties.  # noqa: E501
        :type: str
        """

        self._property_id = property_id

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReleaseManagementCreateReleasePackageResponse200Properties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
