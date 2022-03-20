from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'A session is an occurrence of a course taught at a given time for a given audience'

    name = fields.Char(string="Name", required=True)
    start_date = fields.Date(string="Start date", required=True, default=fields.Date.today())
    is_active = fields.Boolean(string="Active", default=True)
    duration = fields.Integer(string="Duration", required=False, )
    number_seats = fields.Integer(string="Number of seats", required=False, )
    instructor_id = fields.Many2one(comodel_name="res.partner", string="Instructor", required=False,
                                    domain="['|', "
                                           "('instructor', '=', 'True'), "
                                           "('category_id.name', '=like', 'Teacher /%')]")
    course_id = fields.One2many(comodel_name="openacademy.course", inverse_name="session_id",
                                string="Course", required=False, )
    attendees_ids = fields.Many2many(comodel_name="res.partner", relation="session_ids",
                                     string="Attendees", )
    percentage_taken_seats = fields.Integer(string="% taken seats", compute="_compute_taken_seats")

    @api.depends('number_seats', 'attendees_ids')
    def _compute_taken_seats(self):
        for record in self:
            if record.number_seats == 0:
                record.percentage_taken_seats = 0
            else:
                count = 0
                for i in record.attendees_ids:
                    count += 1
                record.percentage_taken_seats = count / record.number_seats * 100

    @api.onchange('number_seats', 'attendees_ids')
    def _onchange_seats(self):
        if self.number_seats < 0:
            return {
                'warning': {
                    'title': "Wrong value",
                    'message': "The number of seats should be positive"
                }
            }
        else:
            count = 0
            for line in self.attendees_ids:
                count += 1
            if count > self.number_seats:
                return {
                    'warning': {
                        'title': "It is too crowded",
                        'message': "The number of seats smaller then number of attendees"
                    }
                }

    @api.constrains('instructor_id')
    def _check_instructor(self):
        for rec in self:
            not_presented = True
            for line in rec.attendees_ids:
                if line == rec.instructor_id:
                    not_presented = False
            if not_presented:
                raise ValidationError("Instructor %s is not present in the attendees of his/her own session"
                                      % rec.instructor_id.name)
