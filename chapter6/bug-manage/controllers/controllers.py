# -*- coding: utf-8 -*-
from odoo import http

class Bug(http.Controller):

    @http.route('/bug-manage')
    def BugManage(self, **kwargs):
        bugs=http.request.env['bm.bug']
        domain_bug=[('is_closed','=',False)]
        bugs_open=bugs.search(domain_bug)
        return http.request.render('bug-manage.bugs_template',{'bugs_open':bugs_open})
