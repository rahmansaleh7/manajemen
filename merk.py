from odoo import api, fields, models, _

class Merk(models.Model):
	_name = "manajemen.merk"

	no = fields.Char(string="No", required=True)
	name = fields.Char(string="Merk", required=True, )
	aksi = fields.Text(string="Aksi", required=False, )