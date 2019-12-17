from odoo import api, fields, models, _

class Subunit(models.Model):
	_name = "manajemen.subunit"

	no = fields.Char(string="No", required=True)
	kodeperangkat = fields.Many2one(comodel_name="manajemen.unit",
					string="Kode/Golongan perangkat", 
					required=True, )
	nosubunit = fields.Text(string="No Sub Unit", required=False, )
	name = fields.Text(string="Nama Sub Unit", required=False, )
	aksi = fields.Text(string="Aksi", required=False, )