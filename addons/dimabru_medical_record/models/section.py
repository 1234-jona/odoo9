# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Section(models.Model):
    _name = 'section'
    _description = 'Section of Medical History'
    
    active = fields.Boolean(string="Status")
    description = fields.Char(string='Description')
    
    name = fields.Text(string='Section')
    question_ids = fields.One2many('question','section_id', string='Questions')
    section_detail_history_id = fields.Many2one('detail.history',string="Detail HIstory")
    
    