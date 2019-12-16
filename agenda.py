from odoo import api, fields, models, _

class Agenda(models.Model):
	_name = "manajemen.agenda"

	no = fields.Char(string="No", required=True)
	tema = fields.Text(string="Tema", required=False, )
	tglmulai = fields.Text(string="Tanggal Mulai", required=False, )
	tglselesai = fields.Text(string="Tanggal Selesai", required=False, )
	aksi = fields.Text(string="Aksi", required=False, )