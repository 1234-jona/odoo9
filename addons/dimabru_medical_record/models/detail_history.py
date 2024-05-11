# -*- coding: utf-8 -*-

from openerp import models, fields, api

class DetailHistory(models.Model):
    _name = 'detail.history'
    
    consultation_date = fields.Date(string='Consultation Date')
    symptoms = fields.Text(string='Symptoms')
    diagnosis = fields.Text(string='Diagnosis')
    prescriptions = fields.Text(string='Prescriptions') 
    section_detail_history_ids = fields.One2many('section','section_detail_history_id',string="Sections")
    question_detail_history_ids = fields.One2many('question','question_detail_history_id',string='Questions')
    detail_history_id = fields.Many2one('history', string='Detail History')
