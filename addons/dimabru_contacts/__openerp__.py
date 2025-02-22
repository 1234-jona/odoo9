# -*- coding: utf-8 -*-
{
    'name': "Contacts dimabru",

    'summary': """
        Additional fields for clients, since sales and marketing areas need these fields""",

    'description': """
        
        Additional fields for clients.    
    """,

    'author': "Jonathan Lituma",
    'website': "http://www.dimabru.com.ec",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security_furniture.xml',
         'security/ir.model.access.csv',
        'views/res_partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
