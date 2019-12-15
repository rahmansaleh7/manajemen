from odoo import api, fields, models, _

class Lan(models.Model):
	_name = "manajemen.lan"
	_rec_name = "name"

	name = fields.Char("Name", required=True)
	no = fields.Text(string="No", required=False, )