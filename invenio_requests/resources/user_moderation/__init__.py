# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 CERN.
#
# Invenio-Requests is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.
"""User Moderation resources module."""

from .config import UserModerationResourceConfig
from .resource import UserModerationResource

__all__ = (
    "UserModerationResource",
    "UserModerationResourceConfig",
)
