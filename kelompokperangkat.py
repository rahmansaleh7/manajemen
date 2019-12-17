from odoo import api, fields, models, _

class Kelompokperangkat(models.Model):
	_name = "manajemen.kelompokperangkat"

	no = fields.Char(string="No", required=True)
	kodegolperangkat = fields.Many2one(comodel_name="manajemen.kodeperangkat",
										string="Kode/Golongan Perangkat", 
										required=True, )
	nokelperangkat = fields.Text(string="No Kelompok Perangkat", required=False, )
	name = fields.Char(string="Nama Kelompok Perangkat", required=True, )
	aksi = fields.Text(string="Aksi", required=False, )