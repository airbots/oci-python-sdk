# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .volume_source_details import VolumeSourceDetails
from ...util import formatted_flat_dict


class VolumeSourceFromVolumeDetails(VolumeSourceDetails):

    def __init__(self):

        self.swagger_types = {
            'type': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id'
        }

        self._type = None
        self._id = None
        self._type = 'volume'

    @property
    def id(self):
        """
        Gets the id of this VolumeSourceFromVolumeDetails.
        The OCID of the volume.


        :return: The id of this VolumeSourceFromVolumeDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VolumeSourceFromVolumeDetails.
        The OCID of the volume.


        :param id: The id of this VolumeSourceFromVolumeDetails.
        :type: str
        """
        self._id = id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
