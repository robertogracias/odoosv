from odoo import api, models, fields, _

class Nivel(models.Model):
    _name = 'acetep.nivel'
    nombre = fields.Char(string='Nombre')

class Seccion(models.Model):
    _name ='acetep.seccion' 
    nombre = fields.Char(string='Nombre')
    horario = fields.Char(string='horario')
    nivel_id = fields.Many2one(comodel_name='acetep.nivel', string='Nivel')


class Periodo(models.Model):
    _name = 'acetep.periodo'
    nombre = fields.Char(string='Nombre')

class Partersv(models.Model):
    _inherit = 'res.partner'
    nino_id = fields.One2many(comodel_name='acetep.nino', string='Contacto' ,inverse_name='partner_id' )

class Ninio(models.Model):
    _name = 'acetep.nino'
    nombre = fields.Char(string='Nombre')
    partner_id = fields.Many2one(comodel_name='res.partner' ,string='Contacto')
