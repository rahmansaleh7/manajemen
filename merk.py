from odoo import api, fields, models, _

class Merk(models.Model):
	_name = "manajemen.merk"

	no = fields.Char(string="No", required=True)
	merk = fields.Text(string="Merk", required=False, )
	aksi = fields.Text(string="Aksi", required=False, )