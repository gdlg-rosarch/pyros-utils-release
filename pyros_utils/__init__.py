# -*- coding: utf-8 -*-
from __future__ import absolute_import

from ._version import __version__

from .ros_utils import get_master, get_ros_home
from .rostest_nose import rostest_or_nose_main

__all__ = [
    'get_master',
    'get_ros_home',
]
