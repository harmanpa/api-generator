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


class PartStudiosCreatePartStudioResponse200(object):
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
        'angle_units': 'str',
        'name': 'str',
        'thumbnail_info': 'object',
        'length_units': 'str',
        'element_type': 'str',
        'type': 'str',
        'id': 'str',
        'thumbnails': 'object'
    }

    attribute_map = {
        'angle_units': 'angleUnits',
        'name': 'name',
        'thumbnail_info': 'thumbnailInfo',
        'length_units': 'lengthUnits',
        'element_type': 'elementType',
        'type': 'type',
        'id': 'id',
        'thumbnails': 'thumbnails'
    }

    def __init__(self, angle_units=None, name=None, thumbnail_info=None, length_units=None, element_type=None, type=None, id=None, thumbnails=None):  # noqa: E501
        """PartStudiosCreatePartStudioResponse200 - a model defined in Swagger"""  # noqa: E501

        self._angle_units = None
        self._name = None
        self._thumbnail_info = None
        self._length_units = None
        self._element_type = None
        self._type = None
        self._id = None
        self._thumbnails = None
        self.discriminator = None

        if angle_units is not None:
            self.angle_units = angle_units
        if name is not None:
            self.name = name
        if thumbnail_info is not None:
            self.thumbnail_info = thumbnail_info
        if length_units is not None:
            self.length_units = length_units
        if element_type is not None:
            self.element_type = element_type
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if thumbnails is not None:
            self.thumbnails = thumbnails

    @property
    def angle_units(self):
        """Gets the angle_units of this PartStudiosCreatePartStudioResponse200.  # noqa: E501

        Angle units, for Part Studio elements only  # noqa: E501

        :return: The angle_units of this PartStudiosCreatePartStudioResponse200.  # noqa: E501
        :rtype: str
        """
        return self._angle_units

    @angle_units.setter
    def angle_units(self, angle_units):
        """Sets the angle_units of this PartStudiosCreatePartStudioResponse200.

        Angle units, for Part Studio elements only  # noqa: E501

        :param angle_units: The angle_units of this PartStudiosCreatePartStudioResponse200.  # noqa: E501
        :type: str
        """

        self._angle_units = angle_units

    @property
    def name(self):
        """Gets the name of this PartStudiosCreatePartStudioResponse200.  # noqa: E501

        Element name  # noqa: E501

        :return: The name of this PartStudiosCreatePartStudioResponse200.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PartStudiosCreatePartStudioResponse200.

        Element name  # noqa: E501

        :param name: The name of this PartStudiosCreatePartStudioResponse200.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def thumbnail_info(self):
        """Gets the thumbnail_info of this PartStudiosCreatePartStudioResponse200.  # noqa: E501

        Thumbnail information  # noqa: E501

        :return: The thumbnail_info of this PartStudiosCreatePartStudioResponse200.  # noqa: E501
        :rtype: object
        """
        return self._thumbnail_info

    @thumbnail_info.setter
    def thumbnail_info(self, thumbnail_info):
        """Sets the thumbnail_info of this PartStudiosCreatePartStudioResponse200.

        Thumbnail information  # noqa: E501

        :param thumbnail_info: The thumbnail_info of this PartStudiosCreatePartStudioResponse200.  # noqa: E501
        :type: object
        """

        self._thumbnail_info = thumbnail_info

    @property
    def length_units(self):
        """Gets the length_units of this PartStudiosCreatePartStudioResponse200.  # noqa: E501

        Length units, for Part Studio elements only  # noqa: E501

        :return: The length_units of this PartStudiosCreatePartStudioResponse200.  # noqa: E501
        :rtype: str
        """
        return self._length_units

    @length_units.setter
    def length_units(self, length_units):
        """Sets the length_units of this PartStudiosCreatePartStudioResponse200.

        Length units, for Part Studio elements only  # noqa: E501

        :param length_units: The length_units of this PartStudiosCreatePartStudioResponse200.  # noqa: E501
        :type: str
        """

        self._length_units = length_units

    @property
    def element_type(self):
        """Gets the element_type of this PartStudiosCreatePartStudioResponse200.  # noqa: E501

        Element type (for example, \"PARTSTUDIO\")  # noqa: E501

        :return: The element_type of this PartStudiosCreatePartStudioResponse200.  # noqa: E501
        :rtype: str
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this PartStudiosCreatePartStudioResponse200.

        Element type (for example, \"PARTSTUDIO\")  # noqa: E501

        :param element_type: The element_type of this PartStudiosCreatePartStudioResponse200.  # noqa: E501
        :type: str
        """

        self._element_type = element_type

    @property
    def type(self):
        """Gets the type of this PartStudiosCreatePartStudioResponse200.  # noqa: E501

        Onshape internal use  # noqa: E501

        :return: The type of this PartStudiosCreatePartStudioResponse200.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PartStudiosCreatePartStudioResponse200.

        Onshape internal use  # noqa: E501

        :param type: The type of this PartStudiosCreatePartStudioResponse200.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this PartStudiosCreatePartStudioResponse200.  # noqa: E501

        Element ID  # noqa: E501

        :return: The id of this PartStudiosCreatePartStudioResponse200.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PartStudiosCreatePartStudioResponse200.

        Element ID  # noqa: E501

        :param id: The id of this PartStudiosCreatePartStudioResponse200.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def thumbnails(self):
        """Gets the thumbnails of this PartStudiosCreatePartStudioResponse200.  # noqa: E501

        Onshape internal use  # noqa: E501

        :return: The thumbnails of this PartStudiosCreatePartStudioResponse200.  # noqa: E501
        :rtype: object
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        """Sets the thumbnails of this PartStudiosCreatePartStudioResponse200.

        Onshape internal use  # noqa: E501

        :param thumbnails: The thumbnails of this PartStudiosCreatePartStudioResponse200.  # noqa: E501
        :type: object
        """

        self._thumbnails = thumbnails

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
        if not isinstance(other, PartStudiosCreatePartStudioResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
