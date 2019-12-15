from odoo import api, fields, models, _

class Berita(models.Model):
	_name = "manajemen.berita"
	_rec_name = "name"

	name = fields.Char("Name", required=True)
	no = fields.Text(string="No", required=False, )