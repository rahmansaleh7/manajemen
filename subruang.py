from odoo import api, fields, models, _

class Subruang(models.Model):
	_name = "manajemen.subruang"

	no = fields.Char(string="No", required=True)
	ruang = fields.Many2one(comodel_name="manajemen.ruang", string="Ruang", required=True, )
	nosubruang = fields.Text(string="No Sub Ruang", required=False, )
	name = fields.Char(string="Nama Sub Ruang", required=True, )
	aksi = fields.Text(string="Aksi", required=False, )
