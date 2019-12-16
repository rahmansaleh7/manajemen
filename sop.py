from odoo import api, fields, models, _

class Sop(models.Model):
	_name = "manajemen.sop"
	_rec_name = "name"

	no = fields.Char(string="No", required=True)
	code = fields.Text(string="Code", required=False, )
	sopname = fields.Text(string="SOP Name", required=False, )
	dataisued = fields.Text(string="Data Isued", required=False, )
	datareview = fields.Text(string="Data Review", required=False, )
	datarevised = fields.Text(string="Data Resived", required=False, )
	detail = fields.Text(string="Detail", required=False, )