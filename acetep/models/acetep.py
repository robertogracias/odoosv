from odoo import api, models, fields, _

class Nivel(models.Model):
    _name= 'acetep.nivel'
    nombre= fields.Char()

class Seccion(models.Model):
    _name ='acetep.seccion' 
    nombre=fields.Char()


class Periodo(models.Model):
    _name= 'acetep.periodo'
    nombre=fields.Char()