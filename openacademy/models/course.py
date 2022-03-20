# -*- coding: utf-8 -*-

from odoo import models, fields


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Courses of the OpenAcademy'

    title = fields.Char(string="Title", required=True, )
    description = fields.Text(string="Description")
    responsible_id = fields.Many2one(comodel_name="res.users", string="Responsible", required=False, )
    session_id = fields.Many2one(comodel_name="openacademy.session", string="Session", required=False, )
    _sql_constraints = [
        ('title_uniq', 'unique (title)', "Course title already exists !"),
        ('title_notequal_descr', 'check (title <> description)', "Title and description should be different !"),
    ]

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
