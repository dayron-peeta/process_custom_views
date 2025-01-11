from odoo import models, fields

class ProcessModel(models.Model):
    _name = 'process.model'
    _description = 'Process'

    name = fields.Char(string='Process Name', required=True)
    type_of_process = fields.Many2one('process.type', string='Type of Process', required=True)
    specific_field_1 = fields.Char(string='Specific Field 1')
    specific_field_2 = fields.Char(string='Specific Field 2')
    specific_field_3 = fields.Char(string='Specific Field 3')

    def open_specific_view(self):
        """Abre la vista configurada en el campo view_id del tipo de proceso"""
        if not self.type_of_process.view_id:
            raise ValueError(f"El tipo de proceso '{self.type_of_process.name}' no tiene una vista definida.")
        
        return {
            'type': 'ir.actions.act_window',
            'name': f'{self.name} ({self.type_of_process.name})',
            'res_model': 'process.model',
            'view_mode': 'form',
            'views': [(self.type_of_process.view_id.id, 'form')],
            'res_id': self.id,
        }