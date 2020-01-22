# -*- coding: utf-8 -*-
import json
from pprint import pprint

from odoo import http
from odoo.http import request

class TeachingLoad(http.Controller):

    @http.route(['/class/form_view/'], type="http", auth='public',methods=['get'],  website="True")
    def class_schedule(self, classes_id='', **kw):
        env = request.env
        classes = request.env["teachingload.classes"].sudo().search([("id", "=", classes_id)])
        return http.request.render('teaching_load.classes_schedule_template', {'classes':classes})

    @http.route(['/class/form_view/schedule/save/'] , type="json", auth='public', methods=['POST'], csrf=False)
    def class_schedule_save(self, **post):
        classes_id = int(post.get("classes_id"))

        if len(post['date_time_list']) > 0:
            schedule = request.env["teachingload.schedule"].sudo().search([("classes_id", "=", classes_id)])
            schedule.unlink()
            print(schedule)

            for data in post['date_time_list']:
                time = data['time'].split('-')
                start_time = time[0]
                end_time = time[1]
                print(start_time+" --- "+end_time)
                request.env["teachingload.schedule"].sudo().create([{
                    'day': data['day'],
                    'start_time': start_time,
                    'end_time': end_time,
                    'classes_id': classes_id,
                }])

        return "heyy"

    @http.route(['/teaching-load/schedule/'], type="http", auth='public', website="True")
    def teachingload_class_schedule(self, teaching_load_id='', **kw):
        env = request.env
        sectionload = env["teachingload.sectionload"].sudo().search([("id", "=", teaching_load_id)])
        return http.request.render('teaching_load.section_load_schedule_template', {'sectionload': sectionload})
