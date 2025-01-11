# -*- coding: utf-8 -*-
{
    'name': "process_custom_views",
    'version': '1.0',
    'category': 'Custom',
    'author': 'Peeta',
    'summary': 'Permite asociar vistas específicas a cada proceso.',
    'description': '''
        Este módulo permite gestionar procesos con vistas personalizadas.
        Cada proceso puede tener su propia vista específica, facilitando
        la visualización y administración de campos únicos para cada uno.
    ''',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/process_type_data.xml',
        'views/process_type_views.xml',
        'views/process_views.xml',
        'views/process_menu.xml',
    ],
    'demo': [
        'demo/process_demo.xml',
    ],
    'installable': True,
    'application': True,
}



