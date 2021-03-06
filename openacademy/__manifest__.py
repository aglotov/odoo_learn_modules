# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Open Academy""",

    'description': """
        Open Academy module
    """,

    'author': "Oleksandr Glotov",
    'website': "https://wwind.ua",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '15.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],
    'application': True,

    # always loaded
    'data': [
        'security/openacademy_groups.xml',
        'security/course_security.xml',
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/partner_views.xml',
        'views/openacademy_menus.xml',
        'report/session_report.xml',
        'report/session_templates.xml',
        'views/dashboard.xml',
        'wizard/fill_session_views.xml',
        'data/course_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
