from odoo import api, fields, models, _

class Perangkatnondc(models.Model):
	_name = "manajemen.perangkatnondc"
	_rec_name = "name"

	name = fields.Char("Name", required=True)
	no = fields.Text(string="No", required=False, )