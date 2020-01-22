# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import custom_helper

class teaching_load(models.Model):
    _name = 'teachingload.sectionload'
    custom_helper = custom_helper.custom_helper()

    name = fields.Char(compute="_get_name", store=True)
    year = fields.Selection([
        ('I', "First Year"),
        ('II', "Second Year"),
        ('III', "Third Year"),
        ('IV', "Fourth Year")
    ])
    section = fields.Selection(custom_helper._get_alphabet())
    course_id = fields.Many2one("teachingload.course")
    course_id_subjects = fields.Char(compute="_get_course_subjects")
    classes_ids = fields.One2many("teachingload.classes","sectionload_id")
    schedule_iframe = fields.Char(compute="_schedule_iframe")

    @api.depends("course_id", "section")
    def _get_course_subjects(self):
        for record in self:
            record.course_id_subjects = record.course_id

    def _schedule_iframe(self):
        for record in self:
            record.schedule_iframe = "<iframe src='/teaching-load/schedule/?teaching_load_id=" + str(record.id) + "' width='100%' height='500px' frameborder='none'/>"

    @api.depends("year", "section", "course_id")
    def _get_name(self):
        for record in self:
            if record.course_id.code and record.course_id.name and record.year and record.section:
                record.name = str(record.course_id.code)+" "+str(record.course_id.name)+" - "+str(record.year)+" - "+str(record.section)

