# -*- coding: utf-8 -*-
{
    'name': "Compressed Gas Cylinder Serial Number Tracking",

    'summary': """
        Tracks serial number of cylinders for compressed air gas (ex. argon, oxygen, helium, co2, etc.)""",

    'description': """
        Serial Number Tracking module for compressed air gas cylinders:
            - Serial Number Tracking
            - Status of Cylinders (available, rented, down, lost)
            - Export to Excel
            - Report for Sale Order
    """,

    'author': "Adrian Paesani",
    'website': "http://www.gasolsrl.biz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/security.xml',
        #'security/ir.model.access.csv',
        'templates.xml',
        'views/cylinders.xml',
        'views/partner.xml',
        'views/session_workflow.xml',
        
        #'views/openacademy.xml',
        #'views/partner.xml',
        #'views/session_workflow.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
