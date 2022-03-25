from odoo import models, fields


class Teachers(models.Model):
    _name = 'academy.teachers'
    _description = 'Teachers'

    name = fields.Char()
    biography = fields.Html()
    course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")

