from odoo import models, fields

class BugReport(models.Model):
    _name = 'bug.report'
    _description = 'Bug Report'
    _auto = False

    name = fields.Char('描述')
    is_done = fields.Boolean('是否完成')
    active = fields.Boolean('是否有效')
    user_id = fields.Many2one('res.users', '负责人')
    date_deadline = fields.Date('截止日期')

    def init(self):
        self.env.cr.execute("""
           CREATE OR REPLACE VIEW bug_report AS
           (SELECT *
           FROM bm_bug
           WHERE active = True)
        """)