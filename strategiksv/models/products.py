# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.osv import expression
from odoo.exceptions import ValidationError

class sv_account_move(models.Model):
	_inherit = 'product.category'
	company_id=fields.Many2one('res.company',string='Company',help='Company')
	

class sv_product_tax(models.Model):
	_inherit = 'product.template'
	product_fiscal_type_id=fields.Many2one('strategiksv.product_fiscal_type',string='Tipo de producto fiscal',help='Posicion fiscal a asociar')
	sv_tipo_costo=fields.Selection([('Seguro','Seguro'), ('Flete','Flete'), ('Impuestos','Impuestos'), ('Otros','Otros')],default='Otros',string='Tipo de Costo')
#sv_descripcion_poliza=fields.Char("Descripcion Poliza")
#sv_posicion_arancelaria= fields.Char("Posicion Arancelaria")
#sv_arancel= field.Float("Arancel")
