# -*- coding: utf-8 -*-
# from odoo import http


# class CalenderTask(http.Controller):
#     @http.route('/calender_task/calender_task/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/calender_task/calender_task/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('calender_task.listing', {
#             'root': '/calender_task/calender_task',
#             'objects': http.request.env['calender_task.calender_task'].search([]),
#         })

#     @http.route('/calender_task/calender_task/objects/<model("calender_task.calender_task"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('calender_task.object', {
#             'object': obj
#         })
