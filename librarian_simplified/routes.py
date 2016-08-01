from streamline import TemplateRoute

from librarian.core.contrib.templates.renderer import template
from librarian.data.manager import Manager


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
            return self.manager.list(path, self.view)
        except self.manager.InvalidQuery:
            self.abort(404)
