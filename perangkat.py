from odoo import api, fields, models, _



class Perangkat(models.Model):
	_name = "manajemen.perangkat"
	_rec_name = "name"

	name = fields.Char("Name", required=True)
	no = fields.Text(string="No", required=False, )
	pemilik = fields.Text(string="SKPD/UKPD/ Pemilik/ Penanggung Jawab ", required=False, )
	posisi = fields.Text(string="Ruang/Posisi", required=False, )
	noreg = fields.Text(string="No.Reg/SN/IP", required=False, )
	merk = fields.Text(string="Merk/Model", required=False, )
	spesifikasi = fields.Text(string="Spesifikasi", required=False, )
	fungsi = fields.Text(string="Fungsi", required=False, )
	visit = fields.Text(string="Visit", required=False, )
	note = fields.Text(string="Note", required=False, )
	aksi = fields.Text(string="Aksi", required=False, )