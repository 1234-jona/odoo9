# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Question(models.Model):
    _name = 'question'
    _description = 'Questions for Medical History'
    active = fields.Boolean(string="Status")
    
    section_id = fields.Many2one('section', string='Section')
    question = fields.Text(string='Question')
    question_detail_history_id = fields.Many2one('detail.history',string="Detail HIstory")
    