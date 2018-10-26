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


class PartStudiosGetBodyDetailsResponse200Surface(object):
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
        'origin': 'list[float]',
        'type': 'str',
        'normal': 'list[float]'
    }

    attribute_map = {
        'origin': 'origin',
        'type': 'type',
        'normal': 'normal'
    }

    def __init__(self, origin=None, type=None, normal=None):  # noqa: E501
        """PartStudiosGetBodyDetailsResponse200Surface - a model defined in Swagger"""  # noqa: E501

        self._origin = None
        self._type = None
        self._normal = None
        self.discriminator = None

        if origin is not None:
            self.origin = origin
        if type is not None:
            self.type = type
        if normal is not None:
            self.normal = normal

    @property
    def origin(self):
        """Gets the origin of this PartStudiosGetBodyDetailsResponse200Surface.  # noqa: E501

        Surface origin  # noqa: E501

        :return: The origin of this PartStudiosGetBodyDetailsResponse200Surface.  # noqa: E501
        :rtype: list[float]
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this PartStudiosGetBodyDetailsResponse200Surface.

        Surface origin  # noqa: E501

        :param origin: The origin of this PartStudiosGetBodyDetailsResponse200Surface.  # noqa: E501
        :type: list[float]
        """

        self._origin = origin

    @property
    def type(self):
        """Gets the type of this PartStudiosGetBodyDetailsResponse200Surface.  # noqa: E501

        Surface type - this can be one of \"cone\",     \"cylinder\", \"plane\", \"sphere\", \"revolved\", \"extruded\", \"torus\", \"other\"  # noqa: E501

        :return: The type of this PartStudiosGetBodyDetailsResponse200Surface.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PartStudiosGetBodyDetailsResponse200Surface.

        Surface type - this can be one of \"cone\",     \"cylinder\", \"plane\", \"sphere\", \"revolved\", \"extruded\", \"torus\", \"other\"  # noqa: E501

        :param type: The type of this PartStudiosGetBodyDetailsResponse200Surface.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def normal(self):
        """Gets the normal of this PartStudiosGetBodyDetailsResponse200Surface.  # noqa: E501

        Normalized surface info  # noqa: E501

        :return: The normal of this PartStudiosGetBodyDetailsResponse200Surface.  # noqa: E501
        :rtype: list[float]
        """
        return self._normal

    @normal.setter
    def normal(self, normal):
        """Sets the normal of this PartStudiosGetBodyDetailsResponse200Surface.

        Normalized surface info  # noqa: E501

        :param normal: The normal of this PartStudiosGetBodyDetailsResponse200Surface.  # noqa: E501
        :type: list[float]
        """

        self._normal = normal

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
        if not isinstance(other, PartStudiosGetBodyDetailsResponse200Surface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
