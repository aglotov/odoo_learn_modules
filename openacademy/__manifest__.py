# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Open Academy""",

    'description': """
        Open Academy module. The best module
    """,

    'author': "Oleksandr Glotov",
    'website': "https://wwind.ua",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '15.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/templates.xml',
        'data/course_data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/course_demo.xml',
    ],
}
