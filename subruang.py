from odoo import api, fields, models, _

class Subruang(models.Model):
	_name = "manajemen.subruang"

	no = fields.Char(string="No", required=True)
	ruang = fields.Text(string="Ruang", required=False, )
	nosubruang = fields.Text(string="No Sub Ruang", required=False, )
	namasubruang = fields.Text(string="Nama Sub Ruang", required=False, )
	aksi = fields.Text(string="Aksi", required=False, )