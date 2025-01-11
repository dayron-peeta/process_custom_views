# -*- coding: utf-8 -*-
# from odoo import http


# class ProcessCustomViews(http.Controller):
#     @http.route('/process_custom_views/process_custom_views', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/process_custom_views/process_custom_views/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('process_custom_views.listing', {
#             'root': '/process_custom_views/process_custom_views',
#             'objects': http.request.env['process_custom_views.process_custom_views'].search([]),
#         })

#     @http.route('/process_custom_views/process_custom_views/objects/<model("process_custom_views.process_custom_views"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('process_custom_views.object', {
#             'object': obj
#         })
