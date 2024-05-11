# -*- coding: utf-8 -*-
from openerp import http

# class DimabruMedicalRecord(http.Controller):
#     @http.route('/dimabru_medical_record/dimabru_medical_record/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dimabru_medical_record/dimabru_medical_record/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dimabru_medical_record.listing', {
#             'root': '/dimabru_medical_record/dimabru_medical_record',
#             'objects': http.request.env['dimabru_medical_record.dimabru_medical_record'].search([]),
#         })

#     @http.route('/dimabru_medical_record/dimabru_medical_record/objects/<model("dimabru_medical_record.dimabru_medical_record"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dimabru_medical_record.object', {
#             'object': obj
#         })