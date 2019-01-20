# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bugTag(models.Model):
    _name='bm.bug.tag'
    _description='bug标示'

    name=fields.Char('名称')
    bug_ids=fields.Many2many('bm.bug',string='bug')


