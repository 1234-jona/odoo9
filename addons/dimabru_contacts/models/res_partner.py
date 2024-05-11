# -*- coding: utf-8 -*-

from openerp import api, fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    # Acuerdos comerciales 
    type_agreement = fields.Selection([
        ('reduction', 'Reduction'),
        ('wholesale_plan', 'Wholesale plan'),
        ('extra_visibility', 'Extra visibility'),
    ], string='Type of Agreement')
    
    start_date = fields.Date(string="Start date")
    end_date = fields.Date(string='Ending date')
    contract = fields.Binary(string='Contract')
    description = fields.Text(string='Description')
    state = fields.Selection([
        ('defeated', 'Defeated'),
        ('current', 'Current'),
    ], string='State', default='defeated')
    check_push = fields.Boolean(string='Sign agreement')
    # Documentación del cliente
    type_document = fields.Selection([
        ('update', 'Update'),
        ('opening', 'Opening'),
        ('closing', 'Closing'),
    ], string='Type of Customer Documentation')
    date_document = fields.Date(string='Date document')
    document = fields.Binary(string='Document')
    document_description = fields.Char(string='Document description')
    furniture_ids = fields.One2many('furniture', 'contact_id', string='Furniture')


