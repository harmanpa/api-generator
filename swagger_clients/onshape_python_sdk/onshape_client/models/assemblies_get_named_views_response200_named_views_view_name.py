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


class AssembliesGetNamedViewsResponse200NamedViewsViewName(object):
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
        'camera_viewport': 'list[float]',
        'view_matrix': 'list[float]',
        'is_perspective': 'bool',
        'angle': 'float'
    }

    attribute_map = {
        'camera_viewport': 'cameraViewport',
        'view_matrix': 'viewMatrix',
        'is_perspective': 'isPerspective',
        'angle': 'angle'
    }

    def __init__(self, camera_viewport=None, view_matrix=None, is_perspective=None, angle=None):  # noqa: E501
        """AssembliesGetNamedViewsResponse200NamedViewsViewName - a model defined in Swagger"""  # noqa: E501

        self._camera_viewport = None
        self._view_matrix = None
        self._is_perspective = None
        self._angle = None
        self.discriminator = None

        if camera_viewport is not None:
            self.camera_viewport = camera_viewport
        if view_matrix is not None:
            self.view_matrix = view_matrix
        if is_perspective is not None:
            self.is_perspective = is_perspective
        if angle is not None:
            self.angle = angle

    @property
    def camera_viewport(self):
        """Gets the camera_viewport of this AssembliesGetNamedViewsResponse200NamedViewsViewName.  # noqa: E501

        the viewport used by the camera for this view  # noqa: E501

        :return: The camera_viewport of this AssembliesGetNamedViewsResponse200NamedViewsViewName.  # noqa: E501
        :rtype: list[float]
        """
        return self._camera_viewport

    @camera_viewport.setter
    def camera_viewport(self, camera_viewport):
        """Sets the camera_viewport of this AssembliesGetNamedViewsResponse200NamedViewsViewName.

        the viewport used by the camera for this view  # noqa: E501

        :param camera_viewport: The camera_viewport of this AssembliesGetNamedViewsResponse200NamedViewsViewName.  # noqa: E501
        :type: list[float]
        """

        self._camera_viewport = camera_viewport

    @property
    def view_matrix(self):
        """Gets the view_matrix of this AssembliesGetNamedViewsResponse200NamedViewsViewName.  # noqa: E501

        the view matrix  # noqa: E501

        :return: The view_matrix of this AssembliesGetNamedViewsResponse200NamedViewsViewName.  # noqa: E501
        :rtype: list[float]
        """
        return self._view_matrix

    @view_matrix.setter
    def view_matrix(self, view_matrix):
        """Sets the view_matrix of this AssembliesGetNamedViewsResponse200NamedViewsViewName.

        the view matrix  # noqa: E501

        :param view_matrix: The view_matrix of this AssembliesGetNamedViewsResponse200NamedViewsViewName.  # noqa: E501
        :type: list[float]
        """

        self._view_matrix = view_matrix

    @property
    def is_perspective(self):
        """Gets the is_perspective of this AssembliesGetNamedViewsResponse200NamedViewsViewName.  # noqa: E501

        true if this is a perspective projection  # noqa: E501

        :return: The is_perspective of this AssembliesGetNamedViewsResponse200NamedViewsViewName.  # noqa: E501
        :rtype: bool
        """
        return self._is_perspective

    @is_perspective.setter
    def is_perspective(self, is_perspective):
        """Sets the is_perspective of this AssembliesGetNamedViewsResponse200NamedViewsViewName.

        true if this is a perspective projection  # noqa: E501

        :param is_perspective: The is_perspective of this AssembliesGetNamedViewsResponse200NamedViewsViewName.  # noqa: E501
        :type: bool
        """

        self._is_perspective = is_perspective

    @property
    def angle(self):
        """Gets the angle of this AssembliesGetNamedViewsResponse200NamedViewsViewName.  # noqa: E501

        the angle used for the perspective projection if applicable  # noqa: E501

        :return: The angle of this AssembliesGetNamedViewsResponse200NamedViewsViewName.  # noqa: E501
        :rtype: float
        """
        return self._angle

    @angle.setter
    def angle(self, angle):
        """Sets the angle of this AssembliesGetNamedViewsResponse200NamedViewsViewName.

        the angle used for the perspective projection if applicable  # noqa: E501

        :param angle: The angle of this AssembliesGetNamedViewsResponse200NamedViewsViewName.  # noqa: E501
        :type: float
        """

        self._angle = angle

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
        if not isinstance(other, AssembliesGetNamedViewsResponse200NamedViewsViewName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
