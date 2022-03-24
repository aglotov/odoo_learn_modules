from odoo import models, fields


class Teachers(models.Model):
    _name = 'academy.teachers'
    _description = 'Teachers'

    name = fields.Char()
