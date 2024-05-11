# -*- coding: utf-8 -*-
from openerp import http

# class DimabruContacts(http.Controller):
#     @http.route('/dimabru_contacts/dimabru_contacts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dimabru_contacts/dimabru_contacts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dimabru_contacts.listing', {
#             'root': '/dimabru_contacts/dimabru_contacts',
#             'objects': http.request.env['dimabru_contacts.dimabru_contacts'].search([]),
#         })

#     @http.route('/dimabru_contacts/dimabru_contacts/objects/<model("dimabru_contacts.dimabru_contacts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dimabru_contacts.object', {
#             'object': obj
#         })