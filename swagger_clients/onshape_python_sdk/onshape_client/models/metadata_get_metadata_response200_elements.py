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

from onshape_client.models.metadata_get_metadata_response200_elements_items import MetadataGetMetadataResponse200ElementsItems  # noqa: F401,E501


class MetadataGetMetadataResponse200Elements(object):
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
        'href': 'str',
        'items': 'list[MetadataGetMetadataResponse200ElementsItems]',
        'prev': 'str',
        'next': 'str'
    }

    attribute_map = {
        'href': 'href',
        'items': 'items',
        'prev': 'prev',
        'next': 'next'
    }

    def __init__(self, href=None, items=None, prev=None, next=None):  # noqa: E501
        """MetadataGetMetadataResponse200Elements - a model defined in Swagger"""  # noqa: E501

        self._href = None
        self._items = None
        self._prev = None
        self._next = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if items is not None:
            self.items = items
        if prev is not None:
            self.prev = prev
        if next is not None:
            self.next = next

    @property
    def href(self):
        """Gets the href of this MetadataGetMetadataResponse200Elements.  # noqa: E501

        URL of current page of the response  # noqa: E501

        :return: The href of this MetadataGetMetadataResponse200Elements.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this MetadataGetMetadataResponse200Elements.

        URL of current page of the response  # noqa: E501

        :param href: The href of this MetadataGetMetadataResponse200Elements.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def items(self):
        """Gets the items of this MetadataGetMetadataResponse200Elements.  # noqa: E501

        Collection of element metadata objects  # noqa: E501

        :return: The items of this MetadataGetMetadataResponse200Elements.  # noqa: E501
        :rtype: list[MetadataGetMetadataResponse200ElementsItems]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this MetadataGetMetadataResponse200Elements.

        Collection of element metadata objects  # noqa: E501

        :param items: The items of this MetadataGetMetadataResponse200Elements.  # noqa: E501
        :type: list[MetadataGetMetadataResponse200ElementsItems]
        """

        self._items = items

    @property
    def prev(self):
        """Gets the prev of this MetadataGetMetadataResponse200Elements.  # noqa: E501

        URL of the previous page of the collection, can be null  # noqa: E501

        :return: The prev of this MetadataGetMetadataResponse200Elements.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this MetadataGetMetadataResponse200Elements.

        URL of the previous page of the collection, can be null  # noqa: E501

        :param prev: The prev of this MetadataGetMetadataResponse200Elements.  # noqa: E501
        :type: str
        """

        self._prev = prev

    @property
    def next(self):
        """Gets the next of this MetadataGetMetadataResponse200Elements.  # noqa: E501

        URL of the next page of the collection, can be null  # noqa: E501

        :return: The next of this MetadataGetMetadataResponse200Elements.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this MetadataGetMetadataResponse200Elements.

        URL of the next page of the collection, can be null  # noqa: E501

        :param next: The next of this MetadataGetMetadataResponse200Elements.  # noqa: E501
        :type: str
        """

        self._next = next

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
        if not isinstance(other, MetadataGetMetadataResponse200Elements):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
