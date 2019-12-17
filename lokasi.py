from odoo import api, fields, models, _

class Lokasi(models.Model):
	_name = "manajemen.lokasi"

	no = fields.Char(string="No", required=True)
	nolokasi = fields.Char(string="No Lokasi", required=False, )
	name = fields.Char(string="Lokasi", 
							required=True, )