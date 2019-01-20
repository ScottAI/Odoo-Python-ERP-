# -*- coding: utf-8 -*-
{
    'name': "bug-wizard",

    'summary': """
        bug管理辅助使用模块""",

    'description': """
        bug管理辅助使用模块
    """,

    'author': "Scott",
    'website': "http://www.scott-odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['bug-manage'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/bug_wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}