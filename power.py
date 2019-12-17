from odoo import api, fields, models, _

class Power(models.Model):
	_name = "manajemen.power"

	name = fields.Char(string="No", required=True)
	ruang = fields.Many2one(comodel_name="manajemen.ruang",
							string="Ruang", 
							required=True, )
	posisi = fields.Many2one(comodel_name="manajemen.subruang",
							string="Posisi", 
							required=True, )
	noregsn = fields.Text(string="No Reg/SN", required=False, )
	merkmodeltype = fields.Many2one(comodel_name="manajemen.merk",
									string="Merk/Model/Type", 
									required=False, )
	fungsi = fields.Text(string="Fungsi", required=False, )
	koneksilistrik = fields.Text(string="Koneksi Listrik", required=False, )
	distribusi = fields.Text(string="Distribusi", required=False, )
	visit = fields.Text(string="Visit", required=False, )
	note = fields.Text(string="Note", required=False, )
	aksi = fields.Text(string="Aksi", required=False, )