from odoo import models, fields

class ProcessModel(models.Model):
    _name = 'process.model'
    _description = 'Process'

    name = fields.Char(string='Process Name', required=True)
    type_of_process = fields.Many2one('process.type', string='Type of Process', required=True)
    specific_field_1 = fields.Char(string='Specific Field 1')
    specific_field_2 = fields.Char(string='Specific Field 2')
    specific_field_3 = fields.Char(string='Specific Field 3')
