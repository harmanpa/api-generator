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


class AssembliesInsertTransformedInstancesBodyInstances(object):
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
        'part_id': 'str',
        'feature_id': 'str',
        'is_assembly': 'bool',
        'microversion_id': 'str',
        'version_id': 'str',
        'document_id': 'str',
        'configuration': 'str',
        'element_id': 'str',
        'is_whole_part_studio': 'bool'
    }

    attribute_map = {
        'part_id': 'partId',
        'feature_id': 'featureId',
        'is_assembly': 'isAssembly',
        'microversion_id': 'microversionId',
        'version_id': 'versionId',
        'document_id': 'documentId',
        'configuration': 'configuration',
        'element_id': 'elementId',
        'is_whole_part_studio': 'isWholePartStudio'
    }

    def __init__(self, part_id=None, feature_id=None, is_assembly=None, microversion_id=None, version_id=None, document_id=None, configuration=None, element_id=None, is_whole_part_studio=None):  # noqa: E501
        """AssembliesInsertTransformedInstancesBodyInstances - a model defined in Swagger"""  # noqa: E501

        self._part_id = None
        self._feature_id = None
        self._is_assembly = None
        self._microversion_id = None
        self._version_id = None
        self._document_id = None
        self._configuration = None
        self._element_id = None
        self._is_whole_part_studio = None
        self.discriminator = None

        if part_id is not None:
            self.part_id = part_id
        if feature_id is not None:
            self.feature_id = feature_id
        if is_assembly is not None:
            self.is_assembly = is_assembly
        if microversion_id is not None:
            self.microversion_id = microversion_id
        if version_id is not None:
            self.version_id = version_id
        if document_id is not None:
            self.document_id = document_id
        if configuration is not None:
            self.configuration = configuration
        if element_id is not None:
            self.element_id = element_id
        if is_whole_part_studio is not None:
            self.is_whole_part_studio = is_whole_part_studio

    @property
    def part_id(self):
        """Gets the part_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501

        Part ID of instance, if it's a part or surface.           Must be left blank if featureId is set.  # noqa: E501

        :return: The part_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :rtype: str
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """Sets the part_id of this AssembliesInsertTransformedInstancesBodyInstances.

        Part ID of instance, if it's a part or surface.           Must be left blank if featureId is set.  # noqa: E501

        :param part_id: The part_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :type: str
        """

        self._part_id = part_id

    @property
    def feature_id(self):
        """Gets the feature_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501

        Feature ID of instance, if it's a feature.           Currently, only sketch features are valid. Must be left blank if partId is set.  # noqa: E501

        :return: The feature_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :rtype: str
        """
        return self._feature_id

    @feature_id.setter
    def feature_id(self, feature_id):
        """Sets the feature_id of this AssembliesInsertTransformedInstancesBodyInstances.

        Feature ID of instance, if it's a feature.           Currently, only sketch features are valid. Must be left blank if partId is set.  # noqa: E501

        :param feature_id: The feature_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :type: str
        """

        self._feature_id = feature_id

    @property
    def is_assembly(self):
        """Gets the is_assembly of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501

        Whether the instance is the assembly           specified by the element ID.  # noqa: E501

        :return: The is_assembly of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :rtype: bool
        """
        return self._is_assembly

    @is_assembly.setter
    def is_assembly(self, is_assembly):
        """Sets the is_assembly of this AssembliesInsertTransformedInstancesBodyInstances.

        Whether the instance is the assembly           specified by the element ID.  # noqa: E501

        :param is_assembly: The is_assembly of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :type: bool
        """

        self._is_assembly = is_assembly

    @property
    def microversion_id(self):
        """Gets the microversion_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501

        Source document microversion ID in which           to resolve elementId and partId. This must be left empty if a versionId is specified.  # noqa: E501

        :return: The microversion_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :rtype: str
        """
        return self._microversion_id

    @microversion_id.setter
    def microversion_id(self, microversion_id):
        """Sets the microversion_id of this AssembliesInsertTransformedInstancesBodyInstances.

        Source document microversion ID in which           to resolve elementId and partId. This must be left empty if a versionId is specified.  # noqa: E501

        :param microversion_id: The microversion_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :type: str
        """

        self._microversion_id = microversion_id

    @property
    def version_id(self):
        """Gets the version_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501

        Document version ID in which to resolve           elementId and partId.  # noqa: E501

        :return: The version_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this AssembliesInsertTransformedInstancesBodyInstances.

        Document version ID in which to resolve           elementId and partId.  # noqa: E501

        :param version_id: The version_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def document_id(self):
        """Gets the document_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501

        Source document ID for the           instance. If this differs from the same document as in the path, you must specify a versionId for the           instance in the source document.  # noqa: E501

        :return: The document_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this AssembliesInsertTransformedInstancesBodyInstances.

        Source document ID for the           instance. If this differs from the same document as in the path, you must specify a versionId for the           instance in the source document.  # noqa: E501

        :param document_id: The document_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def configuration(self):
        """Gets the configuration of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501

        Configuration of the source element,           valid only if the referenced element is a Part Studio.  # noqa: E501

        :return: The configuration of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this AssembliesInsertTransformedInstancesBodyInstances.

        Configuration of the source element,           valid only if the referenced element is a Part Studio.  # noqa: E501

        :param configuration: The configuration of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def element_id(self):
        """Gets the element_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501

        Source element ID for the instance.  # noqa: E501

        :return: The element_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this AssembliesInsertTransformedInstancesBodyInstances.

        Source element ID for the instance.  # noqa: E501

        :param element_id: The element_id of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def is_whole_part_studio(self):
        """Gets the is_whole_part_studio of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501

        Whether the instance is the           entire part studio specified by the element ID.  # noqa: E501

        :return: The is_whole_part_studio of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :rtype: bool
        """
        return self._is_whole_part_studio

    @is_whole_part_studio.setter
    def is_whole_part_studio(self, is_whole_part_studio):
        """Sets the is_whole_part_studio of this AssembliesInsertTransformedInstancesBodyInstances.

        Whether the instance is the           entire part studio specified by the element ID.  # noqa: E501

        :param is_whole_part_studio: The is_whole_part_studio of this AssembliesInsertTransformedInstancesBodyInstances.  # noqa: E501
        :type: bool
        """

        self._is_whole_part_studio = is_whole_part_studio

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
        if not isinstance(other, AssembliesInsertTransformedInstancesBodyInstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
