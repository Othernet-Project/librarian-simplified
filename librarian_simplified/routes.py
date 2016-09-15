"""
Copyright 2014-2015, Outernet Inc.
Some rights reserved.

This software is free software licensed under the terms of GPLv3. See COPYING
file that comes with the source code, or http://www.gnu.org/licenses/gpl.txt.
"""

from bottle_utils.i18n import i18n_url, lazy_gettext as _
from streamline import TemplateRoute, XHRPartialFormRoute

from librarian.core.contrib.templates.renderer import template
from librarian.core.exts import ext_container as exts
from librarian.data.manager import Manager

from .forms import SimplifiedForm


class SimplifiedView(TemplateRoute):
    name = 'simplified:view'
    path = '/simple/'
    template_name = 'simplified/main'
    template_func = template
    view = 'html'

    def __init__(self, *args, **kwargs):
        super(SimplifiedView, self).__init__(*args, **kwargs)
        self.manager = Manager()

    def get(self):
        path = self.manager.get_root()
        try:
            context = self.manager.list(path, self.view)
        except self.manager.InvalidQuery:
            self.abort(404)
        else:
            context.update(content=exts.config.get('simplified.content', ''),
                           placeholder=exts.config['simplified.placeholder'])
            return context


class SimplifiedEditor(XHRPartialFormRoute):
    name = 'simplified:editor'
    path = '/simple/edit/'
    template_func = template
    template_name = 'simplified/simplified'
    partial_template_name = 'simplified/_simplified'
    form_factory = SimplifiedForm

    def get_unbound_form(self):
        form_factory = self.get_form_factory()
        return form_factory({'content': exts.config['simplified.content']})

    def form_valid(self):
        content = self.form.processed_data['content']
        exts.setup.append({'simplified.content': content})
        return dict(message=_('Home content has been saved.'),
                    redirect_url=i18n_url('dashboard:main'))

    def form_invalid(self):
        return dict(message=None)
