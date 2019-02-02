# -*- encoding: utf-8 -*-

from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_author = fields.Boolean(string="Author", )
