# -*- coding: utf-8 -*-
{
    'name': "student_info",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'account'],

    # always loaded
    'data': [
        'security/stu_manager_group.xml',
        'security/ir.model.access.csv',
        'views/ref_field_task.xml',
        'data/student_data_file.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/student_info.xml',
        

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': True,  # for visual in admin as app install
}
