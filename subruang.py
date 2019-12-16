from odoo import api, fields, models, _

class Subruang(models.Model):
	_name = "manajemen.subruang"
	_rec_name = "name"

	no = fields.Char(string="No", required=True)
	ruang = fields.Text(string="No", required=False, )
	nosubruang = fields.Text(string="No", required=False, )
	namasubruang = fields.Text(string="No", required=False, )
	aksi = fields.Text(string="No", required=False, )
