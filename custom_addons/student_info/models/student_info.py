from odoo import models, fields
from odoo import api

class StudentInfo(models.Model):
    _name = "student.information"

    country = [
        ("india", "India"),
        ("america", "America"),
        ("london", "London"),
        ("china", "China"),
    ]
    status = [
        ("draft", "Draft"),
        ("approved", "Approved"),
        ("cancel", "Cancel"),
    ]
    name = fields.Char()
    Email = fields.Char()
    Mobile = fields.Char()
    Country_id = fields.Many2one("res.country")
    state = fields.Selection(status)
    edu_ids = fields.One2many("education.detail", "stu_id")
    login_user=fields.Many2one("res.users",default=lambda self:self.env.user)
            

    def draft_action(self):
        print(f"\n\n\n\nhi draft")
        for rec in self:
            rec.write({'state': 'draft'})

    def approved_action(self):
        print(f"\n\n\n\nhi approved")
        for rec in self:
            rec.write({'state': 'approved'})

    def cancel_action(self):
        print(f"\n\n\n\nhi cancel")
        for rec in self:
            rec.write({'state': 'cancel'})

    def reset_action(self):
        print(f"\n\n\n\nhi reset")
        for rec in self:
            rec.write({'state': 'draft'})
