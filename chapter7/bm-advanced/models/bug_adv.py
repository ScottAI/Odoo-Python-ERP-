# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BugAdvanced(models.Model):
    _inherit='bm.bug'
    #进阶模型当中新增一个所需时间字段
    need_time=fields.Integer('所需时间(小时)')
    #给bm.bug类的name字段增加help属性
    name=fields.Char(help='简要描述发现的bug')
    stage_id=fields.Many2one('bm.bug.stage','阶段')
    tag_ids=fields.Many2many('bm.bug.tag',string='标示')
    deadline = fields.Date('最晚解决日期')
    progress = fields.Integer('进度')
    state=fields.Selection([('draft','草稿'),('submit','提交')])
    priority = fields.Selection(
        [('0', '低'),
         ('1', '中'),
         ('2', '高')],
        '优先级',
        default='1')
    kanban_state = fields.Selection(
        [('normal', '处理中'),
         ('delay', '逾期'),
         ('done', '本阶段完成')],
        '看板状态',
        default='normal')
    color = fields.Integer('颜色')


    user_bug_count = fields.Integer(
        '待处理bug总数',
    compute='_compute_user_bug_count')

    def _compute_user_bug_count(self):
        for task in self:
            task.user_bug_count = task.search_count(
                [('user_id', '=', task.user_id.id)])

'''
    tag_ids = fields.many2many(
        comodel='bm.bug.tag',
        relation='bug_tag_rel',
        column1='bug_id',
        column2='tag_id',
        string='标示'
    )
'''
'''
class BMbug_advanced(models.Model):
    _name = 'bm.bug'
    _inherit = ['bm.bug', 'mail.thread']
'''
