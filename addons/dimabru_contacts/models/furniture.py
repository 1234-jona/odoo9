# -*- coding: utf-8 -*-

from openerp import api, fields, models, _

class Furniture(models.Model):
    _name = 'furniture'
    
    type = fields.Selection([
        ('bedroom_furniture', 'Bedroom furniture'),
        ('office_furniture', 'Office furniture'),
        ('kitchen_furniture', 'Kitchen furniture'),
        ('bathroom_furniture', 'Bathroom furniture'),
        ('terrace_furniture', 'Terrace furniture'),
    ], string='Type of Furniture')
    delivery_date = fields.Date(string='Estimated delivery date')
    amount = fields.Float(string='Quantity of furniture')
    retirement_date = fields.Date(string='Retirement date')
    state_furniture = fields.Selection([
        ('new', 'New'),
        ('used', 'Used'),
        ('damaged', 'Damaged'),
    ], string='Furniture State')
    description = fields.Char(string='Furniture description')
    photo = fields.Binary(string='Photo of the furniture')
    contact_id = fields.Many2one('res.partner', string='Contact')