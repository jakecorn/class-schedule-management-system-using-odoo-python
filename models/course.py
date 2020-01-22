# -*- coding: utf-8 -*-

from odoo import models, fields, api

class teaching_load(models.Model):
    _name = 'teachingload.course'

    code = fields.Char(required=True)
    name = fields.Char(required=True)
    subject_ids = fields.Many2many("teachingload.subject")