from odoo import api, fields, models, _

class Lokasi(models.Model):
	_name = "manajemen.lokasi"

	no = fields.Char(string="No", required=True)
	nolokasi = fields.Text(string="No Lokasi", required=False, )
	lokasi = fields.Text(string="Lokasi", required=False, )
<<<<<<< HEAD
	aksi = fields.Text(string="Aksi", required=False, )
=======
	aksi = fields.Text(string="Aksi", required=False, )
>>>>>>> manajemen_edit
