# -*- coding: utf-8 -*-
{
    'name': "Tutorial theme",

    'summary': """
        Tutorial Theme""",

    'description': """
        My first odoo theme
    """,

    'author': "Oleksandr Glotov",
    'website': "https://wwind.ua",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Theme/Creative',
    'version': '15.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['website', 'web'],

    # always loaded
    'data': [
        'views/layout.xml',
        'views/pages.xml',
    ],
    'assets': {
        'web.assets_common': {
            '/theme_tutorial/static/scss/primary_variables.scss',
        },
        'web.assets_frontend': {
            '/theme_tutorial/static/scss/style.scss',
        },
        'web._assets_frontend_helpers': {
            '/theme_tutorial/static/scss/bootstrap_overridden.scss',
        },
    },
    # only loaded in demonstration mode
    'demo': [],
}
