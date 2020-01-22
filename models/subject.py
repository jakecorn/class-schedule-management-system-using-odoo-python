# -*- coding: utf-8 -*-

from odoo import models, fields, api

class teaching_load(models.Model):
    _name = 'teachingload.subject'

    name = fields.Char(compute="_get_name", store=True)
    code = fields.Char()
    description = fields.Char()
    units = fields.Integer(default=3)
    number_of_hours = fields.Float(default=3.0)
    is_major = fields.Boolean("Is Major Subject", default=False)
    section_load_ids = fields.Many2many("teachingload.sectionload", "subject_ids")
    course_ids = fields.Many2many("teachingload.course")

    @api.depends("code","units","description")
    def _get_name(self):

        for record in self:
            if record.code and record.description and record.units:
                record.name = str(record.code)+" - "+str(record.description)+" - "+str(record.units)+" units"
            else:
                break