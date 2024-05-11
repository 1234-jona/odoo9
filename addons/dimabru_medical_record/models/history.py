# -*- coding: utf-8 -*-

from openerp import models, fields, api

class History(models.Model):
    _name = 'history'

    date = fields.Date(string='Date')
    patient_id = fields.Many2one('res.partner', string='Patient')
    detail_history_ids = fields.One2many('detail.history','detail_history_id', string='Medical Record')
    # birth_place = fields.Char(string="Patient's birthplace")
    type_history = fields.Selection([
        ('surgery', 'Surgery'),
        ('medication', 'Medication'),
        ('allergy', 'Allergy'),
        ('condition', 'Condition'),
        ('test', 'Test'),
        ('other', 'Other')
    ], string='Type')
    immunization_ids = fields.One2many('immunizations', 'history_inmunization_id', string='Immunizations')
    work_experience_ids = fields.One2many('hr.word.experience', 'employee_id', string='Work Experiences')
    detail_exam_ids = fields.One2many('detail.exam','history_detail_exam_id',string="Details Exam")

