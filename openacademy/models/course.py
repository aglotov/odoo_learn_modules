# -*- coding: utf-8 -*-

from odoo import models, fields


class course(models.Model):
    _name = 'openacademy.course'
    _description = 'Courses of the OpenAcademy'

    title = fields.Char(string="Title", required=True, )
    description = fields.Text(string="Description")

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
