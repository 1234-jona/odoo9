# -*- coding: utf-8 -*-

from openerp import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    medical_employee_id = fields.Many2one('history', string='Medical Record')
    blood_type = fields.Selection([
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ], string='Blood Type')
    
