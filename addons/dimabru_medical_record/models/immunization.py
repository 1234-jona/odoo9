# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Immunizations(models.Model):
    _name = 'immunizations'
    
    number_doses = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
    ], string="Number doses")
    date = fields.Date(string='Date doses')
    description = fields.Char(string="Description")
    history_inmunization_id = fields.Many2one('history', string='History')
    vaccine_id = fields.Many2one('vaccine', string='Vaccine')