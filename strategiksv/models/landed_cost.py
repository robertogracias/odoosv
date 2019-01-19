# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.osv import expression
from odoo.exceptions import ValidationError

class sv_landed_cost(models.Model):
	_inherit = 'stock.landed.cost'
	sv_referencia=fields.Char("Referencia")
	sv_declaracion=fields.Char("Declaracion No.")
	sv_guia=fields.Char("Guia/BL")
	sv_comentario=fields.Char("Descripcion")
	
