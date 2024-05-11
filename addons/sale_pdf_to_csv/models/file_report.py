# -*- coding: utf-8 -*-
from openerp import api, fields, models, _


class BaseFileReport(models.TransientModel):

    _name = 'base.file.report'
    _description = u"""In-memory model to temporarily store the files generated when loading a report.
                    We generate a new file that can be (xls, xml, etc.) in this model we are going to create csv"""

    file = fields.Binary('Generated file', readonly=True, required=True)
    filename = fields.Char('Generated file', required=True)


    def show(self, file, filename):
        report = self.create({'file': file, 'filename': filename})
        return {
            'type': 'ir.actions.act_window',
            'name': filename,
            'res_model': self._name,
            'res_id': report.id,
            'view_mode': 'form',
            'target': 'new'
        }