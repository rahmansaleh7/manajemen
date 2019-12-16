from odoo import api, fields, models, _

class Berita(models.Model):
	_name = "manajemen.berita"

	no = fields.Char(string="No", required=True)
	judul = fields.Text(string="Judul", required=False, )
	tglposting = fields.Text(string="Tanggal Posting", required=False, )
	publish = fields.Text(string="Publish", required=False, )
	aksi = fields.Text(string="Aksi", required=False, )