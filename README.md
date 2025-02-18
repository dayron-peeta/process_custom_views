Módulo "Process Custom Views" para Odoo
Este módulo proporciona una solución flexible para gestionar procesos y tipos de procesos en Odoo, permitiendo la asignación de vistas backend específicas para cada tipo de proceso.

Funcionalidad
Gestión de Tipos de Procesos:
Permite definir tipos de procesos en el modelo process.type, asociando una vista específica (view_id) para cada tipo de proceso.

Vistas Personalizadas para Cada Tipo de Proceso:
Cada tipo de proceso puede tener su propia vista formulario (view_process_form_type.x) para mostrar los campos base más sus campos específicos como specific_field_1, specific_field_2, y specific_field_3.
Se define una vista base (view_process_form_base) que contenga los campos comunes (name, type_of_process) y se  asigna por defecto .

Proceso Dinámico:
Al hacer clic en un tipo de proceso en la vista Kanban, se abre una vista lista filtrada que muestra los procesos de ese tipo.
Al hacer clic en un proceso en la vista lista, se abre la vista formulario específica para ese tipo de proceso.

Pasos para replicarlo

1. Definir los Modelos. Primero, define el modelo process.type para gestionar los tipos de procesos y el modelo process.model para los procesos individuales.
class ProcessType(models.Model):
    _name = 'process.type'
    _description = 'Process Type'

    name = fields.Char(string='Type Name', required=True)
    view_id = fields.Many2one(
        'ir.ui.view', 
        string='Specific View', 
        domain="[('name', 'ilike', 'process.form.type.')]"
    )

class ProcessModel(models.Model):
    _name = 'process.model'
    _description = 'Process Model'

    name = fields.Char(string='Process Name')
    type_of_process = fields.Many2one('process.type', string='Type of Process', required=True)
    specific_field_1 = fields.Char(string='Specific Field 1')
    specific_field_2 = fields.Char(string='Specific Field 2')
    specific_field_3 = fields.Char(string='Specific Field 3')
    
2. Crear la Vista Base. Define la vista base que incluirá los campos comunes:
<record id="view_process_form_base" model="ir.ui.view">
    <field name="name">process.form.base</field>
    <field name="model">process.model</field>
    <field name="arch" type="xml">
        <form>
            <sheet>
                <group>
                    <field name="name"/>
                    <field name="type_of_process"/>
                    <field name="specific_field_1"/>
                    <field name="specific_field_2"/>
                    <field name="specific_field_3"/>
                </group>
            </sheet>
        </form>
    </field>
</record>

3. Crear las vistas Específicas para cada tipo de proceso,:
<record id="view_process_form_type_1" model="ir.ui.view">
    <field name="name">process.form.type.1</field>
    <field name="model">process.model</field>
    <field name="inherit_id" ref="your_module_name.view_process_form_base"/>
    <field name="arch" type="xml">
        <xpath expr="//group" position="inside">
            <field name="specific_field_1"/>
        </xpath>
    </field>
</record>

4. Configurar el Campo view_id. En el modelo process.type, asegúrate de que el campo view_id esté configurado para permitir la selección de vistas. Puedes establecer un valor predeterminado para la vista base:
view_id = fields.Many2one(
    'ir.ui.view', 
    string='Specific View', 
    domain="[('name', 'ilike', 'process.form.type.')]",
    default=lambda self: self.env.ref('your_module_name.view_process_form_base', raise_if_not_found=False)
)

5. Crear el Menú y las Acciones. Define un menú principal y submenús para acceder a los tipos de procesos y los procesos:
<menuitem id="menu_process_management" name="Gestión de Procesos"/>
<menuitem id="menu_process_types" name="Tipos de Procesos" parent="menu_process_management" action="action_process_types"/>
<menuitem id="menu_processes" name="Procesos" parent="menu_process_management" action="action_process_kanban"/>

6. Configurar la Acción para el Kanban. Define la acción para abrir los procesos filtrados por tipo:
def open_filtered_process_list(self):
    return {
        'type': 'ir.actions.act_window',
        'name': f'{self.name}',
        'res_model': 'process.model',
        'view_mode': 'tree,form',
        'domain': [('type_of_process', '=', self.id)],
    }
