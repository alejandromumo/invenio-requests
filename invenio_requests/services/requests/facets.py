# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 CERN.
# Copyright (C) 2023 Graz University of Technology.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Facet definitions."""

from invenio_i18n import gettext as _
from invenio_records_resources.services.records.facets import TermsFacet

type = TermsFacet(
    field="type",
    label=_("Type"),
    value_labels={
        "community-submission": _("Draft review"),
        "community-inclusion": _("Community inclusion"),
        "community-invitation": _("Member invitation"),
    },
)

status = TermsFacet(
    field="status",
    label=_("Status"),
    value_labels={
        "submitted": _("Submitted"),
        "expired": _("Expired"),
        "accepted": _("Accepted"),
        "declined": _("Declined"),
        "cancelled": _("Cancelled"),
    },
)
