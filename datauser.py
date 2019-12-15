from odoo import api, fields, models, _

class Datauser(models.Model):
	_name = "manajemen.datauser"
	# _rec_name = "name"

	no = fields.Text(string="No", required=False, )
	username = fields.Text(string="Username", required=False, )
	identitas = fields.Text(string="Identitas", required=False, )
	namalengkap = fields.Char(string="Nama Lengkap", required=True)
	level = fields.Text(string="Level", required=False, )
	blokir = fields.Text(string="Blokir", required=False, )
	pemandu = fields.Text(string="Pemandu", required=False, )
	pengelola = fields.Text(string="Pengelola", required=False, )
	tempadmin = fields.Text(string="Temp Admin", required=False, )
	aksi = fields.Text(string="Aksi", required=False, )