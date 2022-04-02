# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Courses of the OpenAcademy'

    title = fields.Char(string="Title", required=True, )
    description = fields.Text(string="Description")
    responsible_id = fields.Many2one(comodel_name="res.users", string="Responsible", required=False, )
    session_ids = fields.One2many(comodel_name="openacademy.session", string="Session", required=False,
                                  inverse_name="course_id")
    _sql_constraints = [
        ('title_uniq', 'unique (title)', _("Course title already exists !")),
        ('title_notequal_descr', 'check (title <> description)', _("Title and description should be different !")),
    ]

    @api.depends('title')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = rec.title

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {})
        default.setdefault('title', _("Copy of %s", self.title))
        return super(Course, self).copy(default=default)
