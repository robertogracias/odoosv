# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools 
from odoo.exceptions import ValidationError

class sv_account_journal(models.Model):
	_inherit = 'account.journal'
	sv_caja_chica = fields.Boolean("Caja chica")
	sv_formato_cheque=fields.Char("Formato cheque")

class sv_caja_chica(models.Model):
	
	@api.one
	@api.depends('line_ids', 'sv_monto_inicial')
	def _end_balance(self):
		self.sv_total = sum([line.amount for line in self.line_ids])
		self.sv_saldo = self.sv_monto_inicial - self.sv_total

	_name = 'strategiksv.cajachica'
	name = fields.Char("Caja chica")
	journal_id = fields.Many2one('account.journal',string='Libro asociado',help='Libro asociado')
	account_id = fields.Many2one(related='journal_id.default_credit_account_id', string="cuenta a utilizar")
	user_id = fields.Many2one('res.users',string='Responsable',help='Responsable')
	partner_id = fields.Many2one('res.partner',string='Proveedor asociado',help='Proveedor asociado')
	sv_monto_inicial = fields.Float("Monto inicial")
	line_ids = fields.One2many('account.payment','sv_cajachica_id','Pagos realizados')
	sv_total = fields.Float('Total de pagos',compute='_end_balance',store=True)
	sv_saldo = fields.Float("Saldo de la caja",compute='_end_balance',store=True)
	sv_fecha_apertura = fields.Date("Fecha de apertura")
	sv_fecha_cierre = fields.Date("Fecha de cierre")
	state = fields.Selection([('draft','Borrador'), ('open','Abierto'),('closed','Cerrado')],default='draft')
	
	@api.multi
	def open_cc(self):
		for cc in self:
			cc.state='open'
#			cc.sv_fecha_apertura=fields.Date.today
	
	@api.multi
	def close_cc(self):
		for cc in self:
			cc.state='closed'
#			cc.sv_fecha_cierre=fields.Date.today

class sv_payment(models.Model):
	_inherit ='account.payment'
	sv_caja_chica = fields.Boolean(related='journal_id.sv_caja_chica', store=True, string="Caja chica")
	sv_cajachica_id= fields.Many2one('strategiksv.cajachica',string='Caja chica asociada',help='Caja chica asociada')
	sv_reporte = fields.Char(related='journal_id.sv_formato_cheque', store=True, string="formato")
	sv_referencia = fields.Char("Numero cheque/transferencia")
	sv_resumen= fields.Char("Concepto del pago")
	state = fields.Selection([('draft', 'Draft'), ('posted', 'Posted'), ('sent', 'Sent'), ('reconciled', 'Reconciled'),('canceled', 'Canceled')], readonly=True, default='draft', copy=False, string="Status")
	
	@api.multi
	def cancel_payment(self):
		for cc in self:
			if cc.state == 'draft':
				cc.state='canceled'
			else:
				raise ValidationError("El pago debe estar en modo borrador")
	
	
	@api.one
	@api.constrains('sv_caja_chica', 'sv_cajachica_id')
	def _check_description(self):
		if self.sv_caja_chica == True:
			if self.sv_cajachica_id == False:
				raise ValidationError("Debe seleccionarse una caja chica")

