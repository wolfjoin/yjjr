# -*- coding: utf-8 -*-
{
    'name': "GongJiJin",

    'summary': """Yi Jia Jin Rong""",

    'description': """
        壹佳金融
        公积金、社保、个税
        定制办公
    """,

    'author': "WOLFJOIN",
    'website': "http://yj.yijiahouse.top",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/gongjijin.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}