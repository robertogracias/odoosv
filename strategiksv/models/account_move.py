# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.osv import expression
from odoo.exceptions import ValidationError

class sv_account_partida(models.Model):
	_name= 'strategiksv.partida'
	name= fields.Char("Nombre de la partida")
	sv_number=fields.Char("Numero de la partida")
	state = fields.Selection([('draft','Borrador'), ('closed','Cerrado')],default='draft')
	sv_concepto = fields.Text("Concepto")
	journal_id = fields.Many2one('account.journal',string='Diario',help='Diario')


class sv_account_move(models.Model):
	_inherit = 'account.move'
	sv_concepto= fields.Text("Concepto")
	sv_elebora= fields.Char("Elabora",default=lambda self: self.env.user.company_id.sv_elebora_partida)
	sv_revisa= fields.Char("Revisa",default=lambda self: self.env.user.company_id.sv_revisa_partida)
	sv_aprueba= fields.Char("Aprueba",default=lambda self: self.env.user.company_id.sv_aprueba_partida)
	sv_noagrupar= fields.Boolean("No agrupar")
	partida_id= fields.Many2one('strategiksv.partida',string='Partida',help='Partida')
	
	@api.multi
	def post(self,invoice=False):
		inv=invoice
		super(sv_account_move,self).post(invoice=inv)
		if self.sv_noagrupar:
			self.env['job.container'].create({'sv_concepto': self.sv_concepto,'journal_id':self.journal_id,'state':'draft'})


class sv_account_move_line(models.Model):
	_inherit = 'account.move.line'
	sv_concepto= fields.Text("Concepto")
	
	@api.one
	@api.constrains('account_id')
	def _check_account(self):
		if self.account_id.internal_type == 'view':
			raise ValidationError("Debe seleccionar una cuenta que no sea de mayor")
	
class sv_account_sign(models.Model):
	_name= 'strategiksv.accountsign'
	name= fields.Char("Codigo que aplica el signo negativo")
	negativo = fields.Boolean('El Signo es negativo') 
	company_id=fields.Many2one('res.company',string='Company',help='Company')


