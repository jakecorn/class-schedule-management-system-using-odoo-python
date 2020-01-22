# -*- coding: utf-8 -*-

from odoo import models, fields, api

class teaching_load(models.Model):
    _name = 'teachingload.schedule'

    day = fields.Char("Day", default="0.0")
    start_time = fields.Float(default="0.0")
    end_time = fields.Float(default="0.0")
    classes_id = fields.Many2one("teachingload.classes")
