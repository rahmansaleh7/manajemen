from odoo import api, fields, models, _

class Lan(models.Model):
	_name = "manajemen.lan"

	no = fields.Char(string="No", required=True)
	ruang = fields.Text(string="Ruang", required=False, )
	posisi = fields.Text(string="Posisi", required=False, )
	noregsn = fields.Text(string="No Reg/SN", required=False, )
	merkmodel = fields.Text(string="Merk/Model/Type", required=False, )
	fungsi = fields.Text(string="Fungsi", required=False, )
	koneksilan = fields.Text(string="Koneksi LAN", required=False, )
	distribusi = fields.Text(string="Distribusi", required=False, )
	visit = fields.Text(string="Visit", required=False, )
	note = fields.Text(string="Note", required=False, )
	aksi = fields.Text(string="Aksi", required=False, )