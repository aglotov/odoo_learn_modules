# -*- coding: utf-8 -*-
{
    'name': "Academy",

    'summary': """
        Academy: Website Test Module""",

    'description': """
        This module is designed to test website creation
    """,

    'author': "Oleksandr Glotov",
    'website': "http://wwind.ua",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '15.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_sale', 'mail', 'product'],
    'application': True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
