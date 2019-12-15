from odoo import api, fields, models, _

class Lokasi(models.Model):
	_name = "manajemen.lokasi"
	_rec_name = "name"

	name = fields.Char("Name", required=True)
	no = fields.Text(string="No", required=False, )