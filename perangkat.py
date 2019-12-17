from odoo import api, fields, models, _



class Perangkat(models.Model):
	_name = "manajemen.perangkat"

	name = fields.Char(string="No", required=True, )
	pemilik = fields.Text(string="SKPD/UKPD/ Pemilik/ Penanggung Jawab ", required=False, )
	posisi = fields.Many2one(comodel_name="manajemen.ruang",
							string="Ruang/Posisi", 
							required=True, )
	noreg = fields.Char(string="No.Reg/SN/IP", required=False, )
	merk = fields.Many2one(comodel_name="manajemen.merk",
							string="Merk/Model", 
							required=True, )
	spesifikasi = fields.Text(string="Spesifikasi", required=False, )
	fungsi = fields.Char(string="Fungsi", required=False, )
	visit = fields.Char(string="Visit", required=False, )
	note = fields.Text(string="Note", required=False, )
	# visit_id = fields.One2many(comodel_name="manajemen.visit",
	# 							inverse_name="tiket_ids",
	# 							string="visit",
	# 							required=False,
	# 							ondelete="cascade",)