from odoo import api, fields, models, _

class Agenda(models.Model):
	_name = "manajemen.agenda"
	_rec_name = "name"

	name = fields.Char("Name", required=True)
	no = fields.Text(string="No", required=False, )