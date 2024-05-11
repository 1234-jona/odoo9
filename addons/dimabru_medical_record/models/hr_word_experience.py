# -*- coding: utf-8 -*-

from openerp import models, fields, api

class HrWordExperience(models.Model):
    _name = 'hr.word.experience'
    
    employee_id = fields.Many2one('hr.employee')