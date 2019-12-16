from odoo import api, fields, models, _

class Sop(models.Model):
	_name = "manajemen.sop"

	no = fields.Char(string="No", required=True)
	code = fields.Text(string="Code", required=False, )
	sopname = fields.Text(string="SOP Name", required=False, )
	dataisued = fields.Text(string="Date Isued", required=False, )
	datareview = fields.Text(string="Date Review", required=False, )
	datarevised = fields.Text(string="Date Revised", required=False, )
	detail = fields.Text(string="Detail", required=False, )