from odoo import api, fields, models, _

class Ruang(models.Model):
	_name = "manajemen.ruang"

	no = fields.Char(string="No", required=True)
	lokasi = fields.Text(string="Lokasi", required=False, )
	noruang = fields.Text(string="No Ruang", required=False, )
	namaruang = fields.Text(string="Nama Ruang", required=False, )
	aksi = fields.Text(string="Aksi", required=False, )