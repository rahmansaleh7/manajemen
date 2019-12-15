from odoo import api, fields, models, _

class Ruang(models.Model):
	_name = "manajemen.ruang"
	_rec_name = "name"

	name = fields.Char("Name", required=True)
	no = fields.Text(string="No", required=False, )