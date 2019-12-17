from odoo import api, fields, models, _

class Lan(models.Model):
	_name = "manajemen.lan"

	name = fields.Char(string="No", required=True)
	ruang = fields.Many2one(comodel_name="manajemen.ruang",
							string="Ruang", 
							required=True, )
	posisi = fields.Many2one(comodel_name="manajemen.subruang",
							string="Posisi", 
							required=True, )
	noregsn = fields.Text(string="No Reg/SN", required=False, )
	merkmodel = fields.Many2one(comodel_name="manajemen.merk",
								string="Merk/Model/Type", 
								required=True, )
	fungsi = fields.Text(string="Fungsi", required=False, )
	koneksilan = fields.Text(string="Koneksi LAN", required=False, )
	distribusi = fields.Text(string="Distribusi", required=False, )
	visit = fields.Text(string="Visit", required=False, )
	note = fields.Text(string="Note", required=False, )
	aksi = fields.Text(string="Aksi", required=False, )