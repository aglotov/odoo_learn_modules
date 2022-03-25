from odoo import models, fields


class Courses(models.Model):
    # _name = 'academy.courses'
    _inherit = 'product.template'

    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string="Teacher")

    # taxes_id = fields.Many2many(relation='courses_taxes_rel')
    # supplier_taxes_id = fields.Many2many(relation='course_supplier_taxes_rel')
    # route_ids = fields.Many2many(relation='courses_route_rel')
    # alternative_product_ids = fields.Many2many(relation='course_alternative_product_rel')
    # accessory_product_ids = fields.Many2many(relation='course_accessory_product_rel')
