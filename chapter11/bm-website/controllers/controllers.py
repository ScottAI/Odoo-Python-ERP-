# -*- coding: utf-8 -*-
from odoo import http

# class Bm-website(http.Controller):
#     @http.route('/bm-website/bm-website/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bm-website/bm-website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bm-website.listing', {
#             'root': '/bm-website/bm-website',
#             'objects': http.request.env['bm-website.bm-website'].search([]),
#         })

#     @http.route('/bm-website/bm-website/objects/<model("bm-website.bm-website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bm-website.object', {
#             'object': obj
#         })