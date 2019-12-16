from odoo import api, fields, models, _

class Kodeperangkat(models.Model):
	_name = "manajemen.kodeperangkat"

	no = fields.Char(string="No", required=True)
	noperangkat = fields.Text(string="No Perangkat", required=False, )
	golperangkat = fields.Text(string="Golongan Perangkat", required=False, )
	aksi = fields.Text(string="Aksi", required=False, )