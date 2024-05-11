# -*- coding: utf-8 -*-
from openerp import api, fields, models, _
from openerp.exceptions import ValidationError
import base64
import uuid
import pdftables_api
import codecs

_api_key = "we6we1xmt3n2"


class SalePdfToCsvWizard(models.TransientModel):
    _name = "sale.pdf.to.csv.wizard"
    _description = "Model to load a PDF File an convert into a CSV File using an external API"

    pdf_file = fields.Binary(
        string='File to transform',
        required=True,
    )

    @api.multi
    def convert_pdf(self):
        base64_csv = ""
        for record in self:
            client = pdftables_api.Client(_api_key)
            unique_tmp_pdf_file_name = uuid.uuid4()
            pdf_tmp_path = '/tmp/' + str(unique_tmp_pdf_file_name) + '.pdf'
            with open(pdf_tmp_path, "wb") as output_file:
                output_file.write(codecs.decode(record.pdf_file, "base64"))

            try:
                csv_result = client.csv(pdf_tmp_path)
            except Exception:
                raise ValidationError(_('Error when trying to connect to external API, while converting PDF'))

            csv_bytes = csv_result.encode('utf-8')
            csv_base64_bytes = base64.b64encode(csv_bytes)
            base64_csv = csv_base64_bytes.decode('utf-8')

        return self.env['base.file.report'].show(base64_csv, 'PDF TRANSFORMADO.csv')
    
    