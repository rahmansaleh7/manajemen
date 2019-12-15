from odoo import api, fields, models, _

class Merk(models.Model):
	_name = "manajemen.merk"
	_rec_name = "name"

	name = fields.Char("Name", required=True)
	no = fields.Text(string="No", required=False, )