from odoo import api, fields, models, _

class Kelompokperangkat(models.Model):
	_name = "manajemen.kelompokperangkat"

	no = fields.Char(string="No", required=True)
	kodegolperangkat = fields.Text(string="Kode/Golongan Perangkat", required=False, )
	nokelperangkat = fields.Text(string="No Kelompok Perangkat", required=False, )
	namakelperangkat = fields.Text(string="Nama Kelompok Perangkat", required=False, )
	aksi = fields.Text(string="Aksi", required=False, )