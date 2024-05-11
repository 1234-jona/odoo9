# -*- coding: utf-8 -*-
{
    'name' : 'Sales - Convert PDF files to CSV',
    'author' : 'Jonathan Lituma',
    'version' : '0.1',
    'summary': 'Convert PDF files to CSV',
    'description': """
Converts a PDF file to a CSV file and allows its download, it uses an external API
for its funtionability
    """,
    'category': 'Sale',
    'depends' : ['sale'],
    'data': [
        'views/file_report_view.xml',
        'views/pdf_to_csv_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
