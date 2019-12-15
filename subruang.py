from odoo import api, fields, models, _

class Subruang(models.Model):
	_name = "manajemen.subruang"
	_rec_name = "name"

	name = fields.Char("Name", required=True)
	no = fields.Text(string="No", required=False, )