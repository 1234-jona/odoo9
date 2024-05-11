# -*- coding: utf-8 -*-
{
    'name': "Medical Record",

    'summary': """
       Medical Records with a powerful search engine.""",

    'description': """
        Medical Records
    """,

    'author': "Jonathan Lituma",
    'website': "http://www.dimabru.com.ec",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/segurity_dimabru_medical_record.xml',
        'security/ir.model.access.csv',
        'views/history.xml',
        'views/detail_history.xml',
        'views/section.xml',
        'views/questions.xml',
        'views/detail_exam.xml',
        'views/family_emergency.xml',
        'views/inmunization.xml',
        'views/vaccine.xml',
        'views/hr_word_experience.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
