from odoo import api, fields, models, _

class Bcp(models.Model):
	_name = "manajemen.bcp"
	_rec_name = "name"

	name = fields.Char("Name", required=True)
	no = fields.Text(string="No", required=False, )