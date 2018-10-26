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

from onshape_client.models.assemblies_get_named_views_response200_named_views_key_section_planes import AssembliesGetNamedViewsResponse200NamedViewsKeySectionPlanes  # noqa: F401,E501


class AssembliesGetNamedViewsResponse200NamedViewsKey(object):
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
        'angle': 'float',
        'perspective': 'bool',
        'section_planes': 'list[AssembliesGetNamedViewsResponse200NamedViewsKeySectionPlanes]'
    }

    attribute_map = {
        'camera_viewport': 'cameraViewport',
        'view_matrix': 'viewMatrix',
        'angle': 'angle',
        'perspective': 'perspective',
        'section_planes': 'sectionPlanes'
    }

    def __init__(self, camera_viewport=None, view_matrix=None, angle=None, perspective=None, section_planes=None):  # noqa: E501
        """AssembliesGetNamedViewsResponse200NamedViewsKey - a model defined in Swagger"""  # noqa: E501

        self._camera_viewport = None
        self._view_matrix = None
        self._angle = None
        self._perspective = None
        self._section_planes = None
        self.discriminator = None

        if camera_viewport is not None:
            self.camera_viewport = camera_viewport
        if view_matrix is not None:
            self.view_matrix = view_matrix
        if angle is not None:
            self.angle = angle
        if perspective is not None:
            self.perspective = perspective
        if section_planes is not None:
            self.section_planes = section_planes

    @property
    def camera_viewport(self):
        """Gets the camera_viewport of this AssembliesGetNamedViewsResponse200NamedViewsKey.  # noqa: E501

        The viewport of the camera of the view  # noqa: E501

        :return: The camera_viewport of this AssembliesGetNamedViewsResponse200NamedViewsKey.  # noqa: E501
        :rtype: list[float]
        """
        return self._camera_viewport

    @camera_viewport.setter
    def camera_viewport(self, camera_viewport):
        """Sets the camera_viewport of this AssembliesGetNamedViewsResponse200NamedViewsKey.

        The viewport of the camera of the view  # noqa: E501

        :param camera_viewport: The camera_viewport of this AssembliesGetNamedViewsResponse200NamedViewsKey.  # noqa: E501
        :type: list[float]
        """

        self._camera_viewport = camera_viewport

    @property
    def view_matrix(self):
        """Gets the view_matrix of this AssembliesGetNamedViewsResponse200NamedViewsKey.  # noqa: E501

        A 16-element array storing the view matrix of the view  # noqa: E501

        :return: The view_matrix of this AssembliesGetNamedViewsResponse200NamedViewsKey.  # noqa: E501
        :rtype: list[float]
        """
        return self._view_matrix

    @view_matrix.setter
    def view_matrix(self, view_matrix):
        """Sets the view_matrix of this AssembliesGetNamedViewsResponse200NamedViewsKey.

        A 16-element array storing the view matrix of the view  # noqa: E501

        :param view_matrix: The view_matrix of this AssembliesGetNamedViewsResponse200NamedViewsKey.  # noqa: E501
        :type: list[float]
        """

        self._view_matrix = view_matrix

    @property
    def angle(self):
        """Gets the angle of this AssembliesGetNamedViewsResponse200NamedViewsKey.  # noqa: E501

        The angle of the view  # noqa: E501

        :return: The angle of this AssembliesGetNamedViewsResponse200NamedViewsKey.  # noqa: E501
        :rtype: float
        """
        return self._angle

    @angle.setter
    def angle(self, angle):
        """Sets the angle of this AssembliesGetNamedViewsResponse200NamedViewsKey.

        The angle of the view  # noqa: E501

        :param angle: The angle of this AssembliesGetNamedViewsResponse200NamedViewsKey.  # noqa: E501
        :type: float
        """

        self._angle = angle

    @property
    def perspective(self):
        """Gets the perspective of this AssembliesGetNamedViewsResponse200NamedViewsKey.  # noqa: E501

        Whether or not the view is in perspective mode  # noqa: E501

        :return: The perspective of this AssembliesGetNamedViewsResponse200NamedViewsKey.  # noqa: E501
        :rtype: bool
        """
        return self._perspective

    @perspective.setter
    def perspective(self, perspective):
        """Sets the perspective of this AssembliesGetNamedViewsResponse200NamedViewsKey.

        Whether or not the view is in perspective mode  # noqa: E501

        :param perspective: The perspective of this AssembliesGetNamedViewsResponse200NamedViewsKey.  # noqa: E501
        :type: bool
        """

        self._perspective = perspective

    @property
    def section_planes(self):
        """Gets the section_planes of this AssembliesGetNamedViewsResponse200NamedViewsKey.  # noqa: E501

        An array of objects that represent the section planes in the view  # noqa: E501

        :return: The section_planes of this AssembliesGetNamedViewsResponse200NamedViewsKey.  # noqa: E501
        :rtype: list[AssembliesGetNamedViewsResponse200NamedViewsKeySectionPlanes]
        """
        return self._section_planes

    @section_planes.setter
    def section_planes(self, section_planes):
        """Sets the section_planes of this AssembliesGetNamedViewsResponse200NamedViewsKey.

        An array of objects that represent the section planes in the view  # noqa: E501

        :param section_planes: The section_planes of this AssembliesGetNamedViewsResponse200NamedViewsKey.  # noqa: E501
        :type: list[AssembliesGetNamedViewsResponse200NamedViewsKeySectionPlanes]
        """

        self._section_planes = section_planes

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
        if not isinstance(other, AssembliesGetNamedViewsResponse200NamedViewsKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
