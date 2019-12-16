from odoo import api, fields, models, _

class Unit(models.Model):
	_name = "manajemen.unit"

	no = fields.Char(string="No", required=True)
	nounit = fields.Text(string="No Unit", required=False, )
	namaunit = fields.Text(string="Nama Unit", required=False, )
	aksi = fields.Text(string="Aksi", required=False, )