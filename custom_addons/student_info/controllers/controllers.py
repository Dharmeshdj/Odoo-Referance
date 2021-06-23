# -*- coding: utf-8 -*-
# from odoo import http


# class StudentInfo(http.Controller):
#     @http.route('/student_info/student_info/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/student_info/student_info/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('student_info.listing', {
#             'root': '/student_info/student_info',
#             'objects': http.request.env['student_info.student_info'].search([]),
#         })

#     @http.route('/student_info/student_info/objects/<model("student_info.student_info"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('student_info.object', {
#             'object': obj
#         })
