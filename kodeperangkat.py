from odoo import api, fields, models, _

class Kodeperangkat(models.Model):
	_name = "manajemen.kodeperangkat"

	no = fields.Char(string="No", required=True)
	noperangkat = fields.Text(string="No Perangkat", required=False, )
	name = fields.Text(string="Golongan Perangkat", required=True, )
	aksi = fields.Text(string="Aksi", required=False, )