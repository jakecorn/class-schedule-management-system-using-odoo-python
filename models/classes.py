# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import custom_helper
from odoo import http,_

class teaching_load(models.Model):
    _name = 'teachingload.classes'
    custom_helper = custom_helper.custom_helper()

    name = fields.Char(compute="_get_name", store=True)
    subject_id = fields.Many2one("teachingload.subject")
    section = fields.Selection(custom_helper._get_alphabet())
    sectionload_id = fields.Many2one("teachingload.sectionload", "Class/Students")
    teacher = fields.Many2one("teachingload.teacher")
    schedule = fields.One2many("teachingload.schedule", "classes_id")
    schedule_iframe = fields.Char(compute="_schedule_iframe")

    def _schedule_iframe(self):
        for record in self:
            record.schedule_iframe = "<iframe src='class/form_view/?classes_id="+str(record.id)+"' width='100%' height='500px' frameborder='none'/>"

    @api.multi
    def view_class(self, data = None):
        print("rendered")
        return {
            'type': 'ir.actions.act_url',
            'url': 'class/form_view?classes_id='+str(self.id),
            'target': 'self',
            'res_id': self.id,
        }

    @api.depends("subject_id")
    def _get_name(self):
        for record in self:
            if record.subject_id.code:
                record.name = str(record.sectionload_id.name)+" ("+str(record.subject_id.code)+" "+str(record.subject_id.description)+")"