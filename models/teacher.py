# -*- coding: utf-8 -*-

from odoo import models, fields, api

class teaching_load(models.Model):
    _name = 'teachingload.teacher'

    name = fields.Char(required=True)
    Highest_degree = fields.Char(required=True)
    classes_ids = fields.Many2one("teachingload.classes")