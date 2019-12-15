from odoo import api, fields, models, _

class Subunit(models.Model):
	_name = "manajemen.subunit"
	_rec_name = "name"

	name = fields.Char("Name", required=True)
	no = fields.Text(string="No", required=False, )