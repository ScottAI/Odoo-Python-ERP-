# -*- coding: utf-8 -*-
from odoo import http

# class Bm-advanced(http.Controller):
#     @http.route('/bm-advanced/bm-advanced/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bm-advanced/bm-advanced/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bm-advanced.listing', {
#             'root': '/bm-advanced/bm-advanced',
#             'objects': http.request.env['bm-advanced.bm-advanced'].search([]),
#         })

#     @http.route('/bm-advanced/bm-advanced/objects/<model("bm-advanced.bm-advanced"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bm-advanced.object', {
#             'object': obj
#         })