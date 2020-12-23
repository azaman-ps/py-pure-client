# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_4 import models

class SoftwareInstallationSteps(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'checks': 'list[SoftwareInstallationStepsChecks]',
        'description': 'str',
        'details': 'str',
        'hop_version': 'str',
        'installation': 'Reference',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'checks': 'checks',
        'description': 'description',
        'details': 'details',
        'hop_version': 'hop_version',
        'installation': 'installation',
        'status': 'status'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        start_time=None,  # type: int
        end_time=None,  # type: int
        checks=None,  # type: List[models.SoftwareInstallationStepsChecks]
        description=None,  # type: str
        details=None,  # type: str
        hop_version=None,  # type: str
        installation=None,  # type: models.Reference
        status=None,  # type: str
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified.
            name (str): Name of the resource. The name cannot be modified.
            start_time (int): Start time in milliseconds since the UNIX epoch.
            end_time (int): End time in milliseconds since the UNIX epoch.
            checks (list[SoftwareInstallationStepsChecks]): A list of checks in this upgrade step.
            description (str): Detailed description of the step.
            details (str): Detailed result of the step used to diagnose step failures.
            hop_version (str): The version to which the current hop is upgrading.
            installation (Reference): Referenced `software-installation` to which the step belongs.
            status (str): Status of the step. Valid values are `running` and `finished`. A status of `running` indicates that the step has not finished. A status of `finished` indicates that the check has finished.
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if checks is not None:
            self.checks = checks
        if description is not None:
            self.description = description
        if details is not None:
            self.details = details
        if hop_version is not None:
            self.hop_version = hop_version
        if installation is not None:
            self.installation = installation
        if status is not None:
            self.status = status

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SoftwareInstallationSteps`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
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
        if issubclass(SoftwareInstallationSteps, dict):
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
        if not isinstance(other, SoftwareInstallationSteps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
