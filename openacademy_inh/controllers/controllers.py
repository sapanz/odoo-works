# -*- coding: utf-8 -*-
# from odoo import http


# class OpenacademyInh(http.Controller):
#     @http.route('/openacademy_inh/openacademy_inh/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openacademy_inh/openacademy_inh/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openacademy_inh.listing', {
#             'root': '/openacademy_inh/openacademy_inh',
#             'objects': http.request.env['openacademy_inh.openacademy_inh'].search([]),
#         })

#     @http.route('/openacademy_inh/openacademy_inh/objects/<model("openacademy_inh.openacademy_inh"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacademy_inh.object', {
#             'object': obj
#         })
