from odoo import api, fields, models, _

class Datauser(models.Model):
	_name = "manajemen.datauser"

	no = fields.Char(string="No", required=False, )
	name = fields.Char(string="Username", required=False, )
	identitas = fields.Char(string="Identitas", required=False, )
	namalengkap = fields.Char(string="Nama Lengkap", required=True)
	level = fields.Char(string="Level", required=False, )
	blokir = fields.Selection(string="Blokir",
							selection=[('Y','Yes'),('N','No')],
							default='N', 
							required=True, )
	pemandu = fields.Selection(string="Pemandu",
							selection=[('Y','Yes'),('N','No')],
							required=False, )
	pengelola = fields.Selection(string="Pengelola",
							selection=[('Y','Yes'),('N','No')],
							default='N',
							required=True, )
	tempadmin = fields.Selection(string="Temp Admin",
							selection=[('Y','Yes'),('N','No')],
							required=False, )


	# docberitapublish = fields.Selection(string="Publish",
	# 	selection=[('Y','Yes'),('N','No')],default='N',required=True)