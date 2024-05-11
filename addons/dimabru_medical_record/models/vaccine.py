# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Vaccine(models.Model):
    _name = 'vaccine'
    
    name = fields.Selection([
        ('covid', 'Covid'),
        ('difteria', 'Difteria'),
        ('tetanos', 'Tetanos'),
    ], string="Number doses")
    description = fields.Char(string="Description")
    