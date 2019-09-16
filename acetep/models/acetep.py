# -*- coding: utf-8 -*-
from odoo import api, models, fields, _

class Nivel(models.Model):
    _name = 'acetep.nivel'
    name = fields.Char(string='Nombre')

class Seccion(models.Model):
    _name ='acetep.seccion' 
    name = fields.Char(string='Nombre')
    horario = fields.Char(string='horario')
    nivel_id = fields.Many2one(comodel_name='acetep.nivel', string='Nivel')


class Periodo(models.Model):
    _name = 'acetep.periodo'
    name = fields.Char(string='Nombre')

class Partersv(models.Model):
    _inherit = 'res.partner'
    nino_id = fields.One2many(comodel_name='acetep.nino', inverse_name='partner_id' )

class Ninio(models.Model):
    _name = 'acetep.nino'
    name = fields.Char(string='Nombre')
    partner_id = fields.Many2one(comodel_name='res.partner' ,string='Contacto')

class Invoice(models.Model):
    _inherit='account.invoice.line'
    nino_id = fields.Many2one(comodel_name='acetep.nino', string='Niño')
    nivel_id =fields.Many2one(comodel_name='acetep.nivel', string='Nivel')
    seccion_id =fields.Many2one(comodel_name='acetep.seccion', string='seccion')
    periodo_id =fields.Many2one(comodel_name='acetep.periodo', string='periodo')

