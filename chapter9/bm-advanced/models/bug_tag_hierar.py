# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bugTagHierarchy(models.Model):
    _name='bm.bug.tag_hierar'
    _description='bug层级标示'
    _parent_store=True
    _parent_name='parent_id'
    name=fields.Char('名称')
    parent_id=fields.Many2one('bm.bug.tag_hierar','父标示',ondelete='restrict')
    parent_left=fields.Integer('父节点左侧',index=True)
    parent_right=fields.Integer('父节点右侧',index=True)

    child_ids=fields.One2many('bm.bug.tag_hierar','parent_id','子标示')