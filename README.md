
# Módulo "Process Custom Views" para Odoo
Este módulo proporciona una solución flexible para gestionar procesos y tipos de procesos en Odoo, permitiendo la asignación de vistas backend específicas para cada tipo de proceso.

## Funcionalidad
### Gestión de Tipos de Procesos:
Permite definir tipos de procesos en el modelo process.type, asociando una vista específica (view_id) para cada tipo de proceso.

### Vistas Personalizadas para Cada Tipo de Proceso:
- Cada tipo de proceso puede tener su propia vista formulario (view_process_form_type.x) para mostrar los campos base más sus campos específicos como specific_field_1, specific_field_2, y specific_field_3.
- Se define una vista base (view_process_form_base) que contenga los campos comunes (name, type_of_process) y se  asigna por defecto .

### Proceso Dinámico:
- Al hacer clic en un tipo de proceso en la vista Kanban, se abre una vista lista filtrada que muestra los procesos de ese tipo.
- Al hacer clic en un proceso en la vista lista, se abre la vista formulario específica para ese tipo de proceso.
- Al hacer clic en **NUEVO** desde la vista lista, se abre la vista formulario específica para ese tipo de proceso y el campo type_of_process se carga automáticamente con el valor correspondiente (estos valores se pasan por contexto)

## Pasos para replicarlo

1. Definir los Modelos. El modelo process.type para gestionar los tipos de procesos y el modelo process.model para los procesos individuales. En el modelo process.type, el campo view_id permite la selección de vistas. Se define un valor predeterminado para la vista base.
```python
class ProcessType(models.Model):
    _name = 'process.type'
    _description = 'Process Type'

    name = fields.Char(string='Type Name', required=True)
    view_id = fields.Many2one(
        'ir.ui.view', 
        string='Specific View', 
        domain="[('name', 'ilike', 'process.form.type.')]",
        default=lambda self: self.env.ref('your_module_name.view_process_form_base', raise_if_not_found=False)
    )

class ProcessModel(models.Model):
    _name = 'process.model'
    _description = 'Process Model'

    name = fields.Char(string='Process Name')
    type_of_process = fields.Many2one('process.type', string='Type of Process', required=True)
    specific_field_1 = fields.Char(string='Specific Field 1')
    specific_field_2 = fields.Char(string='Specific Field 2')
    specific_field_3 = fields.Char(string='Specific Field 3')
``` 
2. Crear la Vista Base. Define la vista base que incluirá los campos comunes:
```xml
<record id="view_process_form_base" model="ir.ui.view">
    <field name="name">process.form.base</field>
    <field name="model">process.model</field>
    <field name="arch" type="xml">
        <form>
            <sheet>
                <group>
                    <field name="name"/>
                    <field name="type_of_process"/>
                </group>
            </sheet>
        </form>
    </field>
</record>
```
3. Crear las vistas Específicas para cada tipo de proceso (incluye los campos comunes y sus campos específicos):
```xml
<record id="view_process_form_type_1" model="ir.ui.view">
    <field name="name">process.form.type.1</field>
    <field name="model">process.model</field>
    <field name="arch" type="xml">
        <group>
            <field name="name"/>
            <field name="type_of_process"/>
            <field name="specific_field_1"/>
        </group>
    </field>
</record>
```
4. Configurar la acción de ventana que abre la vista lista (view_mode configurado como kanban,tree,form asegura que la acción de ventana tenga acceso a todas las vistas necesarias).
```xml
<record id="action_process_kanban" model="ir.actions.act_window">
    <field name="name">Procesos</field>
    <field name="res_model">process.type</field>
    <field name="view_mode">kanban,tree,form</field>
</record>
```
5. Crear el Menú y las Acciones. Define un menú principal y submenús para acceder a los tipos de procesos y los procesos:
```xml
<menuitem id="menu_process_management" name="Gestión de Procesos"/>
<menuitem id="menu_process_types" name="Tipos de Procesos" parent="menu_process_management" action="action_process_types"/>
<menuitem id="menu_processes" name="Procesos" parent="menu_process_management" action="action_process_kanban"/>
```
6. Configurar la Acción para el Kanban. Define la acción para abrir los procesos filtrados por tipo y pasar el contexto con el tipo de proceso (que debe precargarse al abrir el form) y la vista específica (que define que vista debe abrirse).
```python
def open_filtered_process_list(self):
    return {
        'type': 'ir.actions.act_window',
        'name': f'{self.name}',
        'res_model': 'process.model',
        'view_mode': 'tree,form',
        'domain': [('type_of_process', '=', self.id)],
        'context': {
        'default_type_of_process': self.id,  # Carga el tipo de proceso automáticamente
        'form_view_ref': self.view_id.xml_id,   # Usa la vista específica del tipo de proceso (self.view_id.xml_id obtiene la referencia completa)
        },
    }
```

Se  puede definir **create="false"** dentro de la etiqueta del tipo de vista para q no se muestre el botón **NUEVO**
   
