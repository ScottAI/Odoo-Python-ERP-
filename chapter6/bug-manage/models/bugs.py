# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Bug(models.Model):
    _name='bm.bug'
    _description='bug'
    name=fields.Char('bug简述',required=True)
    detail=fields.Text(size=150)
    is_closed=fields.Boolean('是否关闭')
    close_reason=fields.Selection([('changed','已修改'),('cannot','无法修改'),('delay','推迟')],string='关闭理由')
    user_id=fields.Many2one('res.users',string='负责人')
    follower_id=fields.Many2many('res.partner',string='关注者')

    @api.multi
    def do_close(self):
        for item in self:
            item.is_closed=True
        return True


