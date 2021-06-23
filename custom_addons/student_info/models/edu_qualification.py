from odoo import models, fields
from odoo import api
from datetime import date
from odoo.exceptions import UserError, ValidationError

class EduQlaification(models.Model):
    _name = "education.detail"

    degree = fields.Char()
    institute = fields.Char()
    pass_year = fields.Date()
    total_year = fields.Float(digits=(2,1))
    stu_id = fields.Many2one("student.information")

    @api.onchange('pass_year')
    def calculate_year_a(self):
        current_date = date.today()
        for rec in self:
            if rec.pass_year:
                print(f"\n\n\n{self.env.user}\n\n\n")
                if date.today() <= rec.pass_year:
                    raise ValidationError("Please Enter Correct date")
                else:
                    delta = date.today() - rec.pass_year
                    print(f"\n\n\n\n{delta.days/365}\n\n\n\n")
                    rec.total_year=delta.days/365
                    
            


