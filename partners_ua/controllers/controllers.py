# -*- coding: utf-8 -*-
# from odoo import http


# class PartnersUa(http.Controller):
#     @http.route('/partners_ua/partners_ua', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partners_ua/partners_ua/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partners_ua.listing', {
#             'root': '/partners_ua/partners_ua',
#             'objects': http.request.env['partners_ua.partners_ua'].search([]),
#         })

#     @http.route('/partners_ua/partners_ua/objects/<model("partners_ua.partners_ua"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partners_ua.object', {
#             'object': obj
#         })
