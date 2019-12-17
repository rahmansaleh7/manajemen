from odoo import api, fields, models, _

class Unit(models.Model):
	_name = "manajemen.unit"

	no = fields.Char(string="No", required=True)
	nounit = fields.Text(string="No Unit", required=False, )
	name = fields.Char(string="Nama Unit", required=True, )
	aksi = fields.Text(string="Aksi", required=False, )