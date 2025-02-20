from odoo import models, fields

class ProcessType(models.Model):
    _name = 'process.type'
    _description = 'Process Type'

    name = fields.Char(string='Type Name', required=True)
    view_id = fields.Many2one(
        'ir.ui.view', 
        string='Specific View', 
        domain="[('name', 'ilike', 'process.form.')]",
        default=lambda self: self.env.ref('process_custom_views.view_process_form_base', raise_if_not_found=False)
    )

    def open_filtered_process_list(self):
        """Método para abrir la vista filtrada de procesos"""
        return {
            'type': 'ir.actions.act_window',
            'name': f'{self.name}',
            'res_model': 'process.model',
            'view_mode': 'tree,form',
            'domain': [('type_of_process', '=', self.id)],
            'context': {
            'default_type_of_process': self.id,  # Carga el tipo de proceso automáticamente
            'form_view_ref': self.view_id.xml_id,   # Usa la vista específica del tipo de proceso
            },
        }