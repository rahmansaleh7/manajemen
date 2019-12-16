from odoo import api, fields, models, _

class Subunit(models.Model):
	_name = "manajemen.subunit"
	_rec_name = "name"

	no = fields.Char(string="No", required=True)
	kodegolperangkat = fields.Text(string="Kode/Golongan Perangkat", required=False, )
	nosubunit = fields.Text(string="No Sub Unit", required=False, )
	namasubunit = fields.Text(string="Nama Sub Unit", required=False, )
	aksi = fields.Text(string="Aksi", required=False, )