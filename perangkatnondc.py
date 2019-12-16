from odoo import api, fields, models, _

class Perangkatnondc(models.Model):
	_name = "manajemen.perangkatnondc"

	no = fields.Char(string="No", required=True)
	skpd = fields.Text(string="SKPD/UKDP/Pemilik", required=False, )
	ruangposisi = fields.Text(string="Ruang/Posisi", required=False, )
	noregsn = fields.Text(string="No Reg/SN", required=False, )
	merkmodel = fields.Text(string="Merk/Model", required=False, )
	spesifikasi = fields.Text(string="Spesifikasi", required=False, )
	fungsi = fields.Text(string="Fungsi", required=False, )
	visit = fields.Text(string="Visit", required=False, )
	note = fields.Text(string="Note", required=False, )
	aksi = fields.Text(string="Aksi", required=False, )