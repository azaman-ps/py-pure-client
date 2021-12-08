# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.3, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_3 import models

class ObjectStoreRemoteCredentials(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'access_key_id': 'str',
        'remote': 'FixedReference',
        'secret_access_key': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'access_key_id': 'access_key_id',
        'remote': 'remote',
        'secret_access_key': 'secret_access_key'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        access_key_id=None,  # type: str
        remote=None,  # type: models.FixedReference
        secret_access_key=None,  # type: str
    ):
        """
        Keyword args:
            name (str): A name chosen by the user. Can be changed. Must be locally unique.
            id (str): A non-modifiable, globally unique ID chosen by the system.
            access_key_id (str): Access Key ID to be used when connecting to a remote object store.
            remote (FixedReference): Reference to the associated remote, which can either be a `target` or remote `array`. If it is an `array`, then the `resource-type` field will not be populated.
            secret_access_key (str): Secret Access Key to be used when connecting to a remote object store.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if access_key_id is not None:
            self.access_key_id = access_key_id
        if remote is not None:
            self.remote = remote
        if secret_access_key is not None:
            self.secret_access_key = secret_access_key

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ObjectStoreRemoteCredentials`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            return None
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
        if issubclass(ObjectStoreRemoteCredentials, dict):
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
        if not isinstance(other, ObjectStoreRemoteCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
