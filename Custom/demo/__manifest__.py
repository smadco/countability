{
    'name': 'demo',
    'version': '13.0.1.0.0',
    'category': 'extra tools',
    'summary': 'demo tool for odoo 13',
    'sequence': '10',
    'author': 'aziz',
    'maintainer': 'aziz',
    'depends': ['account','sale'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/demo.xml',


    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}

