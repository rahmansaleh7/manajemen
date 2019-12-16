from odoo import api, fields, models, _

class Bcp(models.Model):
	_name = "manajemen.bcp"
	_rec_name = "name"

	no = fields.Char(string="No", required=True)
	code = fields.Text(string="Code", required=False, )
	bppname = fields.Text(string="BPP Name", required=False, )
	dataisued = fields.Text(string="Data Isued", required=False, )
	datareview = fields.Text(string="Data Review", required=False, )
	datarevised = fields.Text(string="Data Revised", required=False, )
	detail = fields.Text(string="Detail", required=False, )