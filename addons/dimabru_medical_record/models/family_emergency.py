# -*- coding: utf-8 -*-

from openerp import models, fields, api

class FamilyEmergency(models.Model):
    _name = 'family.emergency'
    
    family_name = fields.Char(string="Name relative")
    relationship = fields.Char(string="Relationship")
    phone = fields.Integer(string="Family phone")