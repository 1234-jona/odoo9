# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from openerp import api, fields, models, _

class medical_rounding_procedure(models.Model):
    _name = 'medical.rounding_procedure'

#     medical_rounding_procedure_id = fields.Many2one('medical.procedure',string="Code",required=True)   
    notes = fields.Text(string="Notes") 
    medical_patient_rounding_procedure_id = fields.Many2one('medical.patient.rounding',string="Vaccines")
