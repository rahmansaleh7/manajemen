from odoo import api, fields, models, _



class Visit(models.Model):
	_name = "manajemen.visit"

	name = fields.Text(string="No", required=True, )
	tglberkunjung = fields.Date(string="Tanggal Berkunjung", required=True, )
	tiket = fields.Char(string="Tiket", 
							required=True, )
	# tiket_ids = fields.Many2one(comodel_name="manajemen.perangkat",
	# 						string="Tiketid", 
	# 						required=False, )
	tujuan = fields.Text(string="Tujuan", required=False, )
	keterangan = fields.Text(string="Keterangan", required=False, )
	status = fields.Text(string="Status", required=False, )
	