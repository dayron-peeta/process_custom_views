from odoo import models, fields

class ProcessType(models.Model):
    _name = 'process.type'
    _description = 'Process Type'

    name = fields.Char(string='Type Name', required=True)
    view_id = fields.Many2one('ir.ui.view', string='Specific View')

    def open_action_view_process(self):
        """Método para abrir la vista filtrada de procesos"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Procesos List',
            'res_model': 'process.model',
            'view_mode': 'tree,form',
            'domain': [('type_of_process', '=', self.id)],
        }