from odoo import api, fields, models, _

class Lokasi(models.Model):
	_name = "manajemen.lokasi"
	_rec_name = "name"

	no = fields.Char(string="No", required=True)
	nolokasi = fields.Text(string="No Lokasi", required=False, )
	lokasi = fields.Text(string="Lokasi", required=False, )
	aksi = fields.Text(string="aksi", required=False, )