# -*- coding: utf-8 -*-
from odoo import api, models, fields, _

class Nivel(models.Model):
    _name = 'acetep.nivel'
    name = fields.Char(string='Nombre')

class Seccion(models.Model):
    _name ='acetep.seccion' 
    name = fields.Char(string='Nombre')
    horario = fields.Char(string='Horario')
    nivel_id = fields.Many2one(comodel_name='acetep.nivel', string='Nivel')


class Periodo(models.Model):
    _name = 'acetep.periodo'
    name = fields.Char(string='Nombre')

class Partersv(models.Model): #cliente padre
    _inherit = 'res.partner'
    nino_id = fields.One2many(comodel_name='acetep.nino', inverse_name='partner_id' )
    how = fields.Selection([('Redes sociales','Redes sociales'), ('Referido','Referido'), ('Familiar','Familiar'), ('Pagina web','Pagina web'),  ('Pasaba por el local','Pasaba por el local'), ('Alianza','Alianza'), ('Otros','Otros')])

class Nino(models.Model):
    _name = 'acetep.nino'
    name = fields.Char(string='Nombre')
    birthday = fields.Date(string="Fecha de cumpleaños")
    partner_id = fields.Many2one(comodel_name='res.partner' ,string='Padre') #Nombre del padre
    employed_id = fields.Many2one(comodel_name='hr.employee' ,string='Instructora de la clase de prueba')
    datetest = fields.Date(string="Fecha de la clase de prueba")

class Invoice(models.Model):
    _inherit='account.invoice.line'
    nino_id = fields.Many2one(comodel_name='acetep.nino', string='Niño')
    nivel_id =fields.Many2one(comodel_name='acetep.nivel', string='Nivel')
    seccion_id =fields.Many2one(comodel_name='acetep.seccion', string='seccion')
    periodo_id =fields.Many2one(comodel_name='acetep.periodo', string='periodo')

class Employed(models.Model):
    _inherit='hr.employee'
    nino_id = fields.One2many(comodel_name='acetep.nino', inverse_name='employed_id' )    
      