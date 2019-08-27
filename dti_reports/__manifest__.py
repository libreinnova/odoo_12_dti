###############################################################################
#
# Copyright(c): 2019 Libreinnova (<https://libreinnova.com/>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# All Rights Reserved
#
###############################################################################
{
    'name': 'LBR reports',
    'version': '1.0',
    'summary': 'Expansion of the standard report and account modules',
    'description': '',
    'category': 'Invoicing Management',
    'author': 'Libreinnova',
    'website': 'https://libreinnova.com/',
    'license': 'AGPL-3',
    'images': [
        'static/description/icon.png'
    ],
    'depends': [
        'account',
        'sale'
    ],
    'data': [
        'templates/assets.xml',
        'views/account_report_invoice.xml',
        'views/sale_report_saleorder.xml'
    ],
    'installable': True,
    'application': False,
}
