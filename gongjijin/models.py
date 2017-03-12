from openerp import models, fields, api


class Djsanjin(models.Model):
	_name = 'yjjr.djsanjin'

	name = fields.Many2one('yjjr.customer', string="customer", required=True)
	company_id = fields.Many2one('yjjr.company', ondelete='restrict', string="company", required=True)
	djsanjin_mx_ids = fields.One2many('yjjr.djsanjin.mx', 'djsanjin_id', string="jiao fei qing kuang")
	#jnxz = fields.Selection([""])
	date_begin = fields.Date(string="date begin", default=fields.Date.today)
	date_cx = fields.Integer(string="date chixu")
	date_end = fields.Date(string="date end")
	customer = fields.Many2one('yjjr.customer', string="customer")
	shebao = fields.Float(string="she bao")
	gongjijin = fields.Float(string="gong ji jin")
	geshui = fields.Float(string="ge shui")
	fuwufei = fields.Float(string="fu wu fei")
	month_total = fields.Float(compute='_month_total', store=True)
	all_total = fields.Float(compute='_all_total', store=True)
	memo = fields.Text(string="memo")

	@api.depends('shebao', 'gongjijin', 'geshui', 'fuwufei')
	def _month_total(self):
		for r in self:
			r.month_total = r.shebao + r.gongjijin + r.geshui +r.fuwufei
			
	@api.onchange('shebao', 'gongjijin', 'geshui', 'fuwufei')
	def _verify_valid_month_total(self):
		if self.shebao < 0:
			return {
				'warning':{
				'title': "shebao value incorrect",
				'message': "shebao value >= 0",
				},
			}
		if self.gongjijin < 0:
			return {
				'warning':{
				'title': "gongjijin value incorrect",
				'message': "gongjijin value >= 0",
				},
			}
		if self.geshui < 0:
			return {
				'warning':{
				'title': "geshui value incorrect",
				'message': "geshui value >= 0",
				},
			}
		if self.fuwufei < 0:
			return {
				'warning':{
				'title': "fuwufei value incorrect",
				'message': "fuwufei value >= 0",
				},
			}

	@api.depends('month_total', 'all_total', 'date_cx')
	def _all_total(self):
		for r in self:			
			r.all_total = r.month_total * r.date_cx

	@api.onchange('month_total', 'all_total', 'date_cx')
	def _verify_valid_all_total(self):
		if self.date_cx < 0:
			return {
				'warning':{
				'title': "date_cx value incorrect",
				'message': "date_cx value >= 0",
				},
			}

class Djcompany(models.Model):
	_name = 'yjjr.company'

	name = fields.Char(string="company", required=True)
	djsanjin_ids = fields.One2many('yjjr.djsanjin', 'company_id', string="san jin")

class Djcustomer(models.Model):
	_name = 'yjjr.customer'

	name = fields.Char(string="name", required=True)
	sex = fields.Char(string="sex")
	mobile = fields.Char(string="mobile")
	shenfenzheng = fields.Char(string="shen fen zheng")
	gjjno = fields.Char(string="gong ji jin number")
	memo = fields.Text(string="memo")

class Djsanjin_mx(models.Model):
	_name = 'yjjr.djsanjin.mx'

	def _default_session(self):
		return self.env['yjjr.djsanjin'].browse(self._context.get('active_id'))

	# test name is nessiray
	#name = fields.Char(string="name", required=True)
	djsanjin_id = fields.Many2one('yjjr.djsanjin', ondelete='cascade', string="dai jiao san jin", default=_default_session)
	gongzi = fields.Float(string="gongzi")
	shebao = fields.Float(string="she bao")
	gongjijin = fields.Float(string="gong ji jin")
	geshui = fields.Float(string="ge shui")
	fuwufei = fields.Float(string="fu wu fei")
	#month_total = fields.Float(compute='_month_total', store=True)
	fukuanfs_id = fields.Char(string="fu kuan fang shi")
	fukuan_date = fields.Date(string="fu kuan date", default=fields.Date.today)
	dj_month = fields.Date(string="dai jiao ri qi", default=fields.Date.today)
	memo = fields.Text(string="bei zhu")


class MyModelOne(models.Model):
    _name = 'my_model_one'

    partner_id = fields.Many2one('res.partner', string='Partner')
    money = fields.Float()
    my_model_two_ids = fields.One2many('my_model_two','my_model_one_id')

class MyModelTne(models.Model):
    _name = 'my_model_two'

    partner_id = fields.Many2one('res.partner', string='Partner')
    money = fields.Float(string="money")
    all_total = fields.Float(string="all_total")
    my_model_one_id = fields.Many2one('my_model_one', required=True)

    @api.multi
    def save_model_two(self):
        return {'type': 'ir.actions.act_window_close'}




