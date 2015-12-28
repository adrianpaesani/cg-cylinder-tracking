# -*- coding: utf-8 -*-
from openerp import http

# class Openacademy(http.Controller):
#     @http.route('/cg-cylinder-tracking/cg-cylinder-tracking/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cg-cylinder-tracking/cg-cylinder-tracking/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cg-cylinder-tracking.listing', {
#             'root': '/cg-cylinder-tracking/cg-cylinder-tracking',
#             'objects': http.request.env['cg-cylinder-tracking.cg-cylinder-tracking'].search([]),
#         })

#     @http.route('/cg-cylinder-tracking/cg-cylinder-tracking/objects/<model("cg-cylinder-tracking.cg-cylinder-tracking"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cg-cylinder-tracking.object', {
#             'object': obj
#         })
