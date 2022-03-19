from odoo import models, fields


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'A session is an occurrence of a course taught at a given time for a given audience'

    name = fields.Char(string="Name", required=True)
    start_date = fields.Date(string="Start date", required=True, )
    duration = fields.Integer(string="Duration", required=False, )
    number_seats = fields.Integer(string="Number of seats", required=False, )
    instructor = fields.Many2one(comodel_name="res.partner", string="Instructor", required=False, )
    course = fields.Many2one(comodel_name="openacademy.course", string="Course", required=False, )
