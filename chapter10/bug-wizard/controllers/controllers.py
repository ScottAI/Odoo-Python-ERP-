# -*- coding: utf-8 -*-
from odoo import http

# class Bug-wizard(http.Controller):
#     @http.route('/bug-wizard/bug-wizard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bug-wizard/bug-wizard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bug-wizard.listing', {
#             'root': '/bug-wizard/bug-wizard',
#             'objects': http.request.env['bug-wizard.bug-wizard'].search([]),
#         })

#     @http.route('/bug-wizard/bug-wizard/objects/<model("bug-wizard.bug-wizard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bug-wizard.object', {
#             'object': obj
#         })