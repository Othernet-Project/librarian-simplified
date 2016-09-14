"""
Copyright 2014-2015, Outernet Inc.
Some rights reserved.

This software is free software licensed under the terms of GPLv3. See COPYING
file that comes with the source code, or http://www.gnu.org/licenses/gpl.txt.
"""

from bottle_utils.i18n import lazy_gettext as _

from librarian.core.exts import ext_container as exts
from librarian.presentation.dashboard.dashboard import DashboardPlugin

from .forms import SimplifiedForm


class SimplifiedDashboardPlugin(DashboardPlugin):
    # Translators, used as dashboard section title
    heading = _('Home Content Editor')
    name = 'simplified'

    def get_template(self):
        return '{}/dashboard.tpl'.format(self.name)

    def get_context(self):
        content = exts.config.get('simplified.content', '')
        form = SimplifiedForm({'content': content})
        return dict(form=form)
