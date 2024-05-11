# -*- coding: utf-8 -*-

from openerp import models, fields, api

class DetailExam(models.Model):
    _name = 'detail.exam'
    
    date = fields.Date(string="Day of exam")
    result = fields.Char(string="Result")
    history_detail_exam_id = fields.Many2one('history',string='History')
    
    