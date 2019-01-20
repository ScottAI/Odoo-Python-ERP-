from odoo import http
from odoo.addons.bug_website.controllers.main import Main


class MainExtended(Main):
    @http.route()
    def hello(self, name=None, **kwargs):
        response = super(MainExtended, self).hello()
        response.qcontext['name'] = name
        return response