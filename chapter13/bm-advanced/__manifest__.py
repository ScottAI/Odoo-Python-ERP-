# -*- coding: utf-8 -*-
{
    'name': "bug管理系统升级版",

    'summary': """
        管理项目测试过程当中发现的bug""",

    'description': """
        管理项目测试过程当中发现的bug
    """,

    'author': "Scott",
    'website': "http://www.scott-odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['bug-manage','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/bugs_adv.xml',
        'views/bugs_stage.xml',
        'views/bug_views.xml',
        'views/bug_kanban.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}