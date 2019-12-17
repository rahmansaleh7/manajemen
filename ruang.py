from odoo import api, fields, models, _

class Ruang(models.Model):
	_name = "manajemen.ruang"

	no = fields.Char(string="No", required=True)
	lokasi = fields.Many2one(comodel_name="manajemen.lokasi",
							string="Lokasi", 
							required=True, )
	noruang = fields.Text(string="No Ruang", required=False, )
	name = fields.Char(string="Nama Ruang", required=True, )
	aksi = fields.Text(string="Aksi", required=False, )