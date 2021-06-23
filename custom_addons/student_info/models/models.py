# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class student_info(models.Model):
#     _name = 'student_info.student_info'
#     _description = 'student_info.student_info'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
