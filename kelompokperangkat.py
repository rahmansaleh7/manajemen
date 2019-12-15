from odoo import api, fields, models, _

class Kelompokperangkat(models.Model):
	_name = "manajemen.kelompokperangkat"
	_rec_name = "name"

	name = fields.Char("Name", required=True)
	no = fields.Text(string="No", required=False, )