# -*- coding: utf-8 -*-

from datetime import date
from odoo.tests.common import TransactionCase
from odoo import fields
from odoo.exceptions import Warning

class TestWizard(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestWizard, self).setUp(*args, **kwargs)
        # 关闭开放状态的bug
        self.env['bm.bug'] \
            .search([('is_closed', '=', False)]) \
            .write({'is_closed': True})
        # 选择用demo用户的身份来运行测试
        demo_user = self.env.ref('base.user_demo')
        Todo = self.env['bm.bug'].sudo(demo_user)
        # 创建两个bug用于测试
        t0 = date.today()
        self.bug1 = BugAdvanced.create({
            'name': 'Bug1',
            'user_id': demo_user.id,
            'deadline': fields.Date.to_string(t0),
        })
        self.bug2 = BugAdvanced.create({
            'name': 'Bug2',
            'user_id': demo_user.id,
        })
        # 创建向导用例
        Wizard = self.env['bug.wizard'].sudo(demo_user)
        self.wizard = Wizard \
            .with_context(active_ids=None) \
            .create({})
    def test_populate_tasks(self):
        """Populate bugs button should add two bugs"""
        self.wizard.do_populate_tasks()
        count = len(self.wizard.bug_ids)
        self.assertEqual(
            count, 2,
            'Expected 2 populated bugs')

    def test_do_close(self):
        """批量关闭bug"""
        self.wizard.do_populate_tasks()
        self.wizard.do_close()
        self.assertEqual(
            self.bug1.is_closed,
            self.bug2.is_closed)

    def test_compute_user_bug_count(self):
        """Test count button"""
        with self.assertRaises(Warning) as e:
            self.wizard._compute_user_bug_count()
        self.assertIn(' 2 ', str(e.exception))