from odoo import api, fields, models, _

class Bcp(models.Model):
	_name = "manajemen.bcp"

	no = fields.Char(string="No", required=True)
	code = fields.Text(string="Code", required=False, )
	bcpname = fields.Text(string="BCP Name", required=False, )
	dateisued = fields.Text(string="Date Isued", required=False, )
	datereview = fields.Text(string="Date Review", required=False, )
	daterevised = fields.Text(string="Date Revised", required=False, )
	detail = fields.Text(string="Detail", required=False, )