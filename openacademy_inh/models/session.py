# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Session(models.Model):

    _inherit = 'openacademy.session'
    _description = 'openacademy_inherted_session'

    test = fields.Char(string="Test")


class Session2(models.Model):

    _name = 'openacademy.dup'
    _inherit = 'openacademy.session'
    _description = 'openacademy_duplicated_session'

    test2 = fields.Char(string="Test2")


class Session3(models.Model):
    _name = 'session.attachment'
    _inherits = {'ir.attachment': 'ir_attachment_id'}

    ir_attachment_id = fields.Many2one('ir.attachment')
    session_attachment_name = fields.Char()
